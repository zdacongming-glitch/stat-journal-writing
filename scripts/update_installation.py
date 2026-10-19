"""Preview or safely apply an upstream update to a Git or copied installation.

Copied installations keep an external baseline in CODEX_HOME/skill-maintenance.
Use --base-revision with a trusted upstream commit to bootstrap an older copy.
No branch, remote configuration, or remote repository is forcefully rewritten.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True
from check_resources import validate
from sync_resources import managed_files

DEFAULT_REPOSITORY = "zdacongming-glitch/stat-journal-writing"


def git(root, *arguments, check=True):
    command = ["git", "--no-optional-locks"] + (["-C", str(root)] if root else []) + list(arguments)
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Git command failed")
    return result


def output(root, *arguments):
    return git(root, *arguments).stdout.strip()


def safe_path(root, relative):
    """Reject traversal, links, and file/directory collisions before any write."""
    relative = PurePosixPath(relative)
    if relative.is_absolute() or not relative.parts or any(
            part in {".", ".."} or ":" in part or "\\" in part for part in relative.parts):
        raise RuntimeError(f"Unsafe managed path: {relative}")
    target = root
    for index, part in enumerate(relative.parts):
        target = target / part
        if target.is_symlink() or (hasattr(target, "is_junction") and target.is_junction()):
            raise RuntimeError(f"Refusing linked managed path: {relative}")
        if index < len(relative.parts) - 1 and target.exists() and not target.is_dir():
            raise RuntimeError(f"Managed path parent is a file: {relative}")
    if not target.resolve().is_relative_to(root):
        raise RuntimeError(f"Managed path escapes installation: {relative}")
    if target.exists() and not target.is_file():
        raise RuntimeError(f"Managed file collides with a directory: {relative}")
    return target


def snapshot(root):
    return {path.as_posix(): text_digest(safe_path(root, path.as_posix()))
            for path in managed_files(root)}


def text_digest(path):
    # All managed extensions are text. Git autocrlf must not look like a local edit.
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def digest(root, relative):
    path = safe_path(root, relative)
    return text_digest(path) if path.is_file() else None


def independent_git_root(source):
    # rev-parse alone would mistake an enclosing configuration repository for this skill.
    if not (source / ".git").exists():
        return False
    result = git(source, "rev-parse", "--show-toplevel", check=False)
    if result.returncode or Path(result.stdout.strip()).resolve() != source:
        raise RuntimeError("The installation has .git but is not its own Git worktree root")
    return True


def read_state(path, source, repository):
    if not path.exists():
        return None
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict) or not isinstance(value.get("source"), str):
        raise RuntimeError("Installation state is invalid; inspect it without overwriting it")
    if Path(value["source"]).resolve() != source:
        raise RuntimeError("State belongs to another installation; choose a separate --state path")
    if not isinstance(value.get("repository_full_name"), str) or value["repository_full_name"].lower() != repository.lower():
        raise RuntimeError("State repository differs from --repository")
    if not isinstance(value.get("installed_revision"), str) or not re.fullmatch(r"[0-9a-f]{40}", value["installed_revision"]):
        raise RuntimeError("State lacks a valid installed_revision")
    return value


def atomic_state(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def checked_revision(upstream, revision, latest):
    if not re.fullmatch(r"[0-9a-fA-F]{7,40}", revision):
        raise RuntimeError("Baseline revision must be a trusted 7-40 character hexadecimal commit")
    commit = output(upstream, "rev-parse", "--verify", revision + "^{commit}")
    if git(upstream, "merge-base", "--is-ancestor", commit, latest, check=False).returncode:
        raise RuntimeError("Baseline revision is not an ancestor of the upstream default branch")
    return commit


def revision_snapshot(upstream, revision, latest):
    # The isolated clone may be checked out freely; the installation is never reset.
    output(upstream, "checkout", "--quiet", "--detach", revision)
    try:
        return snapshot(upstream)
    finally:
        output(upstream, "checkout", "--quiet", "--detach", latest)


def copied_plan(source, upstream, latest, state, base_revision):
    incoming = snapshot(upstream)
    baseline = None
    blockers = []
    baseline_revision = None
    if state or base_revision:
        baseline_revision = checked_revision(
            upstream, state["installed_revision"] if state else base_revision, latest)
        if state and base_revision and checked_revision(upstream, base_revision, latest) != baseline_revision:
            raise RuntimeError("--base-revision conflicts with the saved installation baseline")
        baseline = revision_snapshot(upstream, baseline_revision, latest)
        if state and state.get("managed_files") is not None and state["managed_files"] != baseline:
            raise RuntimeError("Saved file hashes differ from the upstream baseline; inspect the state")
        for relative, old_hash in baseline.items():
            if digest(source, relative) != old_hash:
                blockers.append(f"Local change or deletion: {relative}")
    else:
        # Only upstream-owned paths may establish a first baseline. Additional topics
        # are local resources and are preserved when no upstream path collides.
        for relative, new_hash in incoming.items():
            local_hash = digest(source, relative)
            if local_hash is not None and local_hash != new_hash:
                blockers.append(f"No trusted baseline for differing file: {relative}; use --base-revision")
        baseline = {relative: new_hash for relative, new_hash in incoming.items()
                    if digest(source, relative) is not None}
    baseline_paths = {os.path.normcase(relative): relative for relative in baseline}
    for relative, new_hash in incoming.items():
        old_path = baseline_paths.get(os.path.normcase(relative))
        if old_path is not None and old_path != relative:
            blockers.append(f"Case-only upstream rename requires manual reconciliation: {old_path} -> {relative}")
        if relative not in baseline and digest(source, relative) not in {None, new_hash}:
            blockers.append(f"Upstream addition collides with local file: {relative}")
    changed = [relative for relative, new_hash in incoming.items()
               if digest(source, relative) != new_hash]
    deleted = sorted(set(baseline) - set(incoming))
    local_resources = sorted(set(snapshot(source)) - set(incoming) - set(deleted))
    return {"files": sorted(changed), "removed_files": deleted,
            "preserved_local_files": local_resources, "blockers": blockers,
            "baseline_revision": baseline_revision}, incoming


def validate_candidate(source, upstream, plan, staging):
    shutil.copytree(source, staging, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
                    symlinks=True)
    for relative in plan["files"]:
        target = safe_path(staging, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(safe_path(upstream, relative), target)
    for relative in plan["removed_files"]:
        safe_path(staging, relative).unlink()
    report = validate(staging, require_complete=True)
    if not report["ok"]:
        raise RuntimeError("Updated installation failed resource validation: " + "; ".join(report["errors"]))


def apply_copy(source, upstream, plan, original, state_path, state_value):
    if snapshot(source) != original:
        raise RuntimeError("Installation changed after preview; rerun before applying")
    touched = plan["files"] + plan["removed_files"]
    originals = {relative: safe_path(source, relative).read_bytes()
                 if safe_path(source, relative).is_file() else None for relative in touched}
    try:
        for relative in plan["files"]:
            target = safe_path(source, relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(safe_path(upstream, relative).read_bytes())
        for relative in plan["removed_files"]:
            # Deletions are limited to exact, unchanged files from the verified baseline.
            safe_path(source, relative).unlink()
        atomic_state(state_path, state_value)
    except BaseException:
        for relative, previous in originals.items():
            target = safe_path(source, relative)
            if previous is None:
                if target.is_file():
                    target.unlink()
            else:
                target.write_bytes(previous)
        raise


def git_plan(source, upstream, latest):
    blockers = []
    head = output(source, "rev-parse", "HEAD")
    if output(source, "status", "--porcelain", "--untracked-files=all"):
        blockers.append("Git installation has local changes or untracked files")
    if git(source, "symbolic-ref", "--quiet", "HEAD", check=False).returncode:
        blockers.append("Git installation has a detached HEAD")
    # Check ancestry in the isolated clone so preview never fetches into the installation.
    if git(upstream, "cat-file", "-e", head + "^{commit}", check=False).returncode:
        blockers.append("Installed commit is absent from upstream history (fork commits or divergent history)")
    elif git(upstream, "merge-base", "--is-ancestor", head, latest, check=False).returncode:
        blockers.append("Installed branch cannot fast-forward to the upstream default branch")
    tracked = set(git(source, "ls-files", "-z").stdout.rstrip("\0").split("\0"))
    upstream_paths = git(upstream, "ls-files", "-z").stdout.rstrip("\0").split("\0")
    for relative in upstream_paths:
        # Git can overwrite ignored files; explicitly protect these collisions too.
        target = safe_path(source, relative)
        if relative not in tracked and target.exists():
            blockers.append(f"Upstream addition collides with untracked or ignored file: {relative}")
    changed = output(upstream, "diff", "--name-only", head, latest).splitlines() if not blockers else []
    return {"files": changed, "removed_files": [], "preserved_local_files": [],
            "blockers": blockers, "installed_revision": head,
            "incoming_new_paths": [relative for relative in upstream_paths if relative not in tracked]}


def apply_git(source, upstream_url, latest, plan, state_path, state_value):
    if output(source, "status", "--porcelain", "--untracked-files=all") or output(source, "rev-parse", "HEAD") != plan["installed_revision"]:
        raise RuntimeError("Git installation changed after preview; rerun before applying")
    for relative in plan["incoming_new_paths"]:
        if safe_path(source, relative).exists():
            raise RuntimeError(f"Upstream addition now collides with a local file: {relative}")
    reference = "refs/skill-maintenance/stat-journal-writing/" + uuid.uuid4().hex
    try:
        output(source, "fetch", "--quiet", "--no-tags", "--no-write-fetch-head", upstream_url,
               latest + ":" + reference)
        output(source, "-c", "core.hooksPath=", "merge", "--ff-only", "--no-overwrite-ignore", reference)
        if output(source, "rev-parse", "HEAD") != latest:
            raise RuntimeError("Installation did not reach the verified upstream commit")
        atomic_state(state_path, state_value)
    finally:
        git(source, "update-ref", "-d", reference, check=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    config_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    parser.add_argument("--state", type=Path, default=config_home / "skill-maintenance" / "stat-journal-writing-installation.json")
    parser.add_argument("--base-revision", help="Trusted upstream commit for an older copied installation")
    parser.add_argument("--upstream-url", help="Explicit upstream URL or local repository for offline tests")
    parser.add_argument("--apply", action="store_true", help="Apply the preview; otherwise make no installation changes")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        parser.error("--repository must be OWNER/REPOSITORY")
    source, state_path = args.source.resolve(), args.state.resolve()
    if not (source / "SKILL.md").is_file():
        parser.error("--source must be an existing installed skill containing SKILL.md")
    if state_path.is_relative_to(source):
        parser.error("--state must be outside the installed skill")
    state = read_state(state_path, source, args.repository)
    is_git = independent_git_root(source)
    if is_git and args.base_revision:
        parser.error("--base-revision is only for copied installations")
    upstream_url = args.upstream_url or f"https://github.com/{args.repository}.git"
    with tempfile.TemporaryDirectory(prefix="stat-journal-writing-update-") as temporary:
        upstream = Path(temporary) / "upstream"
        git(None, "clone", "--quiet", "--no-tags", "--", upstream_url, str(upstream))
        latest = output(upstream, "rev-parse", "HEAD")
        branch = output(upstream, "symbolic-ref", "--short", "refs/remotes/origin/HEAD").removeprefix("origin/")
        report = validate(upstream, require_complete=True)
        if not report["ok"]:
            raise RuntimeError("Upstream failed resource validation: " + "; ".join(report["errors"]))
        original = snapshot(source)
        if is_git:
            plan = git_plan(source, upstream, latest)
            incoming = snapshot(upstream)
        else:
            plan, incoming = copied_plan(source, upstream, latest, state, args.base_revision)
            if not plan["blockers"]:
                validate_candidate(source, upstream, plan, Path(temporary) / "candidate")
        result = {"source": str(source), "repository_full_name": args.repository,
                  "installation_type": "git" if is_git else "copied",
                  "mode": "apply" if args.apply else "preview", "state": str(state_path),
                  "upstream_revision": latest, "default_branch": branch, **plan,
                  "can_apply": not plan["blockers"], "applied": False}
        if args.apply and not plan["blockers"]:
            new_state = {"schema_version": 1, "source": str(source),
                         "installed_revision": latest, "repository_full_name": args.repository,
                         "managed_files": incoming, "hash_normalization": "crlf-to-lf"}
            if is_git:
                apply_git(source, upstream_url, latest, plan, state_path, new_state)
            else:
                apply_copy(source, upstream, plan, original, state_path, new_state)
            result["applied"] = True
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["can_apply"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
