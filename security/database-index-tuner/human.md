# Database-Index-Tuner - Human Guide

Rank and tune indexes by measured impact minus write tax.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Systematic index tuning ranked by real impact: find what scans shouldn't, add minimal indexes measuring write-tax, remove dead weight — one change at a time with evidence.

## When to use it

Data grew past initial design; p95s climbing; dashboards slow. Triggers: slow query, indexing, EXPLAIN.

## When NOT to use it

Small tables don't need tuning. Don't tune what you can't test at realistic scale.

## How you know it worked

Before/after timings on production-shaped data prove the win; write path unharmed.
