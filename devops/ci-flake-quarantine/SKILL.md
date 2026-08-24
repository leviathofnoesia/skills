---
name: ci-flake-quarantine
description: "Quarantine flaky CI jobs without losing signal."
---

# Ci-Flake-Quarantine

Quarantine flaky CI jobs without losing signal..

## When to Use

Flaky tests erode trust in CI until red builds get merged blindly.

## Workflow

1. Detect flake empirically: rerun failed tests N times on green code; record failure rates per test.
2. Quarantine confirmed flaky tests into a separate suite/job that still RUNS but doesn't block.
3. File quarantine tickets automatically: test name, failure rate, evidence link, owner assignment.
4. Enforce quarantine hygiene: max dwell time (two weeks), then fix-or-delete decision meeting.
5. Track the trend: quarantine population shrinking means discipline works.

## Pitfalls

Quarantine as permanent exile (tests never return). Fixing flakes by adding sleep/retry (hides the race). Losing coverage silently as quarantine grows. Blame-laden tickets nobody claims.

## Verification

Main suite stays green AND quarantine population trends down; no test lives in quarantine past dwell limit without a decision record.

## Inputs

- Task context: CI history access, test suite

## Outputs

- quarantine pipeline + auto-tickets + dwell enforcement

## Related

flaky-test-triage, perf-budget-guardian
