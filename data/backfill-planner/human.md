# Backfill-Planner - Human Guide

Plan safe historical backfills with idempotent batches.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Runs historical data repairs without melting production: idempotent resumable batches, rehearsed at scale first, monitored live, verified thoroughly after.

## When to use it

Logic changed and history needs regenerating. Triggers: backfill, recompute historical, data repair.

## When NOT to use it

Small tables can just UPDATE in place. Don't backfill what the source system can regenerate more reliably.

## How you know it worked

Zero-target predicate scan passes; the kill-and-resume test produced byte-identical results.
