# Config-Change-Journal - Human Guide

Journal every manual infra change with who/why/revert.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

A low-friction log for manual infrastructure changes: what, why-now, and how-to-revert for everything outside your pipelines — ending 'someone changed something' mysteries.

## When to use it

Any environment where console/SSH changes happen alongside IaC. Triggers: config tracking, manual changes, audit trail.

## When NOT to use it

Fully-IaC environments need this only for exceptions. Don't journal what git already records.

## How you know it worked

Next incident consults the journal and finds the answer; reconciliation catches planted unlogged change.
