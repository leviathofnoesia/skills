# Api-Doc-Sketcher - Human Guide

Draft reference docs from real signatures and call sites.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Generates API documentation from what the code ACTUALLY does — real captured request/response pairs, complete error tables — wired so docs fail CI when they drift.

## When to use it

Any public or partner-facing API. Triggers: API documentation, endpoint reference.

## When NOT to use it

Exploratory internal endpoints can wait. Generated OpenAPI alone isn't documentation — narrative matters too.

## How you know it worked

Copy-paste any doc example: it runs. Deliberately break an endpoint: docs build fails.
