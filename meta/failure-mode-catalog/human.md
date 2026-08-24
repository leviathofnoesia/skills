# Failure-Mode-Catalog - Human Guide

Enumerate how this task can fail before starting it.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

A structured brainstorm of every way a thing can break — inputs, dependencies, timing, partial failures — then deliberate decisions about which get handled, tested, or consciously accepted.

## When to use it

Design phase of anything failure-prone. Triggers: edge cases, failure modes, robustness.

## When NOT to use it

Don't enumerate to infinity — rank by likelihood × blast radius. Skip for throwaway scripts.

## How you know it worked

Breaking the system in each cataloged way produces the documented response, not a surprise.
