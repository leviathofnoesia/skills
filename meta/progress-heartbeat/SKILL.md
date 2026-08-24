---
name: progress-heartbeat
description: "Emit structured progress notes during long autonomous runs."
---

# Progress-Heartbeat

Emit structured progress notes during long autonomous runs..

## When to Use

Long autonomous runs where stakeholders currently see silence for hours then a wall of output.

## Workflow

1. Define heartbeat cadence by run length: hourly for day-jobs, per-milestone otherwise.
2. Heartbeat format: current step N/M, last completed milestone, next checkpoint ETA, anomalies if any.
3. Emit to wherever humans already look (status channel, log stream).
4. On anomaly: heartbeat immediately with what changed and what you're doing.
5. End-of-run report links all heartbeats for the full story.

## Pitfalls

Heartbeats so noisy they're muted. 'Still working...' content-free pings. Only emitting good news (anomalies are the point).

## Verification

A stakeholder glancing at the channel can answer 'is it healthy, where is it, when done?' without interrupting the run.

## Inputs

- Task context: task plan with milestones

## Outputs

- structured progress stream + final linked summary

## Related

token-budget-forecast, artifact-lineage
