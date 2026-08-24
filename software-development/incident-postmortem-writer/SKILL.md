---
name: incident-postmortem-writer
description: "Write blameless postmortems with timelines and action items."
---

# Incident-Postmortem-Writer

Write blameless postmortems with timelines and action items..

## When to Use

After any incident worth remembering, ideally within 48 hours while context is fresh.

## Workflow

1. Freeze the timeline from evidence: alerts, deploys, metric changes, chat timestamps (UTC).
2. Build causal chain with contributing factors — ask 'why' until you hit process, not people.
3. Separate detection/response/recovery durations; find the biggest lever.
4. Action items: each has owner, ticket, due date; classify detect/prevent/mitigate.
5. Blameless language pass: replace names with roles; verify systemic framing.

## Pitfalls

Action items like 'be more careful'. Stopping the why-chain at human error. Timelines reconstructed from memory instead of logs. Postmortems that die in a drive folder.

## Verification

Every action item has a tracking ticket; the review meeting produced edits, not just applause; next incident references this document.

## Inputs

- Task context: incident timeline data, metrics, alert logs

## Outputs

- published postmortem + tracked action items

## Related

runbook-author, observability-checklist
