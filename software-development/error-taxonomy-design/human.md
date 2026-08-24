# Error-Taxonomy-Design - Human Guide

Design consistent error types and codes across a codebase.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

It gives your project one consistent language for failures: what users see, what machines parse, what engineers debug. No more mystery strings in logs.

## When to use it

Use when starting a service, before integrating partners, or when logs have become guesswork. Triggers: error codes, error handling, exception design.

## When NOT to use it

Skip for prototypes where speed matters more than consistency. Do not retrofit a giant taxonomy in one pass; do it boundary-first.

## How you know it worked

New code has no ad-hoc error strings; the code registry documents every error a client can hit.
