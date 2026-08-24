---
name: health-endpoint-design
description: "Design liveness/readiness endpoints that tell the truth."
---

# Health-Endpoint-Design

Design liveness/readiness endpoints that tell the truth..

## When to Use

Load balancers restart healthy instances or route to broken ones because health checks lie.

## Workflow

1. Distinguish liveness (process should restart) from readiness (should receive traffic now) — separate endpoints.
2. Liveness: cheap, dependency-free, answers 'am I deadlocked/hung?'. Never check dependencies here (cascade restarts).
3. Readiness: check the dependencies that gate real traffic (DB reachable, cache warm); fail = remove from rotation, not kill.
4. Include version/build info for deploy verification.
5. Test failure modes deliberately: break each dependency, verify correct endpoint behavior and LB reaction.

## Pitfalls

One endpoint doing both jobs (restart storms during dependency blips). Liveness checking DB (DB blip kills entire fleet). Readiness passing while actually unable to serve (cache cold but reporting ready).

## Verification

Chaos test: each dependency failure produces expected behavior (no-restart-but-drain for readiness gates, restart only for true deadlock); deploy verification reads build info.

## Inputs

- Task context: service architecture, dependency map

## Outputs

- designed health endpoints + chaos-verified behavior

## Related

observability-checklist, chaos-drill-lite
