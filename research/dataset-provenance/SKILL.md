---
name: dataset-provenance
description: "Document where data came from and what licenses apply."
---

# Dataset-Provenance

Document where data came from and what licenses apply..

## When to Use

Datasets outlive memory of where they came from; compliance or reproduction looms.

## Workflow

1. Record acquisition: source URL/contact, exact query or scrape config, timestamp, license terms.
2. Document transformations since acquisition as ordered steps with parameters.
3. Note known caveats: collection biases, missing segments, quality issues discovered later.
4. Version the dataset; never mutate in place — derive.
5. Attach provenance sidecar traveling WITH copies of the data.

## Pitfalls

'We downloaded it a while ago' as documentation. Transformations applied interactively and unrecorded. License terms discovered after publication. Sidecars separated from data in transit.

## Verification

A stranger can reconstruct the dataset from provenance metadata alone; license audit passes against recorded terms.

## Inputs

- Task context: dataset files, acquisition history

## Outputs

- provenance sidecar + versioned dataset policy

## Related

artifact-lineage, dependency-license-audit
