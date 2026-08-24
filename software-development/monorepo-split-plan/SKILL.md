---
name: monorepo-split-plan
description: "Plan extracting a package from a monorepo without breaking CI."
---

# Monorepo-Split-Plan

Plan extracting a package from a monorepo without breaking CI..

## When to Use

A package in a monorepo needs separate release cadence, ownership, or access control.

## Workflow

1. Map the package's true dependency cone (code, CI jobs, shared config).
2. Choose seam: git subtree/filter first (history-preserving), then package-manager extraction.
3. Stand up the new repo's CI as a mirror BEFORE cutover; keep both green.
4. Cut over consumers via the package registry, not path imports.
5. Freeze old paths with deprecation shims for one cycle, then delete.

## Pitfalls

Hidden path-imports and shared scripts that break silently. Losing history by copy-paste extraction. Two CI systems drifting during the transition window.

## Verification

New repo CI runs the same gates pre/post split; consumers resolve from the registry; old path imports fail loudly after the shim window.

## Inputs

- Task context: monorepo layout, consumer inventory

## Outputs

- sequenced split plan + new repo scaffold + shim PRs

## Related

dependency-license-audit, api-versioning-strategy
