# Monorepo-Split-Plan - Human Guide

Plan extracting a package from a monorepo without breaking CI.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Plans pulling one package out of a monorepo into its own home: history preserved, CI mirrored before cutover, consumers moved via registry not file paths.

## When to use it

When ownership or release cadence demands separation. Triggers: monorepo, extract package, split repo.

## When NOT to use it

Don't split for aesthetics alone — multi-repo has real coordination cost. Skip if the only pain is CI time (fix caching instead).

## How you know it worked

Both pipelines green at cutover, no consumer breaks, history blame still works in the new home.
