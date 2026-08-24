# Sdk-Design-Review - Human Guide

Review a public SDK/API surface for ergonomics and stability.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Reviews an SDK like a product: naming consistency, right-sized public surface, and whether a stranger can complete real tasks without help.

## When to use it

Pre-release of any public library. Triggers: SDK review, developer experience, API ergonomics.

## When NOT to use it

Internal libraries can start lighter — full review at first external consumer. Not a style-guide enforcement pass.

## How you know it worked

Doc examples run in CI and a cold-start user finishes all three tasks unaided.
