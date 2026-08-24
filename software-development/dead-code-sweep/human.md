# Dead-Code-Sweep - Human Guide

Find and safely remove dead code with call-graph evidence.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

It hunts code nothing uses anymore and deletes only what it can PROVE is unused. It checks hidden call paths (dynamic dispatch, reflection, string-based routing) before declaring anything dead.

## When to use it

Use it before big refactors or after retiring features. Trigger words: dead code, cleanup, unused, remove legacy.

## When NOT to use it

Not for deleting code you merely dislike. If something might be needed by a rollback plan or an external consumer, it stays.

## How you know it worked

Tests pass after removals, builds get smaller, and every deletion is its own revertable commit.
