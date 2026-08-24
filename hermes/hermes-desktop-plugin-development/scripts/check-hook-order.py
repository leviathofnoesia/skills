#!/usr/bin/env python3
"""Scan a Hermes desktop plugin.js for React hook-order violations.

React error #310 "Rendered more hooks than during the previous render" fires
when a component declares a hook (useState/useEffect/useMemo/useCallback/
useRef) AFTER an early conditional `return` (e.g. `if (loading) return ...`).
On the loading render the hook is skipped; on the data render it runs — the
hook count changes between renders and React throws. In a Hermes desktop
plugin the symptom is the ENTIRE dashboard page replaced by a generic
"failed to render" + Retry screen (route error boundary), not a view-local
error.

Usage:
    python check-hook-order.py path/to/plugin.js

Exit 0 = clean, 1 = violations found, 2 = bad args.
"""
import re
import sys

HOOK_RE = re.compile(r'^\s*(useState|useEffect|useMemo|useCallback|useRef)\b')


def scan(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    func_re = re.compile(r'^function (\w+)\(')
    violations = []
    i = 0
    while i < len(lines):
        m = func_re.match(lines[i])
        if not m:
            i += 1
            continue
        name = m.group(1)
        depth = 0
        in_body = False
        hook_lines = []
        return_lines = []
        j = i
        while j < len(lines):
            ln = lines[j]
            for ch in ln:
                if ch == '{':
                    depth += 1
                    in_body = True
                elif ch == '}':
                    depth -= 1
                    if depth == 0 and in_body:
                        break
            if not in_body:
                j += 1
                continue
            if depth < 1:
                break
            if HOOK_RE.match(ln):
                hook_lines.append(j + 1)
            if depth == 1 and re.match(r'\s*return\b', ln):
                return_lines.append(j + 1)
            j += 1
        if return_lines and hook_lines:
            first_return = return_lines[0]
            for h in hook_lines:
                if h > first_return:
                    violations.append((name, h, first_return))
        i = j if j > i else i + 1
    return violations


def main(path):
    violations = scan(path)
    if violations:
        for name, hook_line, ret_line in violations:
            print(f'VIOLATION {name}: hook at line {hook_line} after early return at line {ret_line}')
        print(f'{len(violations)} hook-order violation(s) in {path}')
        return 1
    print(f'clean: no hook-after-early-return in {path}')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
