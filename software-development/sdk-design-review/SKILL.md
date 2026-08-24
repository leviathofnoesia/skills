---
name: sdk-design-review
description: "Review a public SDK/API surface for ergonomics and stability."
---

# Sdk-Design-Review

Review a public SDK/API surface for ergonomics and stability..

## When to Use

Publishing a library/SDK others build on, or reviewing a major version bump.

## Workflow

1. Review naming: verbs/nouns consistent? Errors typed? No surprises vs platform idioms?
2. Check surface stability: what's marked public that shouldn't be; what's needed but internal?
3. Assess ergonomics on 3 real tasks: hello-world, common flow, error recovery.
4. Verify docs examples compile against the actual API (executable snippets).
5. Write compatibility promise: semver policy + deprecation mechanics.

## Pitfalls

Public exposure of internals 'temporarily'. Callback hell where promises/futures fit. Docs written for version N-1. Time-zone/locale-naive APIs.

## Verification

All doc snippets execute in CI; a beta user completes the three tasks without asking questions; breaking-change diff is empty.

## Inputs

- Task context: SDK source, docs, sample tasks

## Outputs

- review report with blocking issues + ergonomics fixes

## Related

api-versioning-strategy, api-doc-sketcher
