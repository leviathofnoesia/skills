# Infra-Tagging-Standard - Human Guide

Enforce resource tagging for ownership and cost allocation.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Establishes a tiny mandatory tagging scheme (owner-team, environment, cost-center), enforces it at creation, and cleans up history so every resource answers 'whose is this?' instantly.

## When to use it

Multi-team cloud usage, cost allocation disputes, incident ownership confusion. Triggers: resource tagging, cloud governance.

## When NOT to use it

Solo accounts with five resources can hold the map in their head. Don't tag what automation already groups logically.

## How you know it worked

Untagged-resource report runs empty; cost-by-team query replaces spreadsheet archaeology.
