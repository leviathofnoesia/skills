# Retry-Policy-Designer - Human Guide

Choose retry/backoff/timeout policies per external dependency.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Designs deliberate retry/timeout/circuit-breaker policies per external dependency — respecting idempotency, adding jitter, and knowing when to give up gracefully.

## When to use it

Any integration with things you don't control. Triggers: retry logic, timeout, circuit breaker, resilience.

## When NOT to use it

Don't retry what isn't safe to repeat. Internal calls on reliable networks may need less ceremony.

## How you know it worked

Induced failures produce textbook backoff curves and clean recovery — verified by metrics, not vibes.
