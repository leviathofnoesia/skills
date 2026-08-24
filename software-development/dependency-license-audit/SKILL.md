---
name: dependency-license-audit
description: "Inventory dependency licenses and flag copyleft/commercial risk."
---

# Dependency-License-Audit

Inventory dependency licenses and flag copyleft/commercial risk..

## When to Use

Before open-sourcing a project, onboarding a commercial customer with legal review, or adding a new dependency family.

## Workflow

1. Generate the full transitive dependency tree (not just direct deps).
2. Resolve license per package (SPDX from lockfile/metadata, not README claims).
3. Classify: permissive / weak copyleft / strong copyleft / unknown.
4. Flag conflicts vs distribution model (SaaS vs binary changes obligations).
5. Produce an attribution bundle (NOTICE file) and a policy for future additions.

## Pitfalls

Trusting the dependency's declared license when metadata says otherwise. Forgetting transitive deps carry licenses too. Treating 'unknown' as safe.

## Verification

Every tree node has an SPDX id recorded; unknowns escalated to zero; NOTICE generated builds cleanly into artifacts.

## Inputs

- Task context: lockfiles, distribution model description

## Outputs

- license inventory + risk flags + NOTICE/attribution output

## Related

dep-upgrade-audit, dataset-provenance
