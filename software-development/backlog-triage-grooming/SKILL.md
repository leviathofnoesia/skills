---
name: backlog-triage-grooming
description: "Turn a stale issue backlog into a ranked, actionable queue."
---

# Backlog-Triage-Grooming

Turn a stale issue backlog into a ranked, actionable queue..

## When to Use

The issue tracker has hundreds of stale items nobody trusts as a planning source.

## Workflow

1. Bulk-close by policy first: duplicates, won't-fix-with-reason, >12mo untouched without votes.
2. Tag survivors by area/type; merge near-duplicates with comment trails preserved.
3. Rank top ~20 by value/effort heuristic; everything else stays searchable, not scheduled.
4. For each ranked item: acceptance criteria draft + missing-info questions to reporter.
5. Set recurring cadence (15 min weekly) so it never re-ferments.

## Pitfalls

Grooming as archive archaeology (reading all 400). Closing items reporters still need without explanation. Ranking theater: precise numbers on unknown estimates.

## Verification

Tracker count drops meaningfully; top-20 list drives the next sprint; zero closed items reopened due to bad closure reasons.

## Inputs

- Task context: issue tracker access

## Outputs

- triaged backlog + ranked shortlist + closure comments

## Related

pr-description-forge, decision-record-mini
