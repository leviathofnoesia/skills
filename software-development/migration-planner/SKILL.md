---
name: migration-planner
description: "Plan zero-downtime schema migrations with reversible steps."
---

# Migration-Planner

Plan zero-downtime schema migrations with reversible steps..

## When to Use

Schema or infrastructure changes must ship without downtime on live traffic.

## Workflow

1. Write current → target schema and every reader/writer affected.
2. Sequence expand → migrate data (batched, idempotent) → switch readers → contract old paths → remove.
3. For each step define: forward SQL, backward SQL, verification query, abort criteria.
4. Rehearse on production-scale copy; measure lock/duration.
5. Execute with monitoring on error rate + latency at each gate.

## Pitfalls

Long-running locks from naive ALTERs on big tables. Forgetting dual-write windows during backfill. Skipping rehearsal then discovering a 40-minute migration at 2am.

## Verification

Each phase has recorded verification results; rollback path tested on rehearsal copy; cutover completes inside the measured window.

## Inputs

- Task context: schema files, DB access, traffic patterns

## Outputs

- step-by-step migration plan with tested rollback per step

## Related

backfill-planner, backup-restore-drill
