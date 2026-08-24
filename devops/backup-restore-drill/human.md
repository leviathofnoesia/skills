# Backup-Restore-Drill - Human Guide

Actually restore from backup and time it; prove RTO/RPO.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Actually restores backups into a clean environment against a stopwatch — exposing the missing pieces (secrets, buckets, DNS) that make untested backups fictional.

## When to use it

Quarterly minimum; after any infrastructure migration. Triggers: disaster recovery, backup testing, restore.

## When NOT to use it

Not for active production databases (use replicas/snapshots environments). Don't skip the stopwatch — unmeasured restores prove nothing.

## How you know it worked

The report shows real numbers: X hours to restore, Y minutes data loss — and they meet stated targets.
