---
name: database-index-tuner
description: "Rank and tune indexes by measured impact minus write tax."
---

# Database-Index-Tuner

Rank and tune indexes by measured impact minus write tax..

## When to Use

Queries slow down as data grows; EXPLAIN plans show scans where indexes should be.

## Workflow

1. Capture slow query log baseline; rank by total impact (frequency × cost), not single worst.
2. For top offenders: read EXPLAIN ANALYZE, identify seq scans on selective predicates, join key mismatches.
3. Propose minimal index set — every index taxes writes; measure the tradeoff on representative write load.
4. Apply one at a time; re-measure the specific query AND write latency.
5. Audit quarterly for unused indexes (they're pure write tax) via usage stats.

## Pitfalls

Indexing every WHERE column blindly (composite order matters, selectivity matters more). Indexes that the planner ignores due to type casts or functions on columns. Adding indexes during peak traffic (lock contention). Never removing dead indexes.

## Verification

Target queries measurably faster in production-shaped data; write latency regression within tolerance; unused-index report shrinks over quarters.

## Inputs

- Task context: slow query log, schema access, production-scale copy for testing

## Outputs

- applied index changes + before/after evidence

## Related

perf-budget-guardian, load-test-from-logs
