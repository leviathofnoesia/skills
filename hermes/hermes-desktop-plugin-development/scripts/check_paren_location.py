#!/usr/bin/env python3
"""Pinpoint the naive paren delta in plugin.js: classify every token with
Python's tokenize (STRING/COMMENT/NL/NAME/OP) and count parens/braces only
in OP tokens. Reports the first OP paren that goes negative.
note: tokenize is Python-syntax-oriented; JS uses many of the same token
classes and this is used only as a heuristic cross-check on top of
node --check (the authoritative gate). Op tokens ('(', ')', '{', '}') are
reliable for both languages.
"""
import io
import tokenize
import sys

path = sys.argv[1]
src = open(path, encoding="utf-8").read()
tokens = list(tokenize.generate_tokens(io.StringIO(src).readline))

depth = 0
neg = None
op_count = {"(": 0, ")": 0}
brace_count = {"{": 0, "}": 0}
for tok in tokens:
    if tok.type == tokenize.OP:
        if tok.string in op_count:
            op_count[tok.string] += 1
            if tok.string == "(":
                depth += 1
            elif tok.string == ")":
                depth -= 1
                if depth < 0 and neg is None:
                    neg = (tok.start[0], tok.start[1])
        if tok.string in brace_count:
            brace_count[tok.string] += 1

print(f"OP parens: ( {op_count['(']} ) {op_count[')']} "
      f"{'BALANCED' if op_count['('] == op_count[')'] else 'UNBALANCED'}")
print(f"OP braces: {{ {brace_count['{']} }} {brace_count['}']} "
      f"{'BALANCED' if brace_count['{'] == brace_count['}'] else 'UNBALANCED'}")
print("first negative paren at:", neg)
# show the line at neg
if neg:
    lines = src.split("\n")
    ln = lines[neg[0] - 1]
    print("line:", ln)
    print("snippet:", ln[max(0, neg[1] - 40): neg[1] + 40])