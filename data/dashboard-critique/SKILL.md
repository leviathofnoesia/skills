---
name: dashboard-critique
description: "Review dashboards: question first, chart honesty, load speed."
---

# Dashboard-Critique

Review dashboards: question first, chart honesty, load speed..

## When to Use

Dashboards exist but decisions still happen elsewhere; or load slowly and answer nothing quickly.

## Workflow

1. Identify the questions this dashboard should answer in under 10 seconds each.
2. Review top-left-first: does visual priority match question priority? (Most-used metric buried below fold?)
3. Check chart honesty: truncated axes lying, dual axes implying correlation, pie charts beyond 3 slices.
4. Test load speed and failure states — slow dashboards get abandoned, broken ones breed distrust.
5. Cut ruthlessly: charts answering no current decision are decoration costing load time.

## Pitfalls

Adding charts by request without removing any (accretion death). Vanity metrics displacing actionable ones. Red/yellow/green thresholds set once years ago. Nobody can remember what some widget means.

## Verification

Each remaining chart maps to a named recurring question; load under 3 seconds; a new team member answers the core questions unaided.

## Inputs

- Task context: dashboard access, stakeholder question list

## Outputs

- critique report + pruned/improved dashboard

## Related

metric-definition-sheet, anomaly-context-pack
