---
name: observability-checklist
description: "Audit a service for metrics, logs, traces before it ships."
---

# Observability-Checklist

Audit a service for metrics, logs, traces before it ships..

## When to Use

Pre-launch review of a service, or after an incident where 'we couldn't see it happening'.

## Workflow

1. Walk the golden signals per endpoint: latency, traffic, errors, saturation.
2. For each: can I see it? Is there a dashboard? Does an alert fire at actionable threshold?
3. Trace one real request end-to-end; verify trace continuity across services.
4. Check log hygiene: correlation IDs present, secrets absent, levels meaningful.
5. Prove alerts route to a human and the runbook link resolves.

## Pitfalls

Dashboards nobody opens. Alerting on symptoms of symptoms (CPU instead of SLO burn). Logs missing request IDs so cross-service stories can't be stitched.

## Verification

A simulated failure triggers the expected alert within threshold; the runbook linked from the alert actually resolves the scenario.

## Inputs

- Task context: service endpoints, dashboards, alert configs

## Outputs

- gap list with severity + wired-up fixes for the top gaps

## Related

health-endpoint-design, incident-postmortem-writer
