# Csv-Hygiene - Human Guide

Repair encoding, quoting, and type-coercion issues in CSVs.. This guide explains what it does, when to reach for it, and how to
tell it worked.

## What this skill does

Repairs chaotic CSV files systematically: detects real encodings, survives hostile quoting, catches Excel's date mangling and silent type coercion — documenting every fix applied.

## When to use it

Vendor imports, legacy exports, any 'just open it in Excel' history. Triggers: CSV import, parsing errors, mangled data.

## When NOT to use it

Clean machine-generated CSVs need only validation, not archaeology. JSON/Parquet inputs skip this entirely.

## How you know it worked

Strict-parser round trip is lossless; violation report would have caught today's bug yesterday.
