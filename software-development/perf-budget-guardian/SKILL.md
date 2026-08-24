---
name: perf-budget-guardian
description: "Set and enforce performance budgets in CI with regression alerts."
---

# Perf-Budget-Guardian

Set and enforce performance budgets in CI with regression alerts..

## When to Use

User-facing latency or bundle size matters and regressions currently reach production unnoticed.

## Workflow

1. Choose budgets users feel: p95 endpoint latency, bundle KB, cold-start ms.
2. Measure baselines on realistic hardware/data (not your dev laptop myth).
3. Encode budgets in CI: perf test job, bundle-size action, Lighthouse threshold.
4. Fail PRs on budget breach with delta shown; allow explicit overrides with justification.
5. Review budgets quarterly as product reality shifts.

## Pitfalls

Budgeting averages (users live in the tail). Measuring on noisy shared runners without control runs. Budgets so tight normal work always needs override (alert fatigue).

## Verification

Synthetic regression introduced on a branch fails CI with a readable delta; clean main stays green across N runs (stability).

## Inputs

- Task context: perf-sensitive paths, baseline environment access

## Outputs

- CI enforcement jobs + budget doc with baselines and owners

## Related

load-test-from-logs, observability-checklist
