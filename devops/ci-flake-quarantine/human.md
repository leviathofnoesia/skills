# Ci-Flake-Quarantine - Human Guide

Quarantine flaky CI jobs without losing signal.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Stops flaky tests from poisoning CI trust: measure actual flakiness, quarantine the guilty without deleting them, auto-ticket with evidence, and enforce fix-or-delete deadlines.

## When to use it

Retry-button culture emerging, main branch perpetually yellow. Triggers: flaky tests, CI stability.

## When NOT to use it

Don't quarantine consistently-failing tests (that's just broken — fix now). Small suites can fix directly.

## How you know it worked

Quarantined tests actually get fixed/deleted by deadline; main stays reliably green.
