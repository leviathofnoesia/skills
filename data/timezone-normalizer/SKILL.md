---
name: timezone-normalizer
description: "Find and fix mixed timezone storage and rendering bugs."
---

# Timezone-Normalizer

Find and fix mixed timezone storage and rendering bugs..

## When to Use

Timestamps stored/rendered inconsistently produce off-by-hours bugs that only users notice.

## Workflow

1. Inventory timestamp handling: storage format (UTC?), timezone metadata presence, rendering locations.
2. Classify violations: naive datetimes, mixed storage zones, client-time assumptions, DST-naive arithmetic.
3. Standardize storage to UTC-with-explicit-type; convert ONLY at render boundary.
4. Fix arithmetic to be zone-aware (adding hours across DST boundaries lies otherwise).
5. Add tests pinning behavior around DST transitions and midnight crossings.

## Pitfalls

Server local time sneaking into logs/storage. 'Just add the offset' math that breaks twice yearly. Rendering UTC raw to users who think their appointment moved. Testing only from the developer's timezone.

## Verification

Deliberate DST-boundary test suite passes; rendered times correct for users in zones unlike the server's; storage audit shows zero naive timestamps.

## Inputs

- Task context: codebase timestamp usage, DB samples

## Outputs

- normalized storage + zone-aware rendering + edge-case tests

## Related

csv-hygiene, metric-definition-sheet
