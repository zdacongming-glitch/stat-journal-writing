"""Prepare evidence-only contributions locally, then submit an opted-in GitHub PR."""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from check_resources import JOURNALS, validate

REPOSITORY = "zdacongming-glitch/stat-journal-writing"


def run(*args, cwd=None, check=True):
    result = subprocess.run([str(a) for a in args], cwd=cwd, capture_output=True,
                            text=True, encoding="utf-8", errors="replace")
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or f"Command failed: {args[0]}")
    return result


def git(directory, *args, check=True):
    return run("git", "-C", directory, *args, check=check)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.is_file() else {}


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2), flush=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def root_git_revision(source):
    if not (source / ".git").exists():
        return None
    result = git(source, "rev-parse", "--show-toplevel", check=False)
    if result.returncode or Path(result.stdout.strip()).resolve() != source:
        return None
    return git(source, "rev-parse", "HEAD").stdout.strip()


def bound_config(args):
    config = read_json(args.config)
    if config and (Path(config.get("source", "")).resolve() != args.source
                   or config.get("repository_full_name") != args.repository):
        raise RuntimeError("This configuration belongs to a different installation/repository; use a separate --config")
    return config


def selected_files(source, selections):
    files = set()
    for selection in selections:
        relative = PurePosixPath(selection.replace("\\", "/"))
        if relative.is_absolute() or any(p in {".", ".."} or ":" in p for p in relative.parts):
            raise RuntimeError("Contribution paths must be relative and remain inside the skill")
        target = source.joinpath(*relative.parts)
        if not target.exists() or target.is_symlink() or not target.resolve().is_relative_to(source):
            raise RuntimeError(f"Missing or unsafe contribution path: {selection}")
        candidates = list(target.rglob("*")) if target.is_dir() else [target]
        for path in candidates:
            if path.is_symlink() or not path.resolve().is_relative_to(source):
                raise RuntimeError(f"Symbolic links are not contribution resources: {path}")
            if not path.is_file():
                continue
            parts = path.relative_to(source).parts
            topic = (len(parts) >= 6 and parts[:2] == ("references", "journals")
                     and parts[2] in JOURNALS and parts[3] == "topics")
            card = (len(parts) == 5 and parts[:2] == ("references", "journals")
                    and parts[2] in JOURNALS and parts[3] == "papers" and path.suffix == ".md")
            if (not (topic and path.suffix in {".md", ".json"} or card)
                    or any(p.startswith(".") or p == "__pycache__" for p in parts)
                    or ".local." in path.name):
                raise RuntimeError(f"Outside the community resource allowlist: {path.relative_to(source)}")
            files.add(path.relative_to(source).as_posix())
    if not files:
        raise RuntimeError("No contribution files selected")
    return sorted(files)


def baseline(args, config):
    if args.base_revision:
        return args.base_revision
    revision = root_git_revision(args.source)
    if revision:
        return revision
    installed = read_json(args.installation_state)
    if (installed.get("installed_revision") and Path(installed.get("source", "")).resolve() == args.source
            and installed.get("repository_full_name") == args.repository):
        return installed["installed_revision"]
    return config.get("base_revision")


def blob(repository, revision, relative):
    result = subprocess.run(["git", "-C", str(repository), "show", f"{revision}:{relative}"],
                            capture_output=True)
    if result.returncode:
        if git(repository, "cat-file", "-e", f"{revision}:{relative}", check=False).returncode:
            return None
        raise RuntimeError("Cannot read baseline resource")
    return result.stdout.replace(b"\r\n", b"\n")


def merge_bytes(current, base, local, folder):
    for name, data in (("current", current), ("base", base), ("local", local)):
        (folder / name).write_bytes(data)
    result = subprocess.run(["git", "merge-file", "-p", str(folder / "current"),
                             str(folder / "base"), str(folder / "local")], capture_output=True)
    if result.returncode:
        return None
    return result.stdout


def prepare(args, config):
    resources = selected_files(args.source, args.path)
    base = baseline(args, config)
    upstream = args.upstream_url or f"https://github.com/{args.repository}.git"
    with tempfile.TemporaryDirectory(prefix="stat-writing-pr-") as temporary:
        temporary = Path(temporary)
        repository = temporary / "repo"
        run("git", "clone", "--quiet", "--", upstream, repository)
        latest = git(repository, "rev-parse", "HEAD").stdout.strip()
        target_branch = git(repository, "symbolic-ref", "--short", "HEAD").stdout.strip()
        if base:
            if (not re.fullmatch(r"[0-9a-fA-F]{7,40}", base)
                    or git(repository, "cat-file", "-e", f"{base}^{{commit}}", check=False).returncode
                    or git(repository, "merge-base", "--is-ancestor", base, latest, check=False).returncode):
                raise RuntimeError("Baseline must be an existing commit in the official default branch history")
            base = git(repository, "rev-parse", base).stdout.strip()
        changed, conflicts = [], []
        for relative in resources:
            # Git objects use LF while Windows checkouts may use CRLF. Compare
            # these text resources using LF so line endings do not create conflicts.
            local = (args.source / relative).read_bytes().replace(b"\r\n", b"\n")
            target = repository / relative
            if target.is_symlink() or not target.resolve().is_relative_to(repository.resolve()):
                raise RuntimeError(f"Unsafe upstream path: {relative}")
            current = target.read_bytes().replace(b"\r\n", b"\n") if target.is_file() else None
            original = blob(repository, base, relative) if base else None
            if local == current or base and local == original:
                continue
            if current == original:
                merged = local
            elif current is None and original is None:
                merged = local
            elif base and current is not None and original is not None:
                merged = merge_bytes(current, original, local, temporary)
            else:
                merged = None
            if merged is None:
                conflicts.append(relative)
                continue
            if merged != current:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(merged)
                changed.append(relative)
        preview = {"mode": "prepare" if args.apply else "preview", "installed_baseline": base,
                   "upstream_revision": latest, "files": changed, "conflicts": conflicts,
                   "external_writes": False, "deletions": False}
        if conflicts:
            preview["hint"] = "Retain both versions and reconcile. Copied installations need --base-revision for existing-file edits."
            emit(preview)
            raise RuntimeError("Contribution has unresolved baseline/path conflicts; no worktree was exported")
        report = validate(repository, require_complete=True)
        if not report["ok"]:
            emit(report)
            raise RuntimeError("Merged resources failed validation; no contribution was exported")
        if not changed or not args.apply:
            emit(preview)
            return
        identity = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:8]
        branch = "contribute/" + identity
        git(repository, "switch", "-c", branch)
        git(repository, "add", "--", *changed)
        destination = args.config.parent / "stat-journal-writing-contributions" / identity
        if destination.resolve().is_relative_to(args.source) or args.source.is_relative_to(destination.resolve()):
            raise RuntimeError("Contribution worktrees must be outside the installed skill")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            raise RuntimeError("Contribution destination already exists")
        shutil.copytree(repository, destination / "repo")
        manifest = {"schema_version": 1, "source": str(args.source), "repository_full_name": args.repository,
                    "upstream_url": upstream, "base_revision": latest, "installed_baseline": base,
                    "target_branch": target_branch, "branch": branch, "worktree": str(destination / "repo"),
                    "files": {p: digest(destination / "repo" / p) for p in changed}}
        save_json(destination / "manifest.json", manifest)
        config.update(schema_version=1, source=str(args.source), repository_full_name=args.repository,
                      active_manifest=str(destination / "manifest.json"))
        save_json(args.config, config)
        preview.update(worktree=manifest["worktree"], manifest=str(destination / "manifest.json"),
                       branch=branch, review_command=f'git -C "{manifest["worktree"]}" diff --cached')
        emit(preview)


def load_contribution(args, config):
    manifest_path = args.manifest or Path(config.get("active_manifest", ""))
    if not manifest_path.is_file():
        raise RuntimeError("Run prepare --apply before submitting")
    manifest = read_json(manifest_path)
    if manifest.get("source") != str(args.source) or manifest.get("repository_full_name") != args.repository:
        raise RuntimeError("Contribution manifest belongs to a different source/repository")
    worktree = Path(manifest["worktree"]).resolve()
    if not root_git_revision(worktree):
        raise RuntimeError("Contribution worktree is missing or is not an independent git checkout")
    if git(worktree, "branch", "--show-current").stdout.strip() != manifest["branch"]:
        raise RuntimeError("Contribution branch changed after preparation")
    for relative, expected in manifest["files"].items():
        path = worktree / relative
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(worktree) or digest(path) != expected:
            raise RuntimeError("Prepared files changed; run prepare again and review the new contribution")
    actual = git(worktree, "diff", "--name-only", manifest["base_revision"]).stdout.splitlines()
    if sorted(actual) != sorted(manifest["files"]):
        raise RuntimeError("Worktree diff differs from the prepared file list")
    if git(worktree, "ls-files", "--others", "--exclude-standard").stdout.strip():
        raise RuntimeError("Unexpected untracked files in contribution worktree")
    expected_head = manifest.get("submitted_commit", manifest["base_revision"])
    if git(worktree, "rev-parse", "HEAD").stdout.strip() != expected_head:
        raise RuntimeError("Contribution history changed; prepare a new contribution")
    if manifest.get("submitted_commit"):
        if git(worktree, "status", "--porcelain").stdout.strip():
            raise RuntimeError("The committed contribution has additional local changes")
    else:
        staged = git(worktree, "diff", "--cached", "--name-only").stdout.splitlines()
        if sorted(staged) != sorted(manifest["files"]) or git(worktree, "diff", "--name-only").stdout.strip():
            raise RuntimeError("The index differs from the prepared files; prepare and review again")
    report = validate(worktree, require_complete=True)
    if not report["ok"]:
        emit(report)
        raise RuntimeError("Prepared resources no longer pass validation")
    return manifest_path, manifest, worktree


def submit(args, config):
    manifest_path, manifest, worktree = load_contribution(args, config)
    if not args.body_file.is_file():
        raise RuntimeError("Provide a real --body-file containing the reviewable PR description")
    emit({"mode": "submit" if args.apply else "preview", "repository": args.repository,
          "branch": manifest["branch"], "files": list(manifest["files"]), "title": args.title,
          "body_file": str(args.body_file.resolve()), "enabled": config.get("enabled", False),
          "external_writes": args.apply})
    if not args.apply:
        return
    if not config.get("enabled"):
        raise RuntimeError("The current installer must explicitly enable public contributions first")
    if manifest.get("upstream_url") != f"https://github.com/{args.repository}.git":
        raise RuntimeError("Test/custom upstream URLs cannot be submitted automatically")
    login = run("gh", "api", "user", "--jq", ".login").stdout.strip()
    if not re.fullmatch(r"[A-Za-z0-9-]+", login):
        raise RuntimeError("Cannot identify the authenticated GitHub account")
    if not manifest.get("submitted_commit"):
        # Resolve identity before any remote mutation, so missing Git config fails locally.
        git(worktree, "var", "GIT_AUTHOR_IDENT")
        git(worktree, "var", "GIT_COMMITTER_IDENT")
        git(worktree, "commit", "-m", args.title)
        manifest["submitted_commit"] = git(worktree, "rev-parse", "HEAD").stdout.strip()
        save_json(manifest_path, manifest)
    owner, name = args.repository.split("/")
    fork = f"{login}/{name}"
    if login.lower() == owner.lower():
        fork = args.repository
    else:
        result = run("gh", "repo", "view", fork, "--json", "nameWithOwner,parent", check=False)
        if result.returncode:
            run("gh", "repo", "fork", args.repository, "--clone=false", "--remote=false")
            result = run("gh", "repo", "view", fork, "--json", "nameWithOwner,parent")
        info = json.loads(result.stdout)
        parent_info = info.get("parent") or {}
        parent = f"{(parent_info.get('owner') or {}).get('login', '')}/{parent_info.get('name', '')}"
        if parent.lower() != args.repository.lower():
            raise RuntimeError("The existing personal repository is not a fork of the configured upstream")
    fork_url = f"https://github.com/{fork}.git"
    reference = f"refs/heads/{manifest['branch']}"
    remote = git(worktree, "ls-remote", fork_url, reference).stdout.strip()
    if remote and remote.split()[0] != manifest["submitted_commit"]:
        raise RuntimeError("Remote contribution branch has changed; preserve it and reconcile without force")
    git(worktree, "push", fork_url, f"HEAD:{reference}")
    pushed = git(worktree, "ls-remote", fork_url, reference).stdout.split()[0]
    if pushed != manifest["submitted_commit"]:
        raise RuntimeError("Remote commit did not match after push; inspect before retrying")
    head = f"{login}:{manifest['branch']}"
    # `gh pr list --head` accepts a branch name, unlike create's owner:branch.
    prs = json.loads(run("gh", "pr", "list", "--repo", args.repository,
                         "--head", manifest["branch"], "--author", login,
                         "--state", "all", "--json", "url,state").stdout)
    if prs:
        emit({"pull_request": prs[0]["url"], "state": prs[0]["state"], "created": False})
        return
    url = run("gh", "pr", "create", "--repo", args.repository, "--base", manifest["target_branch"],
              "--head", head, "--title", args.title, "--body-file", args.body_file.resolve()).stdout.strip()
    manifest["pull_request"] = url
    save_json(manifest_path, manifest)
    emit({"pull_request": url, "created": True, "commit": manifest["submitted_commit"]})


def main():
    codex = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    common.add_argument("--repository", default=REPOSITORY)
    common.add_argument("--config", type=Path, default=codex / "skill-maintenance" / "stat-journal-writing-community.json")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    enable_parser = sub.add_parser("enable", parents=[common])
    enable_parser.add_argument("--enable-public-contributions", action="store_true", required=True)
    enable_parser.add_argument("--base-revision")
    sub.add_parser("disable", parents=[common])
    sub.add_parser("status", parents=[common])
    prepare_parser = sub.add_parser("prepare", parents=[common])
    prepare_parser.add_argument("--path", action="append", required=True)
    prepare_parser.add_argument("--base-revision")
    prepare_parser.add_argument("--installation-state", type=Path, default=codex / "skill-maintenance" / "stat-journal-writing-installation.json")
    prepare_parser.add_argument("--upstream-url", help="Read-only local fixture/custom upstream; submission is disabled")
    prepare_parser.add_argument("--apply", action="store_true")
    submit_parser = sub.add_parser("submit", parents=[common])
    submit_parser.add_argument("--manifest", type=Path)
    submit_parser.add_argument("--title", required=True)
    submit_parser.add_argument("--body-file", type=Path, required=True)
    submit_parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    args.source = args.source.resolve()
    args.config = args.config.resolve()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        parser.error("Repository must have OWNER/REPO form")
    if args.config.is_relative_to(args.source):
        parser.error("Personal configuration must be stored outside the shared skill")
    try:
        config = bound_config(args)
        if args.command == "enable":
            config.update(schema_version=1, source=str(args.source), repository_full_name=args.repository,
                          enabled=True, enabled_at=datetime.now(timezone.utc).isoformat(),
                          authorization_scope="Public metadata, original reading notes and reusable topic writing standards; PRs only")
            revision = args.base_revision or root_git_revision(args.source)
            if revision:
                if not re.fullmatch(r"[0-9a-fA-F]{7,40}", revision):
                    raise RuntimeError("Baseline must be a Git commit hash")
                config["base_revision"] = revision
            save_json(args.config, config)
            emit({"enabled": True, "config": str(args.config), "external_writes": False})
        elif args.command == "disable":
            config.update(schema_version=1, source=str(args.source), repository_full_name=args.repository, enabled=False)
            save_json(args.config, config)
            emit({"enabled": False, "config": str(args.config)})
        elif args.command == "status":
            emit({"enabled": config.get("enabled", False), "config": str(args.config),
                  "active_manifest": config.get("active_manifest"), "base_revision": config.get("base_revision")})
        elif args.command == "prepare":
            prepare(args, config)
        elif args.command == "submit":
            submit(args, config)
    except (RuntimeError, OSError, ValueError, KeyError) as exc:
        emit({"ok": False, "error": str(exc)})
        raise SystemExit(1)


if __name__ == "__main__":
    main()
