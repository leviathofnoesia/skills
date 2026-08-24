---
name: local-dev-bootstrap
description: "Make 'clone to running' under 10 minutes with one command."
---

# Local-Dev-Bootstrap

Make 'clone to running' under 10 minutes with one command..

## When to Use

New contributors lose days to environment setup; 'works on my machine' includes setup archaeology.

## Workflow

1. Document current reality: every manual step a newcomer needs today (the honest baseline).
2. Automate the sequence into one entry point: make dev / ./bootstrap script handling deps, env, data seeds, service starts.
3. Pin everything pinnable: language versions, dependency locks, seed data snapshots.
4. Handle the secrets problem: dev defaults that work offline, clear pointer for needed credentials.
5. Test on truly clean machines regularly (CI job or VM snapshot) — bit rot is inevitable otherwise.

## Pitfalls

Bootstrap scripts assuming pre-installed global tools. Seed data referencing prod-like secrets. Working once then rotting silently (no clean-machine testing). Documentation describing an aspirational setup nobody verified recently.

## Verification

Clean-machine test passes end-to-end; time-from-clone-to-running-app measured under 10 minutes; README instructions match script behavior exactly.

## Inputs

- Task context: repo, target stack knowledge

## Outputs

- one-command bootstrap + clean-machine CI verification

## Related

readme-doctor, env-parity-audit
