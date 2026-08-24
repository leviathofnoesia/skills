---
name: secret-rotation-playbook
description: "Rotate credentials with zero downtime and verified cutover."
---

# Secret-Rotation-Playbook

Rotate credentials with zero downtime and verified cutover..

## When to Use

Credentials older than memory, ex-employees possibly knowing keys, or a leak just happened.

## Workflow

1. Inventory secrets: what exists, where used (grep deploy configs, CI vars, docs), who/what holds them.
2. Order rotation by blast radius: start with lowest-risk credential to rehearse mechanics.
3. For each: create successor → verify successor works in isolation → flip consumers atomically → verify → revoke predecessor → verify revocation breaks old.
4. Schedule regular rotation cadence per secret class going forward.
5. Document the playbook per provider (each has quirks).

## Pitfalls

Revoking before all consumers migrated (outage). Never verifying revocation actually blocks old key (false security). Rotation without inventory (missed consumer breaks later). Doing high-blast-radius secrets first for drama.

## Verification

Old credentials demonstrably fail post-revocation; inventory documents successor lineage; rotation calendar installed.

## Inputs

- Task context: secret inventory access, deployment windows

## Outputs

- rotated credentials + verified revocations + cadence calendar

## Related

pii-scanner, config-change-journal
