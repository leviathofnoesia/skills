# Code-Archaeology - Human Guide

Reconstruct why legacy code exists using git history and docs.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

It treats your codebase like a dig site: follows git history to find WHY strange code exists, separating protective weirdness from dead habit.

## When to use it

New job, inherited repo, or 'who wrote this and why' moments. Triggers: legacy, why does, history, archaeology.

## When NOT to use it

Skip when history genuinely doesn't matter (greenfield). Don't use it to assign blame for past decisions.

## How you know it worked

Weird code now carries a comment/ADR citing its origin — or was safely removed after proving no origin.
