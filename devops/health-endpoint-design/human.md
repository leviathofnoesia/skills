# Health-Endpoint-Design - Human Guide

Design liveness/readiness endpoints that tell the truth.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Designs health checks that tell the truth: liveness separate from readiness, dependencies checked in the right place, so load balancers stop killing healthy fleets during dependency blips.

## When to use it

Any service behind orchestration/load balancing. Triggers: health check, liveness probe, readiness probe.

## When NOT to use it

Single-instance services without orchestration need less ceremony. Don't over-engineer static sites.

## How you know it worked

Induced dependency failure drains traffic WITHOUT mass restarts; genuine deadlock still triggers recovery.
