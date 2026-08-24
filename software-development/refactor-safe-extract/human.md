# Refactor-Safe-Extract - Human Guide

Extract functions/classes behaviorally with seam-first testing.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

The discipline of cutting big code into small pieces WITHOUT changing what it does: pin behavior first, move code verbatim second, improve only after structure is safe.

## When to use it

Any 'this function is 800 lines' moment. Triggers: refactor, extract, split, untangle.

## When NOT to use it

Not while a feature change rides in the same PR. Not without the ability to run the tests that pin behavior.

## How you know it worked

Every commit in the series is reviewable as pure movement; bisect stays useful throughout.
