---
name: pr-description-forge
description: "Write PR descriptions reviewers actually need: intent, risk, test."
---

# Pr-Description-Forge

Write PR descriptions reviewers actually need: intent, risk, test..

## When to Use

Opening any PR another human will review, especially risky or wide-reaching changes.

## Workflow

1. State intent in one sentence: what world looks like after merge.
2. Link context: issue, design doc, prior discussion — reviewer shouldn't dig.
3. Risk section: what could this break, how was that tested, blast radius.
4. Test evidence: commands run and their output shape, not 'tested locally'.
5. Reviewer guidance: where to look hard, what's mechanical, suggested review order.

## Pitfalls

Novels nobody reads (lead with the summary instead). Hiding known limitations (state them + follow-up tickets). Screenshots of code instead of text diffs.

## Verification

Reviewers ask questions about design, not 'what is this doing'; time-to-first-review drops; revert instructions derivable from the description.

## Inputs

- Task context: diff, linked issues, test results

## Outputs

- structured PR description

## Related

changelog-narrator, decision-record-mini
