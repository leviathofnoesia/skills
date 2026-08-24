# Event-Schema-Versioning - Human Guide

Version analytics events so downstream queries never break.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Brings API-style discipline to analytics events: explicit contracts, additive-only evolution, new-event-for-breaking-changes, and validation that kills bad events at birth.

## When to use it

Any event-driven analytics or inter-service events. Triggers: event schema, tracking plan, breaking change.

## When NOT to use it

Prototype-stage products can defer ceremony. Don't version what's genuinely disposable logging.

## How you know it worked

A breaking change attempt fails validation in staging; consumers migrated on evidence, not hope.
