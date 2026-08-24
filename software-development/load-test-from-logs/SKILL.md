---
name: load-test-from-logs
description: "Build realistic load profiles by replaying production traffic shapes."
---

# Load-Test-From-Logs

Build realistic load profiles by replaying production traffic shapes..

## When to Use

Load tests fail to find real bottlenecks because synthetic traffic doesn't match production shapes.

## Workflow

1. Extract traffic truth from access logs: endpoint mix, payload size percentiles, think-time distributions, arrival patterns (daily curve).
2. Build scenario profiles per percentile, not average (p50 profile + p95 profile).
3. Replay with data shaped like production (respect PII rules — synthesize, don't copy).
4. Run at 1x then ramp; watch for the knee: where latency departs from linear.
5. Record findings against the perf budgets.

## Pitfalls

Replaying at constant rate when production is bursty. Cache-warmed replays flattering results. Forgetting auth flows so you test only the cheap paths.

## Verification

Scenario config documents its source log query + time window; the discovered knee matches a known resource ceiling (explains itself).

## Inputs

- Task context: access/application logs, load tooling

## Outputs

- production-shaped scenarios + knee analysis vs budget

## Related

perf-budget-guardian, csv-hygiene
