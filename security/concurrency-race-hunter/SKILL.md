---
name: concurrency-race-hunter
description: "Reproduce and fix races via invariants plus forced interleavings."
---

# Concurrency-Race-Hunter

Reproduce and fix races via invariants plus forced interleavings..

## When to Use

Intermittent failures that vanish under debugging; state corruption without obvious cause.

## Workflow

1. Map shared mutable state: every resource touched by multiple threads/processes/requests.
2. For each, find the invariant that must hold; write an assertion checking it continuously.
3. Stress the suspect paths: interleaving-forcing tests (delays at suspicious points, thread-count ramps, randomized ordering).
4. Analyze with race detectors (TSan/RaceDetector/go test -race) under load, not idle.
5. Fix with the simplest correct primitive (often a queue or single-writer, not clever locking).

## Pitfalls

Testing concurrency single-threaded then declaring victory. Fixes that narrow the race window instead of eliminating it (works until load). Debugging with prints that serialize execution and hide the bug. Locking everything (deadlock/perf death).

## Verification

Race detector clean under stress for sustained runs; invariant assertions never fire in CI soak; production incident rate for that class drops to zero.

## Inputs

- Task context: suspect code paths, load generation ability

## Outputs

- reproduced-and-fixed races + soak-test guards

## Related

flaky-test-triage, chaos-drill-lite
