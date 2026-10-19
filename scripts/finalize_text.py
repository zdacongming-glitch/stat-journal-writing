"""Inspect and conservatively clean a separate prose copy using watermarks-remover."""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def protected_tokens(text):
    pattern = re.compile(
        r"```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)"
        r"|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]"
        r"|\\(?:begin|end|cite\w*|ref|eqref|label)\*?(?:\[[^\]]*\])*\{[^}]*\}"
        r"|https?://[^\s<>]+|\b\d+(?:\.\d+)?(?:e[-+]?\d+)?\b")
    return pattern.findall(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    default_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    parser.add_argument("--watermarks-skill", type=Path, default=default_home / "skills" / "watermarks-remover")
    args = parser.parse_args()
    source, target = args.input.resolve(), args.output.resolve()
    if source.suffix.lower() not in {".txt", ".md", ".tex"}:
        parser.error("Only TXT, Markdown and LaTeX prose files are supported")
    if source == target or target.exists():
        parser.error("Output must be a new separate file")
    wrapper = args.watermarks_skill / "scripts" / "watermarks.py"
    if not wrapper.is_file():
        parser.error("watermarks-remover is not installed; do not claim the CLI cleanup ran")
    before = source.read_text(encoding="utf-8-sig")
    inspected = subprocess.run([sys.executable, "-X", "utf8", str(wrapper), "inspect", str(source)], capture_output=True, text=True, encoding="utf-8")
    if inspected.returncode not in {0, 1}:
        print(inspected.stdout + inspected.stderr)
        raise SystemExit(inspected.returncode)
    cleaned = subprocess.run([sys.executable, "-X", "utf8", str(wrapper), "clean", str(source), "--mode", "unicode", "-o", str(target)], capture_output=True, text=True, encoding="utf-8")
    if cleaned.returncode != 0:
        print(cleaned.stdout + cleaned.stderr)
        raise SystemExit(cleaned.returncode)
    if not target.is_file():
        raise RuntimeError("Cleaner did not produce the requested output file")
    after = target.read_text(encoding="utf-8-sig")
    if protected_tokens(before) != protected_tokens(after):
        print(json.dumps({"ok": False, "output": str(target), "reason": "Protected text differs; retain original and review the separate output."}))
        raise SystemExit(2)
    print(json.dumps({"ok": True, "input": str(source), "output": str(target),
                      "changed": before != after, "protected_tokens_equal": True,
                      "scope": "Conservative Unicode cleanup; prose and technical meaning require assistant review."}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
