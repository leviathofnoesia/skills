---
name: reproducibility-audit
description: "Check whether published results can be reproduced from artifacts."
---

# Reproducibility-Audit

Check whether published results can be reproduced from artifacts..

## When to Use

Relying on published results (papers, benchmarks, internal studies) before building on them.

## Workflow

1. Check artifact availability: code, data, environment specs published?
2. Verify statistical claims against reported data where possible (recompute key numbers).
3. Assess method reporting: could a competent stranger repeat this? Missing details flagged.
4. Note red flags: no variance reported, selective metric display, post-hoc subgroup emphasis.
5. Grade reproducibility: reproduced / partially / failed / unauditable.

## Pitfalls

Confusing peer review with reproducibility (they're different gates). Recomputing only the summary stats that match. Treating 'code available' as 'code runs'.

## Verification

At minimum, headline statistics recomputed from shared data; audit trail shows exactly what was checked versus taken on faith.

## Inputs

- Task context: target paper/study, shared artifacts

## Outputs

- reproducibility grade + specific verification log

## Related

claim-decay-checker, dataset-provenance
