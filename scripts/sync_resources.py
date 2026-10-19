"""Preview or export only approved skill resources to an existing Git worktree."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

from check_resources import validate


def git(worktree, *arguments, check=True):
    result = subprocess.run(["git", "-C", str(worktree), *arguments], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def managed_files(source):
    result = []
    for relative in (Path("SKILL.md"), Path("agents/openai.yaml")):
        if (source / relative).is_file():
            result.append(relative)
    for folder, suffixes in (("references", {".md", ".json"}), ("scripts", {".py"})):
        for path in (source / folder).rglob("*"):
            if path.is_file() and path.suffix.lower() in suffixes:
                relative = path.relative_to(source)
                if any(part.startswith(".") or part == "__pycache__" for part in relative.parts):
                    continue
                if ".local." in path.name:
                    continue
                result.append(relative)
    return sorted(set(result))


def digest(path):
    return hashlib.sha256(path.read_bytes()).digest() if path.is_file() else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    config_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    parser.add_argument("--config", type=Path, default=config_home / "skill-maintenance" / "stat-journal-writing.json")
    parser.add_argument("--worktree", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--push", action="store_true")
    parser.add_argument("--message", default="Update statistical journal writing resources")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8-sig")) if args.config.is_file() else {}
    configured_path = args.worktree or config.get("worktree")
    if not configured_path:
        parser.error("No publishing worktree configured; provide --worktree without changing the writing task")
    if args.push and args.worktree is None and not config.get("automatic_sync_enabled", False):
        parser.error("Automatic synchronization is not enabled in this installation")
    source, worktree = args.source.resolve(), Path(configured_path).resolve()
    if source == worktree or source in worktree.parents or worktree in source.parents:
        parser.error("Installed skill and publishing worktree must be separate non-nested directories")
    if not (worktree / ".git").exists():
        parser.error("Use an existing configured publishing worktree")
    if config.get("repository_full_name") and Path(config.get("worktree", "")).resolve() == worktree:
        origin = git(worktree, "remote", "get-url", "origin")
        repository = origin.split("github.com", 1)[-1].lstrip(":/").removesuffix(".git").rstrip("/")
        if repository.lower() != config["repository_full_name"].lower():
            parser.error("Configured repository and worktree origin differ; inspect before synchronizing")
    if args.push and not args.apply:
        parser.error("--push requires --apply")
    report = validate(source, require_complete=True)
    if not report["ok"]:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    resources = managed_files(source)
    changed = [p for p in resources if digest(source / p) != digest(worktree / p)]
    preview = {"source": str(source), "worktree": str(worktree), "mode": "apply" if args.apply else "preview",
               "files": [p.as_posix() for p in changed], "preserves_repository_readme": True,
               "deletes_files": False, "push_requested": args.push}
    print(json.dumps(preview, ensure_ascii=False, indent=2), flush=True)
    if not args.apply:
        return
    if git(worktree, "status", "--porcelain"):
        raise RuntimeError("Publishing worktree has existing changes; retain them and reconcile before export")
    branch = git(worktree, "symbolic-ref", "--short", "HEAD")
    if args.push:
        git(worktree, "fetch", "origin")
        remote_ref = f"refs/remotes/origin/{branch}"
        if git(worktree, "rev-parse", "HEAD") != git(worktree, "rev-parse", remote_ref):
            raise RuntimeError("Local and remote heads differ; reconcile without force-pushing before export")
    if not changed:
        print("No resource changes; no commit or push was made.")
        return
    for relative in changed:
        target = worktree / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / relative, target)
    git(worktree, "diff", "--check")
    git(worktree, "add", "--", *[p.as_posix() for p in changed])
    if args.push:
        git(worktree, "commit", "-m", args.message)
        git(worktree, "push", "origin", branch)
        local = git(worktree, "rev-parse", "HEAD")
        remote = git(worktree, "ls-remote", "origin", f"refs/heads/{branch}").split()[0]
        if local != remote:
            raise RuntimeError("Remote commit differs after push; inspect before retrying")
        print(json.dumps({"pushed": True, "branch": branch, "commit": local}, ensure_ascii=False))
    else:
        print("Exported and staged the listed files. No commit or push was made.")


if __name__ == "__main__":
    main()
