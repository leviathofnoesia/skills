# Chaos-Drill-Lite - Human Guide

Run small controlled failure drills against your own service.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Small, controlled failure experiments that test whether your resilience code actually works — because untested fallbacks are folklore.

## When to use it

Before big traffic events or after adding retry/fallback logic. Triggers: chaos, resilience, failover, drill.

## When NOT to use it

Never in production without established staging practice. Skip if you can't define an abort switch first.

## How you know it worked

The drill produced evidence: metrics showing graceful degradation, plus filed fixes for what didn't degrade gracefully.
