#!/usr/bin/env python3
"""Regression check for skills CLI frontmatter discovery."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    result = subprocess.run(
        ["npx", "--yes", "skills", "add", str(ROOT), "--list"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout + result.stderr

    if result.returncode != 0:
        print("skills discovery failed:", file=sys.stderr)
        print(output, file=sys.stderr)
        return result.returncode or 1

    found = re.search(r"Found (\d+) skills", output)
    required = [
        "Render a text prompt as a compact monospace PNG image",
        "Compress a text prompt with gzip and encode it as a sequence",
        "Differentiator:",
    ]
    missing = []
    if not found or int(found.group(1)) < 16:
        missing.append("Found at least 16 skills")
    missing.extend(needle for needle in required if needle not in output)
    missing.extend(
        skill
        for skill in ("prompt2image", "prompt2qr")
        if not re.search(rf"│\s+{re.escape(skill)}\s*$", output, re.MULTILINE)
    )
    if missing:
        print("skills discovery output is missing:", file=sys.stderr)
        for needle in missing:
            print(f"  {needle}", file=sys.stderr)
        print(output, file=sys.stderr)
        return 1

    print("PASS: prompt2image and prompt2qr have parseable discoverable frontmatter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
