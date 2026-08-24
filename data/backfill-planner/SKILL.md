---
name: backfill-planner
description: "Plan safe historical backfills with idempotent batches."
---

# Backfill-Planner

Plan safe historical backfills with idempotent batches..

## When to Use

Historical data needs recalculation/regeneration after logic changes — carelessly done, it corrupts or melts the database.

## Workflow

1. Define scope precisely: which rows, which time range, what defines 'needs update' (predicate, not vibes).
2. Write the backfill as idempotent batches: safe to run twice, resumable after crash.
3. Rehearse on production-scale copy: measure batch duration, lock impact, replication lag.
4. Execute with progress tracking and a kill switch; monitor error rate per batch.
5. Verify post-conditions: predicate returns zero rows; spot-check known-tricky records.

## Pitfalls

Single-transaction monsters locking everything for hours. Non-idempotent updates compounding on retry. Forgetting downstream caches/materialized views now stale. Running during peak traffic because 'it's just SELECTs' (it isn't).

## Verification

Predicate scan confirms zero remaining targets; replica lag stayed within bounds; a killed-and-resumed run produced identical results to a clean run.

## Inputs

- Task context: target predicate, DB access, maintenance windows

## Outputs

- executed backfill + verification report

## Related

migration-planner, null-pandemic-audit
