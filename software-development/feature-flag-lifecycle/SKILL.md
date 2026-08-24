---
name: feature-flag-lifecycle
description: "Manage feature flags: naming, expiry, cleanup, kill switches."
---

# Feature-Flag-Lifecycle

Manage feature flags: naming, expiry, cleanup, kill switches..

## When to Use

Flags multiply faster than they die, or a flag flip caused an incident and nobody remembers who owns it.

## Workflow

1. Inventory flags with owner, purpose, created-date, type (release/experiment/ops/permission).
2. Enforce naming + creation template requiring expiry intent.
3. Automate stale-flag reports (>90 days, low traffic share).
4. Define kill-switch drill: flip critical flags in staging monthly.
5. Remove expired flags via the dead-code sweep loop.

## Pitfalls

Boolean creep (flag states beyond true/false). Flags nested in flags creating untested combinations. Cleanup blocked by fear because no one knows what a flag guards.

## Verification

Flag inventory is queryable and current; scheduled job reports staleness; removing an old flag's code path is routine, not archaeology.

## Inputs

- Task context: flag system access (or config files), traffic data optional

## Outputs

- flag registry + staleness report automation + cleanup PRs

## Related

dead-code-sweep, deploy-freeze-discipline
