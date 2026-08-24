# Load-Test-From-Logs - Human Guide

Build realistic load profiles by replaying production traffic shapes.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Builds load tests that look like YOUR traffic — real endpoint mixes and burst patterns mined from your logs — instead of generic synthetic loops that miss real bottlenecks.

## When to use it

Before capacity events or after load tests pass but prod falls over. Triggers: load testing, replay, traffic shape.

## When NOT to use it

Never replay raw logs containing user data into non-prod without synthesis. Skip for pre-traffic systems (no truth yet).

## How you know it worked

The scenario README cites the exact log query it came from; the found bottleneck has a named resource cause.
