---
name: diff-explain
description: "Explain a git diff or PR change as layered summaries for different readers."
---

# Diff Explain

Turn any `git diff`, commit range, or patch into a layered explanation:
one-line what, then why-it-matters, then a per-file walkthrough. Optimized
for the reader who must approve or review a change they did not write.

## When to Use

- "Explain this diff", "what does this PR do", "summarize the changes",
  "review prep" — any time a human needs to understand a change quickly
  before deciding something (approve, merge, revert, test).
- Differentiator: produces decision-ready summaries, not a file-by-file
  recitation. Every layer answers a question a reviewer actually asks.

## The three layers

Produce all three, in order, in your final response:

1. **Headline** (one sentence): what changed and to what end. No file names.
2. **Why it matters**: 2-4 bullets — behavior change, risk, blast radius,
   migration or config impact.
3. **Walkthrough** (optional, on request): per-file table with
   `path | intent | risk` columns. Intent is a verb phrase ("adds retry to
   uploads"), never a restatement of the hunk.

## Workflow

1. Get the diff: `git diff <base>...<head>` for a branch, `git show <sha>`
   for a commit, or read the provided patch. If no range is given, ask or
   default to `git diff @{u}...` (unpushed work).
2. Read hunks in dependency order, not file order: shared types/utilities
   first, call sites second, tests last. This reveals intent.
3. Check test diffs separately from code diffs: a behavior change without a
   corresponding test change is a finding, not trivia — surface it under
   "why it matters".
4. Verify claims against the actual hunks. Never describe code you did not
   read; if a hunk is ambiguous, quote it and say what is unclear.

## Rules

- Cite as `path:line` against the NEW side of the diff.
- Name every public API/CLI/config change explicitly — these are contract
  changes and reviewers must see them even in the headline layers.
- If the diff is huge (>2000 lines), summarize by subsystem and offer the
  walkthrough table per subsystem instead of dumping everything.

## Failure handling

- Empty diff → say so; do not invent content.
- Binary/generated files → note them in one line, skip analysis.
- Merge commits → use `git show <sha> -m --first-parent` or diff the parents
  explicitly; a plain merge-show is often empty and will mislead you.
