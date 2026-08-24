# Cost-Anomaly-Hunt - Human Guide

Trace cloud bill spikes to specific services and causes.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Traces bill spikes to their mechanical cause — usually retries, logging, or forgotten environments — fixes the cause rather than the symptom, and installs alerts for next time.

## When to use it

Monthly bill review, pre-budget planning, post-feature-launch. Triggers: cloud costs, bill spike, spend anomaly.

## When NOT to use it

Don't chase sub-percent deltas (noise). Growth-driven increases need capacity decisions, not optimization.

## How you know it worked

Evidence names the exact mechanism (e.g., retry multiplier 4x on error X); next cycle confirms the fix.
