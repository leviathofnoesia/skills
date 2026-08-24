---
name: context-pruning-pass
description: "Drop stale conversation context before long tasks to save budget."
---

# Context-Pruning-Pass

Drop stale conversation context before long tasks to save budget..

## When to Use

Long agent sessions degrade as irrelevant history accumulates; token costs climb mid-task.

## Workflow

1. Mark the task's active working set: current goal, decisions made, open threads.
2. Classify history: load-bearing (results, decisions), ambient (tool noise), dead (superseded attempts).
3. Summarize dead + ambient into compact state notes; drop originals.
4. Re-verify: can the task proceed correctly with only working set + summaries?
5. Repeat at natural phase boundaries, not mid-surgery.

## Pitfalls

Pruning error messages that explain current weirdness. Summaries losing numbers/paths precision. Pruning during multi-step operations that reference earlier steps.

## Verification

Post-prune, next-step execution succeeds without re-fetching pruned content; token spend drops measurably.

## Inputs

- Task context: session transcript

## Outputs

- compacted session state + prune report

## Related

token-budget-forecast, progress-heartbeat
