# Repo-Ambiguity Disambiguation — Quick Reference

When `git` and `write_file`/`read_file` disagree on where files live (common
with nested checkouts like `hermes-agent` containing a `skills` repo, or any
shared-parent directory layout), run this sequence before *any* git write:

```bash
# 0. Explicit cd (do NOT rely on cwd/-C params for git)
cd /c/Users/billy/skills

# 1. Am I in the repo I mean to be?
git rev-parse --show-toplevel          # must be …/skills
git config remote.origin.url           # must be …/leviathofnoesia/skills.git

# 2. Am I on the right branch?
git branch --show-current

# 3. Is the file I just edited actually in THIS repo's index?
git ls-files --error-unmatch <path/to/file.ext>

# 4. After write/push: local == remote?
git rev-parse HEAD
git rev-parse origin/$(git branch --show-current)   # must match
git status -sb                          # should be clean after push
```

## Red flags (stop and disambiguate)

| Symptom | Likely cause |
|---|---|
| `git checkout -b feat/X` created a repo in a different GitHub org | cwd is a nested repo parent; `git` operated on the outer checkout |
| `npx skills add . --list` discovers stale skill count | git op targeted wrong repo; `write_file` wrote to the intended repo |
| `git push` says "everything up-to-date" but the branch is new on remote | you pushed to the wrong origin |
| `git status` clean but files you edited appear missing in `--stat` | `git ls-files` does not find them → they live outside this repo's tree |

## Merge-confirm when ancestor check is inconclusive

```bash
git checkout main
git log --oneline --all | grep -iE "deepsec-luna|#3"
# If PR #3's merge commit appears in main's history → merged, safe to delete
git merge-base --is-ancestor <branch> main && echo merged || echo check-pr
```
