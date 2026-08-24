---
name: cost-anomaly-hunt
description: "Trace cloud bill spikes to specific services and causes."
---

# Cost-Anomaly-Hunt

Trace cloud bill spikes to specific services and causes..

## When to Use

Cloud bills jump inexplicably or costs creep upward while traffic doesn't.

## Workflow

1. Isolate the delta: which service/resource line grew, over which window?
2. Correlate with changes: deploys, traffic shifts, config changes, pricing updates in window.
3. Trace unit economics: cost per request/user/transaction now vs before — efficiency regression or volume growth?
4. Hunt common culprits: chatty retries amplifying failures, unbounded logging, forgotten test environments, storage accumulation, egress surprises.
5. Fix root cause; install budget alerts BEFORE the next surprise.

## Pitfalls

Optimizing the biggest bill line when it's actually efficient (chase the DELTA). Reserved-instance math obscuring usage problems. Cutting capability to save pennies. Alerts set after the fire with thresholds nobody tuned.

## Verification

Root cause identified with evidence (not correlation alone); fix verified in next billing cycle; budget alert would have caught this anomaly earlier if retroactively applied.

## Inputs

- Task context: billing exports, deploy/change logs

## Outputs

- root-caused explanation + fix + forward-looking alerts

## Related

capacity-headroom-check, log-retention-tuner
