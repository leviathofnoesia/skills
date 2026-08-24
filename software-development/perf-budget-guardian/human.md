# Perf-Budget-Guardian - Human Guide

Set and enforce performance budgets in CI with regression alerts.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

It turns 'the app feels slow lately' into a number that fails CI. You set the limits users would care about; the pipeline enforces them on every change.

## When to use it

Use once performance is a feature. Triggers: performance budget, bundle size, p95, regression.

## When NOT to use it

Skip pre-product-market-fit micro-optimization. Don't budget what you can't measure reliably yet.

## How you know it worked

A knowingly slow change gets blocked by CI showing exactly how much over budget it is.
