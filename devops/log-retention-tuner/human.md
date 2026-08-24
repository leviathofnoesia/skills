# Log-Retention-Tuner - Human Guide

Right-size log retention vs cost vs debugging need.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Balances log value against storage cost: classify streams by purpose, tier them accordingly, sample aggressively where safe — while proving incident investigation still works.

## When to use it

Log bills growing, or 'we deleted that' during incident review. Triggers: log retention, storage costs, logging policy.

## When NOT to use it

Compliance-mandated streams aren't negotiable — check requirements before optimizing. Tiny volumes don't justify tuning effort.

## How you know it worked

Costs visibly dropped AND the last incident type remains fully investigable.
