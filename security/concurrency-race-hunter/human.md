# Concurrency-Race-Hunter - Human Guide

Reproduce and fix races via invariants plus forced interleavings.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Hunts heisenbugs systematically: map shared state, assert invariants continuously, force interleavings under load, fix with boring primitives — not narrower race windows.

## When to use it

Once-in-a-hundred failures, corrupted state mysteries, works-in-debug ghosts. Triggers: race condition, intermittent, concurrency.

## When NOT to use it

Single-threaded code has no races (check for hidden threads in frameworks first). Don't hunt without soak-test infrastructure.

## How you know it worked

Soak tests pass clean for days; the specific incident class stops recurring.
