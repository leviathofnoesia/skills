---
name: backup-restore-drill
description: "Actually restore from backup and time it; prove RTO/RPO."
---

# Backup-Restore-Drill

Actually restore from backup and time it; prove RTO/RPO..

## When to Use

Backups exist but have never been restored; or restore time expectations are folklore.

## Workflow

1. Define RTO/RPO targets honestly: how much data loss is tolerable, how fast must recovery complete?
2. Select backup set; document the FULL restore path including secrets, config, DNS — everything beyond raw data.
3. Execute restore into clean environment against the clock; log every stall point.
4. Verify restored state: data integrity checks, application smoke tests, business-critical queries.
5. Record measured RTO/RPO vs targets; fix the gaps (usually undocumented steps or missing pieces).

## Pitfalls

Restoring into the same environment with cached secrets masking gaps. Backups of the database but not the bucket. Nobody timing it ('it worked eventually'). Success declared before application-level verification.

## Verification

Measured RTO/RPO recorded against targets; every stall point fixed and re-drilled; restore evidence archived.

## Inputs

- Task context: backup system access, clean environment

## Outputs

- timed drill report + gap fixes + confidence rating

## Related

secret-rotation-playbook, runbook-author
