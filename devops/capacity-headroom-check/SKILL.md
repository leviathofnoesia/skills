---
name: capacity-headroom-check
description: "Measure headroom before traffic events; set scaling triggers."
---

# Capacity-Headroom-Check

Measure headroom before traffic events; set scaling triggers..

## When to Use

Before predictable traffic spikes (launches, sales, seasonal) or when scaling feels like guesswork.

## Workflow

1. Identify bottleneck resource per tier: it's rarely CPU (usually DB connections, memory, rate limits, downstream quotas).
2. Measure current utilization at known load; compute headroom ratio per resource.
3. Model the spike: expected multiplier × current baseline, duration shape (cliff vs ramp).
4. Compare against headroom; identify which resource exhausts first and at what multiplier.
5. Act: scale preemptively, set scaling triggers with lead-time awareness (scaling isn't instant), prepare degradation plan.

## Pitfalls

Scaling the comfortable resource (add app servers) while DB connections exhaust first. Assuming autoscaling acts faster than it does (image pulls, warmup). Testing capacity only via synthetic load that doesn't match spike shape.

## Verification

Post-event analysis: predicted exhaustion point matched reality within tolerance; degradation plan executed smoothly if needed.

## Inputs

- Task context: metrics history, event forecast

## Outputs

- headroom report with first-exhaustion prediction + action plan

## Related

load-test-from-logs, cost-anomaly-hunt
