---
name: flaky-test-triage
description: "Diagnose flaky tests: isolate ordering, timing, and environment causes."
---

# Flaky Test Triage

Systematic diagnosis of intermittently failing tests. A flaky test is a bug
in the test, the code, or the environment — this skill finds which, with
evidence, instead of rerunning until green.

## When to Use

- A test passes locally but fails CI, fails alone but passes in a suite,
  or fails only sometimes. Use when someone says "flaky", "intermittent",
  "passes on retry", or "green after re-run".
- Differentiator: reproduces first, hypothesizes second. Never shrug a
  failure off as "probably a timeout".

## Workflow

1. **Reproduce deterministically before theorizing.** Run the failing test
   N times in isolation (`--repeat`/loop) and record the pass rate. A test
   that fails 1/10 gives you a cheap experiment loop; one that fails 0/20
   points at environment or ordering.
2. **Bisect the dimensions**, one at a time:
   - *Ordering*: run the full suite vs. the single test. Suite-only failure
     → leaked state (module globals, DB rows, temp files, mocks not reset).
     Try `pytest -p no:randomly` / shuffle seed pinning to confirm.
   - *Timing*: look for sleeps, real network, real clock, timeouts near the
     edge. Replace sleeps with event-based waits; replace wall-clock reads
     with an injected fake clock.
   - *Concurrency*: races between tests sharing ports, files, or fixtures;
     parallel runners (`-n`) hiding or creating collisions.
   - *Environment*: OS, timezone/locale, filesystem case-sensitivity, line
     endings, resource limits. Diff CI logs against local output.
3. **Classify** with evidence from step 2:
   - Test bug (shared state, race in fixture, over-tight assertion).
   - Product bug (real race, unhandled error path) — escalate, do not fix
     in the test.
   - Environment gap (missing service, version skew) — document the
     required environment.
4. **Fix at the root.** Delete the sleep and wait on the real condition.
   Reset the leaked global. Seed the RNG. Quarantine only as a last resort,
   with an issue link in the skip reason.

## Rules

- Never "fix" flakiness by adding retries around an assertion without also
  naming the root cause — retries hide product bugs.
- Every claim cites command + observed output (`path:line`, run counts).
- If you cannot reproduce after exhausting the dimensions above, say so and
  hand back the classification "environment-dependent, unreproduced" with
  everything you ruled out.

## Failure handling

- Cannot run the suite locally → reproduce in CI by re-running the job with
  extra logging; do not guess.
- Flakiness spans many unrelated tests → suspect infrastructure (runner
  resources, shared services) before touching individual tests.
