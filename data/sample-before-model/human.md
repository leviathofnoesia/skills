# Sample-Before-Model - Human Guide

Profile distributions and leakage before any modeling.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Forces the boring step that prevents disasters: actually looking at data distributions, hunting leakage patterns, and writing down constraints BEFORE any model touches anything.

## When to use it

Start of any prediction/modeling project. Triggers: EDA, data profiling, before modeling.

## When NOT to use it

Don't profile forever — timebox it. Well-understood internal datasets with existing profiles need refreshes, not rebuilds.

## How you know it worked

The constraint list visibly shaped model choice; zero 'surprise' leakage discoveries later.
