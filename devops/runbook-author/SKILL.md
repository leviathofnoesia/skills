---
name: runbook-author
description: "Write runnable runbooks: symptoms, checks, actions, rollback."
---

# Runbook-Author

Write runnable runbooks: symptoms, checks, actions, rollback..

## When to Use

Recurring operational procedures live in one person's head or scattered Slack messages.

## Workflow

1. Pick the procedure; shadow an expert executing it OR execute slowly yourself narrating every check.
2. Structure for 3am use: symptom → diagnostic steps (with expected outputs) → actions → verification → escalation path.
3. Make steps executable: exact commands, not descriptions of commands.
4. Include the abort criteria: when STOP and escalate instead of continuing.
5. Drill it: someone who didn't write it executes against a staged scenario; revise where they stall.

## Pitfalls

Narrative prose instead of executable steps. Missing expected-output descriptions ('run healthcheck' — then what should I SEE?). No abort criteria so people push through failing states. Written once, never drilled.

## Verification

Stranger completes drill using only the document; timestamps show diagnosis-to-resolution under target; revisions folded back within a day.

## Inputs

- Task context: expert execution observation or self-narrated pass

## Outputs

- drilled runbook stored at point-of-need

## Related

checklist-compiler, oncall-transition-kit
