---
name: config-change-journal
description: "Journal every manual infra change with who/why/revert."
---

# Config-Change-Journal

Journal every manual infra change with who/why/revert..

## When to Use

'Someone changed something' mysteries during incidents; manual infra edits invisible to git history.

## Workflow

1. Define what requires journaling: any change outside IaC pipeline (console clicks, SSH edits, emergency hotfixes).
2. Minimize friction: journal entry template = what changed, why now, revert path, ticket link.
3. Make it adjacent to action: journal BEFORE or WITH the change, never as homework after.
4. Review cadence: weekly scan for entries revealing patterns (same system repeatedly hand-edited = automation candidate).
5. Reconcile against reality: periodic diffs catch unjournaled changes (drift both ways).

## Pitfalls

Journals nobody writes under pressure (exactly when needed most). Journal-as-punishment culture. Entries without revert paths ('changed timeout to 30s' — from what?). Never reconciled so fiction persists.

## Verification

Incident retrospectives reference journal entries resolving 'what changed' questions; reconciliation diffs find zero undocumented changes.

## Inputs

- Task context: change process design, team buy-in

## Outputs

- working journal + reconciliation loop + automation candidates list

## Related

env-parity-audit, deploy-freeze-discipline
