"""Validate the skill's resource integrity; does not certify that reading occurred."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path

JOURNALS = ("jasa", "jrss-b", "aos", "biometrika")


def validate(root, require_complete=False, cache_root=None):
    errors, summaries = [], []
    papers_by_id, paper_journals, doi_seen = {}, {}, {}
    cache_hashes = None
    if cache_root:
        cache_hashes = {hashlib.sha256(p.read_bytes()).hexdigest() for p in cache_root.rglob("*")
                        if p.is_file() and p.suffix.lower() in {".pdf", ".html", ".htm", ".xml", ".txt"}}
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8-sig")
        relative = path.relative_to(root).as_posix()
        prose = re.sub(r"```[^\n]*\n.*?```", "", text, flags=re.S)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        if re.search(r"\\[()\[\]]", prose):
            errors.append(f"{relative}: disallowed Markdown math delimiter")
        display_count = 0
        for line in prose.splitlines():
            if "$$" in line:
                if line.strip() != "$$":
                    errors.append(f"{relative}: display math delimiter must occupy its own line")
                display_count += 1
        if display_count % 2:
            errors.append(f"{relative}: unpaired display math delimiter")
        if re.search(r"(?:[A-Za-z]:[\\/]Users[\\/]|/Users/|/home/)[^\s]+", prose):
            errors.append(f"{relative}: personal absolute path in shared prose")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"^(?:https?://|mailto:|#)", target):
                continue
            destination = target.split("#", 1)[0].strip("<>")
            if destination and not (path.parent / destination).exists():
                errors.append(f"{relative}: broken local link {destination}")
    for journal in JOURNALS:
        directory = root / "references" / "journals" / journal
        corpus_path = directory / "core-corpus.json"
        if not corpus_path.exists():
            summaries.append({"journal_id": journal, "papers": 0, "read": 0})
            if require_complete:
                errors.append(f"{journal}: missing core corpus")
            continue
        try:
            corpus = json.loads(corpus_path.read_text(encoding="utf-8-sig"))
        except (ValueError, OSError) as exc:
            errors.append(f"{journal}: invalid core corpus: {exc}")
            continue
        if not isinstance(corpus, dict) or not isinstance(corpus.get("papers"), list):
            errors.append(f"{journal}: expected corpus object with papers list")
            continue
        papers = corpus["papers"]
        if corpus.get("journal_id") != journal:
            errors.append(f"{journal}: corpus journal_id does not match its directory")
        read = 0
        if require_complete and len(papers) != 25:
            errors.append(f"{journal}: expected 25 core papers, found {len(papers)}")
        if not (directory / "guide.md").is_file():
            errors.append(f"{journal}: missing guide.md")
        for paper in papers:
            ident = paper.get("id", "?")
            if ident in papers_by_id:
                errors.append(f"{journal}: duplicate paper ID {ident}")
            papers_by_id[ident] = paper
            paper_journals[ident] = journal
            doi = paper.get("doi", "").lower().removeprefix("https://doi.org/")
            if not re.match(r"^10\.\d{4,9}/\S+$", doi):
                errors.append(f"{ident}: invalid DOI")
            if doi in doi_seen:
                errors.append(f"{ident}: duplicate core DOI also in {doi_seen[doi]}")
            doi_seen[doi] = ident
            if not isinstance(paper.get("year"), int) or not 2000 <= paper["year"] <= date.today().year:
                errors.append(f"{ident}: formal publication year outside core range")
            for field in ("title", "authors", "article_type", "topics", "selection_reason", "citation_evidence"):
                if not paper.get(field):
                    errors.append(f"{ident}: missing {field}")
            full = paper.get("full_text", {})
            if full.get("status") == "read":
                read += 1
                for field in ("url", "version", "format", "read_scope", "read_at"):
                    if not full.get(field):
                        errors.append(f"{ident}: read record missing {field}")
                digest = full.get("sha256") or full.get("extracted_text_sha256") or ""
                if not full.get("sha256") and full.get("hash_scope") != "extracted_text":
                    errors.append(f"{ident}: missing source-byte hash requires an explicit extracted_text hash scope")
                if not re.fullmatch(r"[0-9a-f]{64}", digest):
                    errors.append(f"{ident}: invalid source SHA256")
                elif cache_hashes is not None and digest not in cache_hashes:
                    errors.append(f"{ident}: source SHA256 absent from supplied research cache")
            elif require_complete:
                errors.append(f"{ident}: full-text reading is not marked complete")
            note = paper.get("note", "")
            if not note or not (directory / note).is_file():
                errors.append(f"{ident}: missing individual reading note")
            elif len((directory / note).read_text(encoding="utf-8-sig")) < 300:
                errors.append(f"{ident}: reading note is unexpectedly short")
        summaries.append({"journal_id": journal, "papers": len(papers), "read": read})
        calibration_path = directory / "calibration-corpus.json"
        try:
            calibration = json.loads(calibration_path.read_text(encoding="utf-8-sig")) if calibration_path.is_file() else {}
            if not isinstance(calibration, dict) or not isinstance(calibration.get("papers", []), list):
                raise ValueError("expected calibration object with papers list")
        except (ValueError, OSError) as exc:
            errors.append(f"{journal}: invalid calibration corpus: {exc}")
            calibration = {}
        calibration_papers = calibration.get("papers", [])
        calibration_read = 0
        if require_complete and len(calibration_papers) < 2:
            errors.append(f"{journal}: initial upgrade requires two additional recent calibration papers")
        for paper in calibration_papers:
            ident = paper.get("id", "?")
            doi = paper.get("doi", "").lower().removeprefix("https://doi.org/")
            if ident in papers_by_id or doi in doi_seen:
                errors.append(f"{ident}: calibration duplicates an existing ID or DOI")
            papers_by_id[ident] = paper
            paper_journals[ident] = journal
            doi_seen[doi] = ident
            if not re.match(r"^10\.\d{4,9}/\S+$", doi):
                errors.append(f"{ident}: invalid calibration DOI")
            if not isinstance(paper.get("year"), int) or not 2020 <= paper["year"] <= date.today().year:
                errors.append(f"{ident}: calibration publication year outside recent range")
            for field in ("title", "authors", "article_type", "topics", "selection_reason", "citation_evidence"):
                if not paper.get(field):
                    errors.append(f"{ident}: missing calibration {field}")
            full = paper.get("full_text", {})
            if full.get("status") == "read":
                calibration_read += 1
                for field in ("url", "version", "format", "read_scope", "read_at"):
                    if not full.get(field):
                        errors.append(f"{ident}: calibration read record missing {field}")
                digest = full.get("sha256") or full.get("extracted_text_sha256") or ""
                if not full.get("sha256") and full.get("hash_scope") != "extracted_text":
                    errors.append(f"{ident}: calibration extracted-text hash must identify its scope")
                if not re.fullmatch(r"[0-9a-f]{64}", digest):
                    errors.append(f"{ident}: invalid calibration source hash")
                elif cache_hashes is not None and digest not in cache_hashes:
                    errors.append(f"{ident}: calibration source hash absent from research cache")
            elif require_complete:
                errors.append(f"{ident}: calibration reading not complete")
            note = paper.get("note", "")
            if not note or not (directory / note).is_file():
                errors.append(f"{ident}: missing calibration reading note")
        summaries[-1].update(calibration_papers=len(calibration_papers), calibration_read=calibration_read)
    for topic_path in (root / "references" / "journals").glob("*/topics/*/corpus.json"):
        try:
            topic = json.loads(topic_path.read_text(encoding="utf-8-sig"))
        except (ValueError, OSError) as exc:
            errors.append(f"{topic_path.relative_to(root)}: invalid topic corpus: {exc}")
            continue
        journal = topic_path.parents[2].name
        target_type = topic.get("article_type_id")
        type_evidence = topic.get("type_evidence", {})
        if topic.get("status") == "complete" and not target_type:
            errors.append(f"{topic_path.relative_to(root)}: complete topic must identify its article_type_id")
        extra = {p["id"]: p for p in topic.get("additional_papers", [])}
        resolved = {ident: (extra.get(ident) or papers_by_id.get(ident)) for ident in topic.get("paper_ids", [])}
        read_dois = set()
        for ident, paper in resolved.items():
            if not paper:
                errors.append(f"{topic_path.relative_to(root)}: unknown paper ID {ident}")
                continue
            if ident not in extra and paper_journals.get(ident) != journal:
                errors.append(f"{topic_path.relative_to(root)}: {ident} belongs to a different journal")
                continue
            if ident in extra:
                if paper.get("journal_id") != journal:
                    errors.append(f"{ident}: additional topic paper must identify the target journal")
                    continue
                for field in ("title", "authors", "year", "doi", "article_type", "topics", "selection_reason", "citation_evidence", "note"):
                    if not paper.get(field):
                        errors.append(f"{ident}: missing additional-paper {field}")
                if paper.get("note") and not (topic_path.parent / paper["note"]).is_file():
                    errors.append(f"{ident}: missing additional-paper reading note")
            full = paper.get("full_text", {})
            if full.get("status") == "read":
                matched_type = type_evidence.get(ident, {})
                if not target_type or matched_type.get("article_type_id") != target_type or not matched_type.get("basis"):
                    if topic.get("status") == "complete":
                        errors.append(f"{ident}: complete topic requires evidence matching the target article type")
                    continue
                for field in ("url", "version", "format", "read_scope", "read_at"):
                    if not full.get(field):
                        errors.append(f"{ident}: topic read record missing {field}")
                digest = full.get("sha256") or full.get("extracted_text_sha256") or ""
                if not re.fullmatch(r"[0-9a-f]{64}", digest):
                    errors.append(f"{ident}: topic reading requires a valid source hash")
                elif cache_hashes is not None and digest not in cache_hashes:
                    errors.append(f"{ident}: topic source hash absent from supplied cache")
                doi = paper.get("doi", "").lower().removeprefix("https://doi.org/")
                if re.match(r"^10\.\d{4,9}/\S+$", doi):
                    read_dois.add(doi)
        if topic.get("status") == "complete" and len(read_dois) < 10:
            errors.append(f"{topic_path.relative_to(root)}: complete topic requires ten distinct read papers in the target journal and article type")
    return {"ok": not errors, "journals": summaries, "errors": errors,
            "limitation": "Integrity checks cannot establish whether full-text reading or semantic review occurred."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--cache-root", type=Path)
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.require_complete, args.cache_root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
