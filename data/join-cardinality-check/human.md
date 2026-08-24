# Join-Cardinality-Check - Human Guide

Verify expected row counts before/after joins to catch fan-out.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Prevents the classic doubled-revenue disaster: predicts how many rows a join SHOULD produce, verifies reality matches, and hunts down the duplication when it doesn't.

## When to use it

New analytical queries, post-migration verification, suspicious metrics. Triggers: join, duplicate rows, fan-out, double counting.

## When NOT to use it

Exploratory one-off queries may skip ceremony. Tiny lookup-table joins rarely surprise.

## How you know it worked

Injected duplicate keys trip your assertions instantly; reports stay trustworthy.
