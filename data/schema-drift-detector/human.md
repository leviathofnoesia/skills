# Schema-Drift-Detector - Human Guide

Detect silent schema drift between environments or snapshots.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Compares database schemas across environments to expose silent divergence — missing migrations, manual hotfixes, abandoned experiments — before they cause mystery failures.

## When to use it

'Works in dev, breaks in prod', pre-deploy checks, periodic hygiene. Triggers: schema diff, environment drift.

## When NOT to use it

Single-environment setups have nothing to drift against. Don't run during deploy windows.

## How you know it worked

Every reported difference gets explained (migration gap/hotfix/allowlisted); clean re-scan after remediation.
