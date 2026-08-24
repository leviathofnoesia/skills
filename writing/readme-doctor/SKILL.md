---
name: readme-doctor
description: "Diagnose READMEs: missing promise, install friction, stale bits."
---

# Readme-Doctor

Diagnose READMEs: missing promise, install friction, stale bits..

## When to Use

READMEs that fail their one job: converting a visitor into a user in under two minutes.

## Workflow

1. Test the promise: does the first screen say WHAT this is and WHY it exists?
2. Run the install cold: copy commands verbatim into a clean environment; note every failure.
3. Check the quickstart: does it produce a working result fast? Time it.
4. Audit honesty: badges real? Screenshots match current version? Links resolve?
5. Verify maintenance signals: last-commit recency, issue responsiveness, contributing clarity.

## Pitfalls

Beautiful READMEs describing version 0.9 to users of version 3.2. Install instructions tested on the author's machine (with its hidden global state). Feature lists replacing the why. Wall-of-text with no visual hierarchy.

## Verification

Cold-environment install succeeds using only README text; time-to-first-success under 10 minutes; a stranger summarizes the project correctly after reading.

## Inputs

- Task context: the repo, clean environment access

## Outputs

- diagnosis report + prioritized fixes

## Related

local-dev-bootstrap, tutorial-scaffolder
