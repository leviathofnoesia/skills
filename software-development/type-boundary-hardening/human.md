# Type-Boundary-Hardening - Human Guide

Introduce strict types at module boundaries incrementally.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Adds strict typing where it pays off — at the edges where outside data enters — then lets inference handle the inside. Fails fast on bad input with useful messages.

## When to use it

Runtime type errors cluster at integration points. Triggers: types, validation, boundary, strict mode.

## When NOT to use it

Not a big-bang strict-mode rollout. Skip for exploratory code where shapes are genuinely fluid.

## How you know it worked

Feed garbage into the boundary: it rejects with a message pointing at the exact field.
