---
name: oncall-transition-kit
description: "Structured handoffs: open incidents, risks, quiet wins."
---

# Oncall-Transition-Kit

Structured handoffs: open incidents, risks, quiet wins..

## When to Use

Weekly/biweekly oncall handoffs where context evaporates between shifts.

## Workflow

1. Outgoing writes the handoff doc BEFORE the sync call: open incidents with state, lurking risks (flaky alerts, known-fragile components), pending follow-ups from their week.
2. Sync call: 15 minutes, walk the doc, incoming asks questions, outgoing adds answers inline.
3. Incoming acknowledges ownership explicitly per item — silence isn't transfer.
4. Escalation paths verified: who's the backup, when do you wake people up (documented thresholds).
5. Archive handoff docs; patterns across weeks reveal systemic issues worth fixing.

## Pitfalls

Handoffs as ticket-dumps without narrative state. 'Nothing major this week' hiding three near-misses. Escalation thresholds assumed rather than stated. No archive so lessons repeat monthly.

## Verification

Incoming can describe every open incident's current state unaided post-handoff; first page of new shift handled using transferred context successfully.

## Inputs

- Task context: week's incident/commit history

## Outputs

- handoff document + acknowledged transfer + archived pattern log

## Related

runbook-author, incident-postmortem-writer
