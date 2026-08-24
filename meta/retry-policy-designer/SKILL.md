---
name: retry-policy-designer
description: "Choose retry/backoff/timeout policies per external dependency."
---

# Retry-Policy-Designer

Choose retry/backoff/timeout policies per external dependency..

## When to Use

Integrations with external dependencies need explicit failure handling instead of default-then-hope.

## Workflow

1. Classify each dependency call: idempotent? latency tolerance? failure visibility?
2. Set policy per class: max retries, backoff curve, jitter, timeout budget total.
3. Define circuit-breaker thresholds: when to stop hammering and degrade.
4. Distinguish retryable (network blip) from fatal (auth rejected) errors explicitly.
5. Document policies in code as configuration, not scattered magic numbers.

## Pitfalls

Retrying non-idempotent operations (double charges). Retry storms amplifying outages. Timeouts longer than user patience. Same policy for every dependency regardless of behavior.

## Verification

Chaos test: dependency returns 500s; system backs off per curve, trips breaker at threshold, recovers cleanly when dependency heals.

## Inputs

- Task context: dependency inventory, SLOs

## Outputs

- per-dependency policy table + implemented configs

## Related

failure-mode-catalog, chaos-drill-lite
