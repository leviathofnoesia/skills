# Feature-Flag-Lifecycle - Human Guide

Manage feature flags: naming, expiry, cleanup, kill switches.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Keeps feature flags from becoming archaeology: every flag has an owner, purpose, expected death date, and a regular cleanup report.

## When to use it

Flags pile up or after a bad flip. Triggers: feature flag, kill switch, toggle debt.

## When NOT to use it

Don't run where flags ARE the product (CMS toggles). Not for one-day branches.

## How you know it worked

'What does flag X do, who owns it, when does it die?' answerable in under a minute.
