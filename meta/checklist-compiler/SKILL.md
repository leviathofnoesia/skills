---
name: checklist-compiler
description: "Compile recurring workflows into executable checklists."
---

# Checklist-Compiler

Compile recurring workflows into executable checklists..

## When to Use

A workflow recurs often enough that steps get missed, but rarely enough that full automation isn't justified.

## Workflow

1. Run the workflow once slowly, capturing EVERY step including verification bits usually skipped.
2. Order steps by dependency; mark which are skippable under what conditions.
3. Format as executable checklist: imperative verbs, checkable outcomes, links to commands.
4. Pilot with someone who didn't write it; fix where they stall.
5. Store where the work happens; revisit after each use until stable.

## Pitfalls

Checklists written from memory (missing the tacit steps). Aspirational steps ('verify backups') without instructions. Never updating after reality diverges.

## Verification

A competent stranger completes the workflow using only the checklist; post-run notes fold fixes back in within a day.

## Inputs

- Task context: one observed execution of the workflow

## Outputs

- versioned checklist stored at point-of-use

## Related

runbook-author, progress-heartbeat
