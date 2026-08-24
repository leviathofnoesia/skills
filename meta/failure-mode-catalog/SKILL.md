---
name: failure-mode-catalog
description: "Enumerate how this task can fail before starting it."
---

# Failure-Mode-Catalog

Enumerate how this task can fail before starting it..

## When to Use

Before building anything with failure states: integrations, migrations, autonomous flows.

## Workflow

1. Enumerate failure axes per component: input bad, dependency down, timeout, partial completion, repeated delivery.
2. For each: how would we KNOW (detection), what's user impact, what's automatic vs manual response.
3. Mark unhandled modes explicitly as accepted-risk (with owner) or must-fix.
4. Design tests for the top modes; wire alerts for silent ones.
5. Keep the catalog next to the code it describes.

## Pitfalls

Catalogs of obvious failures only (missing the weird ones: clock skew, unicode, double-submit). Writing it post-launch as documentation theater. No owner on accepted risks.

## Verification

Each top mode has either a test proving handling or an alert detecting occurrence; the catalog references real incident IDs over time.

## Inputs

- Task context: design doc or code under consideration

## Outputs

- failure-mode table + tests/alerts for critical modes

## Related

chaos-drill-lite, retry-policy-designer
