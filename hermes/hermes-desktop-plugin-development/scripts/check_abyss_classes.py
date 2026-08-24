#!/usr/bin/env python3
"""Verify every Tailwind-ish class token used in plugin.js exists in the host's
compiled CSS bundle. Uses the scan-tailwind-classes.js output (list of selectors
with counts) and the plugin's className strings.

Usage:
    python check_abyss_classes.py <css_scan_output.txt> <plugin_class_tokens.txt>
"""
import re
import sys


def main():
    css_scan = sys.argv[1]
    plugin_tokens = sys.argv[2]

    compiled = set()
    with open(css_scan, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = re.match(r"^\s*\d+\s+(.+)$", line)
            if m:
                sel = m.group(1).strip()
                # selector may be like .class or .class\:variant or .class\.5
                # normalize the tailwind escape backslashes away for matching
                norm = sel.lstrip(".").replace("\\", "")
                compiled.add(norm)

    tokens = set()
    with open(plugin_tokens, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                tokens.add(line)

    skip_prefixes = ("abyss-",)  # plugin-injected via CONSOLE_CSS
    missing = []
    for t in sorted(tokens):
        if t.startswith(skip_prefixes):
            continue
        # exact-boundary match: compiled set may contain suffix pieces e.g.
        # 'bg-(--ui-bg-tertiary)' — check full token, then variants where the
        # token's pseudo suffix got separately compiled (hover:, focus: etc.)
        # We already accept the plugin's token verbatim; compiled selectors
        # keep the colon escapes removed, so exact equality is the right check
        # for most utilities. For combos like 'hover:bg-(--ui-bg-tertiary)'
        # the compiled entry will be 'hover:bg-(--ui-bg-tertiary)' too.
        if t in compiled:
            continue
        # allow known false positives that are SDK component classes / data
        missing.append(t)

    print(f"plugin tokens: {len(tokens)}")
    print(f"compiled selectors: {len(compiled)}")
    if missing:
        print("MISSING (not found in compiled CSS):")
        for m in missing:
            print("  -", m)
    else:
        print("0 dead utilities")


if __name__ == "__main__":
    main()