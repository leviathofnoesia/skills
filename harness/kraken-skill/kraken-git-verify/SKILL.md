---
name: kraken-git-verify
description: Verify repo, branch, remote before any git write.
---

# kraken-git-verify

Git discipline when working across multiple cloned repositories (e.g. an outer
`hermes-agent` repo and an inner `skills` repo, or any nested checkout). Prevents
the #1 silent-failure class in agent sessions: a command that looks right but
lands on the wrong repo/branch/remote.

## When this skill fires

- A `git checkout`/`git push` created a branch on the wrong remote.
- `git status` in directory X shows files from directory Y.
- A branch you just deleted still shows in `git ls-remote`.
- `npx skills add` discovers N skills but you just wrote a new one and it's not
  in the count.
- Any moment where "did that actually land where I think it did?" arises.

## The rule

**Always confirm the repo → branch → remote → file path chain before acting,
and again after.** Treat any `cwd`/`-C` discrepancy as a hard stop.

## Checklist (run verbatim)

```bash
# 1. Confirm this is the repo you intend to modify.
git rev-parse --show-toplevel     # must be the repo root you expect
git config remote.origin.url      # must be the expected remote

# 2. Confirm the branch.
git branch --show-current

# 3. Confirm local == remote tracking line is sensible.
git status -sb                    # should show the branch name + ahead/behind

# 4. Confirm the remote you will push to.
git remote -v                     # origin fetch/push must match intended remote

# 5. Confirm the file you edited actually lives in THIS repo's tree.
git ls-files --error-unmatch <path>
#   -> if this errors, <path> is NOT tracked in this repo. Stop.

# 6. After any write operation, re-verify.
git diff --stat                   # should be empty after a clean commit/push
git rev-parse HEAD                # must match the commit you think you made
```

## The pitfall this prevents

A common failure mode: the terminal's cwd defaults to repo A
(`/c/Users/billy/AppData/Local/hermes/hermes-agent`), but you intend to work in
repo B (`/c/Users/billy/skills`). Git commands then operate against repo A
while `write_file` (absolute paths) silently writes to repo B's files.
Result: `git status` looks clean, the commit lands on the wrong project, the
branch appears in the wrong GitHub org, and a `npx skills` re-install discovers
stale state because repo B's tree was never the target of the git op.

Worse: `--cwd`-style path flags can resolve differently than absolute
`write_file`/read paths, so even "I pointed at the right dir" is untrustworthy
unless you verify with `git rev-parse --show-toplevel` *after* the cd.

## How to disambiguate (ordered, most reliable first)

1. **Explicit `cd` at the start of every command chain.** A leading `cd /path/to/repo`
   resolves consistently in bash. Do **not** rely on `cwd`/`-C` params for git —
   they diverge between the terminal harness and direct file tools.
2. **`git rev-parse --show-toplevel`** immediately after the cd — confirms the
   canonical path git resolved.
3. **`git config remote.origin.url`** — confirms which remote "origin" maps to
   in the resolved repo (the outer hermes-agent repo's origin is
   `NousResearch/hermes-agent.git`; the skills repo's origin is
   `github.com/leviathofnoesia/skills.git`). These differ; a mismatch means
   you're in the wrong repo.
4. **`git ls-files --error-unmatch <file>`** — confirms a file lives in this
   repo's index. (If a `read_file`/`write_file`/terminal command referenced a
   file that `git ls-files` cannot find, the file is outside git's view and the
   commit will not include it.)
5. **Local == remote SHA after a push:** compare
   `git rev-parse <branch>` with `git rev-parse origin/<branch>`. Diverging SHAs
   mean the push did not land where you think, or an extra commit is ahead.

## Merge-status discipline (before deleting branches)

Before pruning a branch, check merge status against the branch it should fold
into:

```bash
git checkout <target>          # e.g. main
git merge-base --is-ancestor <branch> <target> && echo "SAFE: fully merged" \
  || echo "CHECK: not an ancestor — verify PR status"
```

If an ancestor check is inconclusive (e.g., a PR was merged by a merge commit
rather than a fast-forward), confirm by:

```bash
git log --oneline --all | grep -i "<branch-keywords>\|#N"
# If the PR's merge commit (with (#N) in message) appears in <target>'s history,
# the branch is merged even if its tip is not an ancestor.
```

Only delete when confirmed. Use `-D` (force) only after confirming the
underlying commits survive elsewhere (e.g., via a merged PR reference).

## See also

- `kraken-engineer` — the PDSA process this git discipline serves.
- `references/repo-ambiguity-cheatsheet.md` — quick one-page reminder of the
  disambiguation commands above.
