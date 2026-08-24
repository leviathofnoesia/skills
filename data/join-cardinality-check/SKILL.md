---
name: join-cardinality-check
description: "Verify expected row counts before/after joins to catch fan-out."
---

# Join-Cardinality-Check

Verify expected row counts before/after joins to catch fan-out..

## When to Use

Aggregations suddenly report doubled revenue or user counts explode after query changes.

## Workflow

1. Before running new joins, predict expected row count from known cardinality (1:1, 1:N, N:M).
2. Run joins wrapped in count comparisons: input rows vs output rows.
3. Fan-out detected? Identify which side multiplied and why (duplicate keys, missing unique constraint, time-range overlap).
4. Fix at the data level (dedupe, constraint) not just the query level (DISTINCT band-aids).
5. Codify expectations as assertion tests for critical reporting queries.

## Pitfalls

DISTINCT hiding fan-out while corrupting legitimate multi-row aggregates. Assuming PK uniqueness that soft-deletes violated. Left joins assumed to preserve left count when join keys duplicate.

## Verification

Critical queries carry cardinality assertions that fail loudly on violation; deliberate fan-out injection trips the alarm.

## Inputs

- Task context: query access, table knowledge

## Outputs

- verified joins + cardinality assertions for critical paths

## Related

metric-definition-sheet, csv-hygiene
