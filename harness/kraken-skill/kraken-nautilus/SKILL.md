---
name: kraken-nautilus
description: >-
  Nautilus codebase-search method — systematic, cross-validated codebase exploration with structured results. Use for multi-module or multi-angle search: 'where is X defined', 'who calls X', pattern matching, navigation, or history. Picks the right tool per intent (LSP definitions/references, ast_grep, grep, glob, git log/blame), runs independent searches in parallel, and cross-validates. Part of the kraken-engineer mindset family — adopt directly; compose with kraken-engineer for process and specialist skills for technique.
---

# Codebase Search (Nautilus method)

Systematic search with cross-validation and structured results. Goal: make the
requester successful with minimal follow-up — comprehensive, validated,
actionable results beat fast but incomplete ones.

## Search Strategy Framework

### Phase 1: Intent Classification
| Intent | Indicators | Strategy |
|--------|------------|----------|
| Structural Discovery | "Where is X defined?", "Find class Y" | LSP definitions, `ast_grep` |
| Usage Discovery | "Who calls X?", "Where is Y used" | LSP references, `grep` |
| Pattern Matching | "Code that does X", "Files matching Y" | `ast_grep`, `glob`, `grep` |
| Navigation | "Find file near X", "What contains Y" | `glob` |
| Historical | "When was X added?", "Who changed Y" | `git log`, `git blame` |

### Phase 2: Tool Selection Matrix
**LSP** (when available): `definition` (where defined), `references` (who uses
it), `documentSymbols` (what's in a file), `hover` (symbol details).

**`ast_grep`** (structural): function definitions matching a pattern; class
structures with specific methods; import patterns; AST-based code patterns.

**`grep`** (text): string literals; comments mentioning concepts; log
statements; TODO/FIXME.

**`glob`** (files): by extension (`*.ts`, `*.py`); by name pattern (`auth*.ts`);
directory traversal.

**`git`** (history): `git log --oneline -S "query"`; `git blame`; `git log --follow`.

### Phase 3: Parallel Execution
Launch independent searches in parallel:
- `definition` + `references` (understand a symbol fully)
- `grep` + `ast_grep` (text + structural)
- `glob` + `grep` (discovery + verification)
- multiple `grep` variations

**Cross-validate** results across tool types to ensure completeness.

### Phase 4: Result Synthesis
```
<analysis>
Search Intent: [classification]
Query Strategy: [tools]
Confidence: High/Medium/Low
</analysis>
<results>
<primary_findings>[most relevant, ranked]</primary_findings>
<supporting_evidence>[additional context]</supporting_evidence>
<confidence_indicators>
- [ ] All expected matches found
- [ ] Cross-validated across tools
- [ ] No obvious gaps in search space
</confidence_indicators>
<next_steps>[what the requester should do next]</next_steps>
</results>
```

## Quality Assurance
| Criterion | Requirement |
|-----------|-------------|
| Paths | ALL paths absolute (start with `/`) |
| Completeness | find ALL relevant matches |
| Actionability | requester can proceed without follow-up |
| Validation | cross-validated across tool types |

**Failure** if: any path is relative; obvious matches missed; no structured
`<results>` block; tools don't match intent.

## Search Optimization
- **Breadth-first**: broad (`glob`, `grep -r`) → narrow (`definition`, `ast_grep`) → validate.
- **Depth-first**: specific symbol (`definition`) → usage (`references`) → relationships (`git`).
- **Multi-module**: identify module boundaries (imports) → search each in parallel → synthesize by module.

Output: no emojis, absolute paths only, structured tags. Make the requester successful with minimal follow-up.
