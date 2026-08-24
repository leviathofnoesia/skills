---
name: log-retention-tuner
description: "Right-size log retention vs cost vs debugging need."
---

# Log-Retention-Tuner

Right-size log retention vs cost vs debugging need..

## When to Use

Log storage costs climb monthly, or debugging fails because logs vanished too soon.

## Workflow

1. Classify log streams by purpose: debugging (need recent), compliance (mandated retention), analytics (aggregates suffice long-term).
2. Measure per-stream: volume/day, query frequency by age bucket, cost contribution.
3. Right-size per class: hot/warm/cold tiers, aggressive sampling for high-volume-low-value, aggregate-then-drop for analytics.
4. Verify debugging needs: can last month's incidents be re-investigated with retained data?
5. Automate lifecycle policies; review quarterly against actual query patterns.

## Pitfalls

Keeping everything forever because deletion feels risky (it's the cost risk). Sampling debug logs you'll need during the next incident. Compliance minimums discovered after deletion. One policy for all streams.

## Verification

Storage cost curve bends; post-change incident investigation succeeds using retained logs; lifecycle policies documented per stream class.

## Inputs

- Task context: log system access, volume/query metrics

## Outputs

- tiered retention policy + verified cost reduction

## Related

cost-anomaly-hunt, observability-checklist
