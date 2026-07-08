# Documentation (Siren method)

Create clear, comprehensive, actionable documentation using information-architecture principles. Docs developers actually want to read reduce support burden and accelerate adoption.

## Documentation Framework

### Phase 1: Documentation Analysis
1. **Content mapping** — topics to cover; logical ordering; references connecting topics.
2. **Audience assessment** — who reads it; prior knowledge assumed; tasks they'll accomplish.
3. **Format selection** — README (overview/quick start); API Reference (complete signatures); Tutorial (step-by-step); Guide (problem-solution).

### Phase 2: Content Development
1. **Clarity** — active voice; short sentences; define terms on first use; concrete examples.
2. **Structure** — logical sections with clear headings; progressive complexity; cross-references; consistent formatting.
3. **Code examples** — complete and runnable; commented; include error handling; show success **and** failure cases.

### Phase 3: Quality Verification
1. **Readability** — scannable with headers; clear navigation; no unexplained jargon.
2. **Accuracy** — code examples tested and working; API signatures match implementation; commands verified in context.
3. **Completeness** — all public APIs documented; common use cases covered; error conditions explained.

## Output Format
```
# [Title]
## Overview
## Prerequisites
## [Section] / ### [Subsection]  (with runnable code examples)
## API Reference
### [Function/Class]
**Signature**: `...`
**Description**: ...
**Parameters**: | Name | Type | Description |
**Returns**: ...
**Example**: ...
## Troubleshooting
### [Problem] / [Solution]
```

## Quality Checklist (before completing)
- [ ] All code examples tested and working
- [ ] All APIs have complete signatures
- [ ] Cross-references verified
- [ ] Readable by target audience
- [ ] Consistent formatting throughout

Remember: clear, accurate, complete documentation reduces support burden and accelerates adoption.
