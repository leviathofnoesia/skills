---
name: artifact-lineage
description: "Record which files/artifacts produced which outputs and why."
---

# Artifact-Lineage

Record which files/artifacts produced which outputs and why..

## When to Use

Workflows produce many artifacts (reports, datasets, builds) whose relationships become unknowable.

## Workflow

1. At creation time, record: which inputs (files/data/versions) produced this, with hashes or paths.
2. Note transformations applied and why (tool versions matter).
3. Store lineage metadata WITH the artifact (sidecar file, header comment).
4. On consumption, verify lineage intact (hash match) before trusting stale artifacts.
5. Prune orphaned artifacts whose lineage shows nothing depends on them.

## Pitfalls

Lineage recorded after-the-fact from memory (wrong). Hashing unstable inputs (timestamps). Lineage so verbose nobody maintains it.

## Verification

Given any artifact, its origin chain reconstructs without asking a human; stale artifacts fail verification loudly.

## Inputs

- Task context: artifact-producing workflow

## Outputs

- lineage sidecars + prune list + verification hooks

## Related

progress-heartbeat, csv-hygiene
