---
name: dead-code-sweep
description: "Find and safely remove dead code with call-graph evidence."
---

# Dead-Code-Sweep

Find and safely remove dead code with call-graph evidence..

## When to Use

Before refactors, after long-lived features are killed, or when coverage reports flag never-executed regions.

## Workflow

1. Build the candidate list: linters (vulture/ts-prune/ruff), coverage zero-hit files, unreferenced exports.
2. For each candidate, prove it is unreachable: search dynamic dispatch (string-keyed registries), reflection, templates, config-referenced entry points.
3. Classify: dead (delete now), dormant (feature-flagged — record owner + expiry), public-API (deprecate first).
4. Delete in small commits with green tests; note each removal in the changelog.

## Pitfalls

Dynamic invocation hides usage (plugins, ORMs, CLI dispatch). Deleting 'unused' exports that are part of a published API contract. Removing code that a migration or rollback path still needs.

## Verification

Full test suite green post-removal; build artifacts shrink or stay equal; grep for deleted symbols returns only changelog/history hits.

## Inputs

- Task context: repo access, coverage data optional

## Outputs

- removal commits + dead-code report listing survivors and why they stay

## Related

refactor-safe-extract, type-boundary-hardening
