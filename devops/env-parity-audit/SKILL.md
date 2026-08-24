---
name: env-parity-audit
description: "Diff dev/staging/prod config and surface drift."
---

# Env-Parity-Audit

Diff dev/staging/prod config and surface drift..

## When to Use

Bugs reproduce only in production; configuration differences accumulate invisibly between dev/staging/prod.

## Workflow

1. Inventory config surfaces: env vars, config files, feature flags, infrastructure parameters, secrets (existence, not values).
2. Diff across environments systematically; classify each difference: intentional (scaled resources) vs accidental (drifted flag) vs forgotten (staging-only hack).
3. For accidental drift: align or explicitly document why different.
4. Encode parity checks: automated diff job reporting new unexplained differences.
5. Establish change protocol: env-specific values declared in one reviewable place.

## Pitfalls

Secrets VALUES diffed and leaked in reports (existence only). 'Temporary' staging hacks living for years. Parity theater: configs match while underlying data volumes/shape differ meaningfully.

## Verification

Every difference classified and documented or aligned; parity job runs on schedule catching new drift within one cycle.

## Inputs

- Task context: environment access for config reads

## Outputs

- parity report + alignment PRs + recurring diff job

## Related

schema-drift-detector, config-change-journal
