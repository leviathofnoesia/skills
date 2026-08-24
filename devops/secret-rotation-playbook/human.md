# Secret-Rotation-Playbook - Human Guide

Rotate credentials with zero downtime and verified cutover.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Rotates credentials safely: rehearse on low-risk keys first, migrate consumers before revoking anything, prove old keys actually die, and install a rotation calendar.

## When to use it

Post-leak, post-departure, periodic hygiene. Triggers: rotate keys, credential lifecycle, secret management.

## When NOT to use it

Don't rotate during peak traffic windows. Some secrets (encryption keys protecting existing data) need special migration handling beyond this playbook.

## How you know it worked

The old key demonstrably fails somewhere you test it; nothing broke because everything migrated first.
