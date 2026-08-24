# Env-Parity-Audit - Human Guide

Diff dev/staging/prod config and surface drift.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Systematically compares configuration across environments to expose invisible drift — the temporary hacks and forgotten flags causing works-in-dev mysteries.

## When to use it

Environment-specific bug reports, pre-launch hardening, post-incident reviews. Triggers: environment parity, config drift.

## When NOT to use it

Intentional scale differences are fine — audit catches ACCIDENTAL divergence. Solo projects may track informally.

## How you know it worked

Deliberate misconfiguration planted in staging gets caught by the parity job within one cycle.
