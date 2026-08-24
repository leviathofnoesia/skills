# Null-Pandemic-Audit - Human Guide

Quantify and root-cause null inflation across tables/columns.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Treats rising null counts as the epidemic they are: quantifies spread, traces each outbreak to its origin (usually a specific deploy), and installs monitors as vaccines.

## When to use it

Distrusted dashboards, mysterious data gaps. Triggers: missing data, null values, data quality.

## When NOT to use it

Legitimately-optional fields aren't sick. Don't chase historical nulls whose sources are long dead — document instead.

## How you know it worked

Null curves visibly bend after fixes; the monitor demonstrably fires on induced recurrence.
