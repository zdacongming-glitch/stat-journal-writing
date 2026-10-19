"""Validate the skill's resource integrity; does not certify that reading occurred."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit

JOURNALS = ("jasa", "jrss-b", "aos", "biometrika")
ARTICLE_TYPES = {"original-methods", "original-theory", "computational-methods",
                 "applications-case-studies", "discussion-paper", "review", "short-communication"}


def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def canonical_doi(value):
    if not isinstance(value, str):
        return ""
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value.strip(), flags=re.I)
    value = unquote(value).lower()
    return value if re.fullmatch(r"10\.\d{4,9}/\S+", value) else ""


def inside_root(path, root):
    try:
        path.resolve().relative_to(root)
        return True
    except (ValueError, OSError, RuntimeError):
        return False


def relative_file(base, value, root, label, errors, allow_directory=False):
    if not nonempty_text(value):
        errors.append(f"{label}: missing relative file path")
        return None
    windows_path = PureWindowsPath(value)
    if Path(value).is_absolute() or windows_path.drive or windows_path.root:
        errors.append(f"{label}: file path must be relative to its resource directory")
        return None
    candidate = base / value
    if not inside_root(candidate, root):
        errors.append(f"{label}: file path escapes the skill directory")
        return None
    try:
        if not (candidate.exists() if allow_directory else candidate.is_file()):
            errors.append(f"{label}: missing file {value}")
            return None
    except OSError as exc:
        errors.append(f"{label}: cannot inspect file: {exc}")
        return None
    return candidate


def read_text(path, root, label, errors):
    if not inside_root(path, root):
        errors.append(f"{label}: resource resolves outside the skill directory")
        return None
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{label}: cannot read resource: {exc}")
        return None


def read_json(path, root, label, errors):
    content = read_text(path, root, label, errors)
    if content is not None:
        try:
            return json.loads(content)
        except ValueError as exc:
            errors.append(f"{label}: invalid JSON: {exc}")
    return None


def check_note(paper, directory, root, label, errors):
    path = relative_file(directory, paper.get("note"), root, f"{label} reading note", errors)
    if path:
        content = read_text(path, root, f"{label} reading note", errors)
        if content is not None and len(content.strip()) < 300:
            errors.append(f"{label}: individual reading note must contain at least 300 characters")


def check_read_record(paper, label, errors, cache_hashes, require_read=False):
    full = paper.get("full_text", {})
    if not isinstance(full, dict):
        errors.append(f"{label}: full_text must be an object")
        return False
    if "status" in full and not nonempty_text(full["status"]):
        errors.append(f"{label}: full_text status must be a nonempty string")
    if full.get("status") != "read":
        if require_read:
            errors.append(f"{label}: full-text reading is not marked complete")
        return False
    for field in ("url", "version", "format", "read_scope", "read_at"):
        if not nonempty_text(full.get(field)):
            errors.append(f"{label}: read record missing valid {field}")
    if nonempty_text(full.get("url")):
        try:
            source = urlsplit(full["url"])
            if source.scheme not in {"http", "https"} or not source.netloc:
                raise ValueError("expected an HTTP(S) source URL")
        except ValueError:
            errors.append(f"{label}: invalid full-text source URL")
    if nonempty_text(full.get("read_at")):
        try:
            date.fromisoformat(full["read_at"])
        except ValueError:
            errors.append(f"{label}: read_at must be an ISO calendar date")
    scope = full.get("hash_scope")
    if scope is not None and (not isinstance(scope, str) or scope not in {"source_bytes", "source", "extracted_text"}):
        errors.append(f"{label}: unrecognized source hash scope")
    source_digest, extracted_digest = full.get("sha256"), full.get("extracted_text_sha256")
    if not source_digest and (not extracted_digest or scope != "extracted_text"):
        errors.append(f"{label}: missing source-byte hash requires an explicit extracted_text hash scope")
    if scope == "extracted_text" and not extracted_digest:
        errors.append(f"{label}: extracted_text hash scope requires extracted_text_sha256")
    for field, digest in (("sha256", source_digest), ("extracted_text_sha256", extracted_digest)):
        if digest is None or digest == "":
            continue
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"{label}: invalid {field}")
    digest = source_digest or extracted_digest
    if isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest):
        if cache_hashes is not None and digest not in cache_hashes:
            errors.append(f"{label}: source SHA256 absent from supplied research cache")
    return True


def validate(root, require_complete=False, cache_root=None):
    root = Path(root).resolve()
    errors, summaries = [], []
    papers_by_id, paper_journals, doi_seen = {}, {}, {}
    cache_hashes = None
    if cache_root:
        try:
            cache_hashes = {hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(cache_root).rglob("*")
                            if p.is_file() and p.suffix.lower() in {".pdf", ".html", ".htm", ".xml", ".txt"}}
        except OSError as exc:
            errors.append(f"research cache: cannot read source bytes: {exc}")
    for path in root.rglob("*.md"):
        relative = path.relative_to(root).as_posix()
        text = read_text(path, root, relative, errors)
        if text is None:
            continue
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
            if re.match(r"^(?:https?://|mailto:|#)", target, flags=re.I):
                continue
            destination = unquote(target.split("#", 1)[0].strip("<>"))
            if destination:
                relative_file(path.parent, destination, root, f"{relative} local link", errors, allow_directory=True)
    for journal in JOURNALS:
        directory = root / "references" / "journals" / journal
        corpus_path = directory / "core-corpus.json"
        if not corpus_path.exists():
            summaries.append({"journal_id": journal, "papers": 0, "read": 0})
            if require_complete:
                errors.append(f"{journal}: missing core corpus")
            continue
        corpus = read_json(corpus_path, root, f"{journal} core corpus", errors)
        if not isinstance(corpus, dict) or not isinstance(corpus.get("papers"), list):
            errors.append(f"{journal}: expected corpus object with papers list")
            continue
        papers = corpus["papers"]
        if corpus.get("journal_id") != journal:
            errors.append(f"{journal}: corpus journal_id does not match its directory")
        read = 0
        if require_complete and len(papers) != 25:
            errors.append(f"{journal}: expected 25 core papers, found {len(papers)}")
        relative_file(directory, "guide.md", root, f"{journal} guide", errors)
        for index, paper in enumerate(papers):
            if not isinstance(paper, dict):
                errors.append(f"{journal} core paper {index + 1}: paper must be an object")
                continue
            ident = paper.get("id")
            if not nonempty_text(ident):
                errors.append(f"{journal} core paper {index + 1}: ID must be a nonempty string")
                continue
            if ident in papers_by_id:
                errors.append(f"{journal}: duplicate paper ID {ident}")
            papers_by_id[ident] = paper
            paper_journals[ident] = journal
            doi = canonical_doi(paper.get("doi"))
            if not doi:
                errors.append(f"{ident}: invalid DOI")
            if doi in doi_seen:
                errors.append(f"{ident}: duplicate core DOI also in {doi_seen[doi]}")
            doi_seen[doi] = ident
            if type(paper.get("year")) is not int or not 2000 <= paper["year"] <= date.today().year:
                errors.append(f"{ident}: formal publication year outside core range")
            for field in ("title", "authors", "article_type", "topics", "selection_reason", "citation_evidence"):
                if not paper.get(field):
                    errors.append(f"{ident}: missing {field}")
            if check_read_record(paper, ident, errors, cache_hashes, require_complete):
                read += 1
            check_note(paper, directory, root, ident, errors)
        summaries.append({"journal_id": journal, "papers": len(papers), "read": read})
        calibration_path = directory / "calibration-corpus.json"
        calibration = read_json(calibration_path, root, f"{journal} calibration corpus", errors) if calibration_path.exists() else {}
        if not isinstance(calibration, dict) or not isinstance(calibration.get("papers", []), list):
            errors.append(f"{journal}: expected calibration object with papers list")
            calibration = {}
        if calibration.get("journal_id", journal) != journal:
            errors.append(f"{journal}: calibration journal_id does not match its directory")
        calibration_papers = calibration.get("papers", [])
        calibration_read = 0
        if require_complete and len(calibration_papers) < 2:
            errors.append(f"{journal}: initial upgrade requires two additional recent calibration papers")
        for index, paper in enumerate(calibration_papers):
            if not isinstance(paper, dict):
                errors.append(f"{journal} calibration paper {index + 1}: paper must be an object")
                continue
            ident = paper.get("id")
            if not nonempty_text(ident):
                errors.append(f"{journal} calibration paper {index + 1}: ID must be a nonempty string")
                continue
            doi = canonical_doi(paper.get("doi"))
            if ident in papers_by_id or doi in doi_seen:
                errors.append(f"{ident}: calibration duplicates an existing ID or DOI")
            papers_by_id[ident] = paper
            paper_journals[ident] = journal
            doi_seen[doi] = ident
            if not doi:
                errors.append(f"{ident}: invalid calibration DOI")
            if type(paper.get("year")) is not int or not 2020 <= paper["year"] <= date.today().year:
                errors.append(f"{ident}: calibration publication year outside recent range")
            for field in ("title", "authors", "article_type", "topics", "selection_reason", "citation_evidence"):
                if not paper.get(field):
                    errors.append(f"{ident}: missing calibration {field}")
            if check_read_record(paper, ident, errors, cache_hashes, require_complete):
                calibration_read += 1
            check_note(paper, directory, root, ident, errors)
        summaries[-1].update(calibration_papers=len(calibration_papers), calibration_read=calibration_read)
    # A paper may support several topics. Reusing its existing ID/DOI is valid;
    # changing that identity in another topic is a conflict, not new evidence.
    additional_ids, additional_dois, topic_summaries = {}, {}, []
    topic_directories = sorted((root / "references" / "journals").glob("*/topics/*"))
    shared_topic_papers, shared_topic_journals = {}, {}
    # Index first so a profile can cite an earlier contribution by its stable
    # paper ID without copying its metadata or note. The owning topic below
    # still receives all source, identity and reading-card validation.
    for directory in topic_directories:
        if not inside_root(directory, root) or not directory.is_dir():
            continue
        source_topic = read_json(directory / "corpus.json", root, str(directory), [])
        extras = source_topic.get("additional_papers", []) if isinstance(source_topic, dict) else []
        if not isinstance(extras, list):
            continue
        for paper in extras:
            if not isinstance(paper, dict) or not nonempty_text(paper.get("id")):
                continue
            if paper["id"] not in shared_topic_papers:
                shared_topic_papers[paper["id"]] = paper
                shared_topic_journals[paper["id"]] = directory.parents[1].name
    for directory in topic_directories:
        label = directory.relative_to(root).as_posix()
        if not inside_root(directory, root):
            errors.append(f"{label}: topic directory resolves outside the skill directory")
            continue
        if not directory.is_dir():
            errors.append(f"{label}: topic entry must be a directory")
            continue
        journal = directory.parents[1].name
        if journal not in JOURNALS:
            errors.append(f"{label}: unsupported target journal")
        for filename in ("profile.md", "corpus.json", "terms.json"):
            relative_file(directory, filename, root, f"{label} {filename}", errors)
        terms = read_json(directory / "terms.json", root, f"{label} terms", errors)
        if not isinstance(terms, (dict, list)):
            errors.append(f"{label}: terms.json must be an object or array")
        topic = read_json(directory / "corpus.json", root, f"{label} corpus", errors)
        if not isinstance(topic, dict):
            errors.append(f"{label}: topic corpus must be an object")
            continue
        if "schema_version" in topic and (type(topic["schema_version"]) is not int or topic["schema_version"] != 1):
            errors.append(f"{label}: unsupported topic schema_version; expected 1")
        if topic.get("journal_id", journal) != journal:
            errors.append(f"{label}: topic journal_id does not match its directory")
        if not isinstance(topic.get("status"), str) or topic["status"] not in {"provisional", "complete"}:
            errors.append(f"{label}: topic status must be provisional or complete")
        target_type = topic.get("article_type_id")
        if not isinstance(target_type, str) or target_type not in ARTICLE_TYPES:
            errors.append(f"{label}: article_type_id must identify a supported stable article type")
        type_evidence = topic.get("type_evidence", {})
        if not isinstance(type_evidence, dict):
            errors.append(f"{label}: type_evidence must be an object")
            type_evidence = {}
        lists = {}
        for key in ("paper_ids", "supplementary_paper_ids"):
            values = topic.get(key, [])
            if not isinstance(values, list) or any(not nonempty_text(value) for value in values):
                errors.append(f"{label}: {key} must be an array of nonempty paper ID strings")
                values = []
            if len(values) != len(set(values)):
                errors.append(f"{label}: duplicate IDs in {key}")
            lists[key] = values
        if set(lists["paper_ids"]) & set(lists["supplementary_paper_ids"]):
            errors.append(f"{label}: primary and supplementary paper lists overlap")
        extras = topic.get("additional_papers", [])
        if not isinstance(extras, list):
            errors.append(f"{label}: additional_papers must be an array")
            extras = []
        extra_by_id, topic_dois = {}, {}
        for index, paper in enumerate(extras):
            paper_label = f"{label} additional paper {index + 1}"
            if not isinstance(paper, dict):
                errors.append(f"{paper_label}: paper must be an object")
                continue
            ident, doi = paper.get("id"), canonical_doi(paper.get("doi"))
            if not nonempty_text(ident):
                errors.append(f"{paper_label}: ID must be a nonempty string")
                ident = None
            else:
                paper_label = f"{label} {ident}"
                if ident in extra_by_id or ident in papers_by_id:
                    errors.append(f"{paper_label}: duplicate additional ID; reuse the existing paper reference")
                else:
                    extra_by_id[ident] = paper
                if ident in additional_ids and additional_ids[ident] != (journal, doi):
                    errors.append(f"{paper_label}: additional ID conflicts with an existing topic record")
                additional_ids[ident] = (journal, doi)
            if not doi:
                errors.append(f"{paper_label}: invalid DOI")
            else:
                if doi in doi_seen:
                    errors.append(f"{paper_label}: DOI already exists as {doi_seen[doi]}; reuse its existing ID")
                if doi in topic_dois:
                    errors.append(f"{paper_label}: duplicate additional DOI also in {topic_dois[doi]}")
                topic_dois[doi] = ident
                if doi in additional_dois and additional_dois[doi] != (journal, ident):
                    errors.append(f"{paper_label}: DOI conflicts with an existing topic ID or journal")
                additional_dois[doi] = (journal, ident)
            if paper.get("journal_id") != journal:
                errors.append(f"{paper_label}: additional paper must identify the target journal")
            year = paper.get("year")
            if type(year) is not int or not 1 <= year <= date.today().year:
                errors.append(f"{paper_label}: formal publication year outside supported range")
            for field in ("title", "authors", "article_type", "topics", "selection_reason", "citation_evidence"):
                if not paper.get(field):
                    errors.append(f"{paper_label}: missing additional-paper {field}")
            # Even supplementary or unmatched types must pass source/note checks.
            check_read_record(paper, paper_label, errors, cache_hashes)
            check_note(paper, directory, root, paper_label, errors)
        resolved, referenced_dois = {}, {}
        for ident in lists["paper_ids"] + lists["supplementary_paper_ids"]:
            paper = extra_by_id.get(ident) or papers_by_id.get(ident) or shared_topic_papers.get(ident)
            if not paper:
                errors.append(f"{label}: unknown paper ID {ident}")
                continue
            resolved[ident] = paper
            actual_journal = (paper.get("journal_id") if ident in extra_by_id
                              else paper_journals.get(ident, shared_topic_journals.get(ident)))
            if actual_journal != journal:
                errors.append(f"{label}: {ident} belongs to a different journal")
            doi = canonical_doi(paper.get("doi"))
            if doi and doi in referenced_dois and referenced_dois[doi] != ident:
                errors.append(f"{label}: duplicate referenced DOI under different IDs")
            if doi:
                referenced_dois[doi] = ident
        for ident, evidence in type_evidence.items():
            if ident not in resolved:
                errors.append(f"{label}: type evidence references an unlisted paper ID {ident}")
            if not isinstance(evidence, dict):
                errors.append(f"{label} {ident}: article type evidence must be an object")
                continue
            evidence_type = evidence.get("article_type_id")
            if not isinstance(evidence_type, str) or evidence_type not in ARTICLE_TYPES:
                errors.append(f"{label} {ident}: unsupported evidence article_type_id")
            if not nonempty_text(evidence.get("basis")):
                errors.append(f"{label} {ident}: article type evidence requires a nonempty basis")
        read_dois = set()
        for ident in lists["paper_ids"]:
            paper = resolved.get(ident)
            if not paper:
                continue
            full = paper.get("full_text", {})
            if not isinstance(full, dict) or full.get("status") != "read":
                continue
            matched_type = type_evidence.get(ident, {})
            if not isinstance(matched_type, dict):
                continue
            if matched_type.get("article_type_id") != target_type or not nonempty_text(matched_type.get("basis")):
                if topic.get("status") == "complete":
                    errors.append(f"{label} {ident}: complete topic requires evidence matching the target article type")
                continue
            actual_journal = (paper.get("journal_id") if ident in extra_by_id
                              else paper_journals.get(ident, shared_topic_journals.get(ident)))
            doi = canonical_doi(paper.get("doi"))
            if actual_journal == journal and doi:
                read_dois.add(doi)
        if topic.get("status") == "complete" and len(read_dois) < 10:
            errors.append(f"{label}: complete topic requires ten distinct read papers in the target journal and article type")
        topic_summaries.append({"path": label, "status": topic.get("status"), "matching_read_papers": len(read_dois)})
    return {"ok": not errors, "journals": summaries, "topics": topic_summaries, "errors": errors,
            "limitation": "Integrity checks cannot establish whether full-text reading occurred, whether papers match a topic semantically, or whether writing rules and article-type evidence are sound. These require evidence review."}


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
