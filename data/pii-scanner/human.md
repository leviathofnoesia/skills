# Pii-Scanner - Human Guide

Locate PII leaking into logs, fixtures, and exports.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Hunts personal information hiding in places it shouldn't be — logs, fixtures, exports — using patterns plus entropy tricks, then wires the scanner into CI so leaks stay out.

## When to use it

Pre-release of anything leaving the trust boundary. Triggers: PII, privacy scan, data leak.

## When NOT to use it

Not legal compliance certification — counsel confirms regulatory posture. Internal-only trusted stores may prioritize differently.

## How you know it worked

Planted test PII gets caught by CI; current artifacts show zero unjustified hits.
