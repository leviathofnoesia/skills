#!/usr/bin/env python3
"""Count parens/braces in CODE ONLY (comments and strings excluded) for
plugin.js. Handles // and /* */ comments, ' " ` strings (with basic template
handling good enough for this file). Prints per-region deltas.
"""
import sys


def code_only(src):
    i, n = 0, len(src)
    out = []
    in_line = in_block = False
    in_str = None
    tpl_stack = []
    while i < n:
        c = src[i]
        nxt = src[i + 1] if i + 1 < n else ""
        if in_line:
            if c == "\n":
                in_line = False
                out.append(c)
            i += 1
            continue
        if in_block:
            if c == "*" and nxt == "/":
                in_block = False
                i += 2
                continue
            i += 1
            continue
        if in_str:
            if c == "\\":
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if tpl_stack:
            if c == "\\":
                i += 2
                continue
            if c == "`":
                # may close an inner or outer template
                tpl_stack.pop()
                out.append(c)
                i += 1
                continue
            if c == "$" and nxt == "{":
                tpl_stack.append("${")
                out.append(c)
                i += 1
                continue
            if c == "}" and tpl_stack and tpl_stack[-1] == "${":
                tpl_stack.pop()
                out.append("}")
                i += 1
                continue
            i += 1
            continue
        if c == "/" and nxt == "/":
            in_line = True
            i += 2
            continue
        if c == "/" and nxt == "*":
            in_block = True
            i += 2
            continue
        if c in ('"', "'"):
            in_str = c
            i += 1
            continue
        if c == "`":
            tpl_stack.append("`")
            out.append(c)
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


def main():
    src = open(sys.argv[1], encoding="utf-8").read()
    code = code_only(src)
    opens = code.count("(")
    closes = code.count(")")
    print(f"code-only parens: ( {opens} ) {closes} -> {'BALANCED' if opens == closes else 'UNBALANCED'}")
    bo = code.count("{")
    bc = code.count("}")
    print(f"code-only braces: {{ {bo} }} {bc} -> {'BALANCED' if bo == bc else 'UNBALANCED'}")
    if opens != closes:
        # find first divergence
        depth = 0
        for idx, ch in enumerate(code):
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth < 0:
                    print(f"first negative paren at code-char {idx}, line ~{code[:idx].count(chr(10))+1}")
                    break


if __name__ == "__main__":
    main()