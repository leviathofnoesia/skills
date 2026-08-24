---
name: deploy-freeze-discipline
description: "Implement freeze windows with exception tracking."
---

# Deploy-Freeze-Discipline

Implement freeze windows with exception tracking..

## When to Use

High-stakes windows (holiday commerce, major events, audits) where change risk must drop to near zero.

## Workflow

1. Define the freeze window precisely: start/end times in explicit timezone, scope (all deploys? only risky classes?).
2. Establish exception path: who can approve, what qualifies (security patches yes, features no), how exceptions get logged.
3. Communicate early and repeatedly: calendar invites, deploy-tool warnings, pre-freeze reminder.
4. Prepare the hotfix lane BEFORE freeze: tested emergency process that bypasses without abandoning discipline.
5. Post-freeze: staged unfreeze with monitoring, plus retro on exceptions requested vs granted.

## Pitfalls

Freezes without exception paths breeding dangerous workarounds. Silent freezes people discover by failed deploy. Never unfreezing officially (drift into permanent freeze). Hotfix lane untested until needed at 2am.

## Verification

Zero unauthorized deploys during window; every exception logged with approver; first post-freeze deploy ships through the normal pipeline cleanly.

## Inputs

- Task context: business calendar, deployment tooling

## Outputs

- enforced freeze + exception log + tested hotfix lane

## Related

oncall-transition-kit, config-change-journal
