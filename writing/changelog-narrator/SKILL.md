---
name: changelog-narrator
description: "Turn diff sets into user-facing changelog entries."
---

# Changelog-Narrator

Turn diff sets into user-facing changelog entries..

## When to Use

Release notes read like commit logs; users can't tell what changed for THEM.

## Workflow

1. Gather merged PRs/diffs since last release; group by user-visible impact area.
2. Translate each group to outcome language: what users can now do / stop suffering.
3. Order by user impact, not merge time. Lead with the headline change.
4. Include upgrade notes ONLY where behavior actually shifts (breaking, deprecations).
5. Link each entry to PR/docs for those who need depth.

## Pitfalls

'Various bug fixes and improvements' (says nothing). Internal jargon leaking through (refactored the widgetizer). Every commit getting equal billing. Hiding behavior changes among features.

## Verification

A user reading only this changelog correctly predicts what's different in their workflow; support tickets about 'what changed' drop.

## Inputs

- Task context: merged PR range, previous changelog

## Outputs

- user-facing changelog section

## Related

release-note-editor, pr-description-forge
