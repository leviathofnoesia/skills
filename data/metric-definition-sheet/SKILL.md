---
name: metric-definition-sheet
description: "One canonical definition per metric with formula and owner."
---

# Metric-Definition-Sheet

One canonical definition per metric with formula and owner..

## When to Use

Meetings where 'active user' means three different things and every dashboard disagrees.

## Workflow

1. Inventory metrics in circulation across dashboards, docs, meetings.
2. For each contested metric, write the canonical sheet: exact formula (in SQL where possible), inclusion/exclusion rules, timezone, owner.
3. Adjudicate conflicts explicitly — pick ONE definition per concept, document rejected alternatives.
4. Propagate: fix queries, annotate dashboards with definition links.
5. Version definitions; changes require review since trend lines break silently otherwise.

## Pitfalls

Definitions by committee producing mush. Timezone ambiguity (daily active per WHICH midnight?). Silent definition changes making month-over-month comparisons fiction. Ownerless sheets nobody can amend.

## Verification

Two engineers independently implementing the formula from the sheet produce identical numbers; dashboards link their definitions.

## Inputs

- Task context: existing queries/dashboards, stakeholder interviews

## Outputs

- canonical definition sheets + aligned queries

## Related

dashboard-critique, event-schema-versioning
