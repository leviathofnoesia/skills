---
name: chaos-drill-lite
description: "Run small controlled failure drills against your own service."
---

# Chaos-Drill-Lite

Run small controlled failure drills against your own service..

## When to Use

You claim resilience (retries, fallbacks, timeouts) but have never watched it fail for real.

## Workflow

1. Pick ONE hypothesis: 'if dependency X times out, requests fail gracefully within budget'.
2. Design the smallest injection: local proxy delay, kill one replica, fill a disk partition in staging.
3. Define blast radius + abort trigger BEFORE injecting; notify on-call even if it's you.
4. Run in staging first; capture metrics + logs during failure.
5. File findings: what held, what didn't, what surprise appeared.

## Pitfalls

Injecting into prod on day one. No abort switch. Running during peak traffic. Testing only the happy degradation path you built, not adjacent failures (retry storms, cache stampede).

## Verification

Drill report exists with timeline, metrics, and at least one concrete hardening action filed (ticket, not vibes).

## Inputs

- Task context: staging environment, ability to inject latency/faults

## Outputs

- drill report + prioritized resilience backlog items

## Related

backup-restore-drill, observability-checklist
