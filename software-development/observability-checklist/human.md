# Observability-Checklist - Human Guide

Audit a service for metrics, logs, traces before it ships.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

A pre-flight inspection for whether you'll SEE problems: golden signals per endpoint, working dashboards, alerts that reach humans with runbooks attached.

## When to use it

Before launches and after blind incidents. Triggers: observability, monitoring, alerting, golden signals.

## When NOT to use it

Not a substitute for actually designing SLOs. Skip the theater of dashboards for hobby projects where logs suffice.

## How you know it worked

Break something small on purpose: the right alert fires, links to a runbook, and reaches a human.
