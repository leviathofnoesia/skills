---
name: anomaly-context-pack
description: "Pair each anomaly alert with the context needed to triage it."
---

# Anomaly-Context-Pack

Pair each anomaly alert with the context needed to triage it..

## When to Use

Alerts fire and responders waste the first 20 minutes gathering what should ship with the page.

## Workflow

1. For each alert, define the triage questions a responder will ask: scope (who/what affected), recent changes, comparable history.
2. Pre-compute answers into the notification: affected-entity counts, deploys in window, similar past incidents links.
3. Include the metric's own context: normal range, seasonality expectation, current deviation shape.
4. Link the canonical runbook section for this alert class.
5. Iterate from real pages: what did responders manually look up? Add it next revision.

## Pitfalls

Context packs so dense they're another dashboard. Stale runbook links (checked never). Packs built once from imagination instead of responder interviews. Alert spam making packs unread.

## Verification

Time-to-triage measurably drops after rollout; responders confirm the pack answered their first three questions; zero stale links on audit.

## Inputs

- Task context: alert definitions, incident history

## Outputs

- enriched alerts + measured triage improvement

## Related

runbook-author, observability-checklist
