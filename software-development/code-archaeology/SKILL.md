---
name: code-archaeology
description: "Reconstruct why legacy code exists using git history and docs."
---

# Code-Archaeology

Reconstruct why legacy code exists using git history and docs..

## When to Use

Inheriting an unfamiliar codebase, debugging 'why is it like this', or before refactoring legacy modules.

## Workflow

1. Anchor on the oldest stable commit; read the earliest README/design docs.
2. git log --follow key files; extract decision commits (messages with 'because/revert/fix/workaround').
3. Map surviving constraints: issue links, mailing lists, ADRs, deleted tests.
4. Distinguish load-bearing weirdness (still protects against a real failure) from fossilized weirdness.
5. Record findings as mini-ADRs so the next person doesn't re-dig.

## Pitfalls

Judging old decisions by today's context. Trusting comments (they rot) over commit messages and linked issues. Rewriting load-bearing weirdness and rediscovering its reason in production.

## Verification

Every 'this is weird' finding has either a cited origin (commit/issue) or an explicit unknown; documented findings survive in the repo.

## Inputs

- Task context: git history access, ticket/issue archive if available

## Outputs

- annotated map of why-the-code-is-this-way + new ADRs

## Related

decision-record-mini, refactor-safe-extract
