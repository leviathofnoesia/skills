# Migration-Planner - Human Guide

Plan zero-downtime schema migrations with reversible steps.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Converts scary migrations into boring sequences: add alongside old, move gradually, switch reads, retire old — each step reversible and rehearsed.

## When to use it

Any live-data schema change. Triggers: migration, zero-downtime, cutover.

## When NOT to use it

Empty tables or maintenance-window-friendly systems favor simpler paths.

## How you know it worked

Rehearsal ran at production scale; every step's rollback was executed once.
