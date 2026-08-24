# Timezone-Normalizer - Human Guide

Find and fix mixed timezone storage and rendering bugs.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Fixes the entire class of off-by-hours bugs: standardize storage to UTC, convert only when showing users, do timezone-aware math, and pin it all with DST-edge tests.

## When to use it

Scheduling features, global user bases, log correlation across services. Triggers: timezone, UTC, off by hours, DST.

## When NOT to use it

Single-timezone internal tools can defer. Don't normalize what's already correctly handled.

## How you know it worked

Users in three different zones confirm identical event times render correctly; the DST test suite exists and passes.
