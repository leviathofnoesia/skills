# Test-Data-Builder-Pattern - Human Guide

Replace brittle test fixtures with composable builder factories.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Replaces brittle shared test fixtures with small factories: every test states only the fields it cares about, defaults handle the rest.

## When to use it

When fixture edits cause cascading red. Triggers: test data, fixtures, factory, builder.

## When NOT to use it

Skip for tiny suites where two plain fixtures win on simplicity. Don't build meta-frameworks around it.

## How you know it worked

Changing a model field updates ONE builder instead of thirty fixtures.
