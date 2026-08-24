# Capacity-Headroom-Check - Human Guide

Measure headroom before traffic events; set scaling triggers.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Predicts exactly which resource dies first under upcoming traffic — usually not the one you'd scale instinctively — then sets triggers accounting for how slowly scaling actually happens.

## When to use it

Pre-launch, Black Friday, viral moments. Triggers: capacity planning, headroom, will we survive.

## When NOT to use it

Steady-state systems with proven autoscaling can spot-check rather than deep-dive. Pre-product systems lack baseline data.

## How you know it worked

The predicted breaking resource was right (or safely wrong with margin); scaling triggered with enough lead time.
