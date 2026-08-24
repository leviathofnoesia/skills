# Api-Versioning-Strategy - Human Guide

Choose and implement an API versioning scheme that ages well.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Picks how your API will age: where versions live, what counts as breaking, how long old versions live, and how you'll know who still uses them.

## When to use it

Before first external consumer, or before the first painful breaking change. Triggers: API version, breaking change, deprecation.

## When NOT to use it

Internal-only APIs between teams on one deploy cadence usually need contracts, not versions.

## How you know it worked

Your next unavoidable breaking change ships without surprise: consumers got noticed, telemetry showed who migrated.
