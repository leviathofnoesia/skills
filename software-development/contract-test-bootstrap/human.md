# Contract-Test-Bootstrap - Human Guide

Stand up consumer-driven contract tests between two services.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

It makes the promise between two services executable: consumers write what they need, providers prove they deliver it — both in their own CI pipelines.

## When to use it

Use when two teams keep breaking each other at integration time. Triggers: contract testing, pact, integration breaks, provider/consumer.

## When NOT to use it

Skip for single-team projects where one deploy unit covers both sides. Not a substitute for E2E smoke of critical journeys.

## How you know it worked

Break the contract on purpose: provider CI must go red before anything deploys.
