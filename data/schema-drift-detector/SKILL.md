---
name: schema-drift-detector
description: "Detect silent schema drift between environments or snapshots."
---

# Schema-Drift-Detector

Detect silent schema drift between environments or snapshots..

## When to Use

Environments silently diverge; queries work in dev, fail mysteriously in prod.

## Workflow

1. Snapshot schemas from every environment (tables, columns, types, indexes, constraints, defaults).
2. Normalize for legitimate differences (dev-only test tables) via explicit allowlist.
3. Diff everything else; classify drift direction: env-vs-env, code-migration-vs-reality.
4. For each drift: is it a missing migration, manual hotfix, or abandoned experiment?
5. Output remediation list + install recurring snapshot diffs to catch future drift early.

## Pitfalls

Snapshotting at different times during active deploys (false alarms). Ignoring index/constraint drift because columns match. Allowlists growing forever until they hide real problems.

## Verification

Known intentional differences appear in allowlist; zero unexplained drift remains; next scheduled scan runs clean.

## Inputs

- Task context: environment access for schema reads

## Outputs

- drift report + allowlist + recurring detection job

## Related

env-parity-audit, migration-planner
