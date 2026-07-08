---
name: kraken-abyssal
description: >-
  Abyssal external-research method — evidence-based answers about external libraries, frameworks, and docs, every claim citing a permanent version-pinned source. Use for questions about libraries/frameworks outside this repo: 'how do I use X', 'how does X implement Y', 'X vs Y', troubleshooting, or version history. Clone repos, extract commit SHAs for permalinks, synthesize with mandatory citations. Part of the kraken-engineer mindset family — adopt directly; compose with kraken-engineer for process and specialist skills for technique.
---

# External Research (Abyssal method)

Investigate external libraries, frameworks, and documentation to provide
evidence-based answers. Every factual claim cites a permanent, version-pinned
source. Researchers who cite sources let downstream decisions be verified.

## Research Framework

### Phase 1: Request Classification
| Type | Indicators | Primary method |
|------|------------|----------------|
| Conceptual | "How do I use X?", "What is Y?" | Documentation synthesis |
| Implementation | "How does X implement Y?", "Show me code" | Source code analysis |
| Historical | "Why was X changed?", "When was Y added" | Version-control analysis |
| Comparative | "X vs Y", "Which is better for Z" | Feature analysis |
| Troubleshooting | "Why does X fail?", "How to fix Y" | Root-cause analysis |

### Phase 2: Information Gathering
1. **Documentation discovery** — locate official docs URL; identify
   version-specific docs; map structure.
2. **Source code investigation** — clone the repository to a temporary
   directory; extract the commit SHA for permanent references; locate relevant
   implementation files; construct permalinks.
3. **Version history** — search the issue tracker; review PR discussions; read
   release notes; trace file history (`git log --follow`, `git blame`).

### Phase 3: Evidence Synthesis
```
## Research Summary
Topic / Type / Confidence
## Key Findings
### Finding 1: [title]
**Evidence**: [permanent link to source]
```[language]
// relevant code or documentation
```
**Explanation**: [how this answers the question]
## Version Information
- Library: [name]@[version]
- Documentation: [URL]
- Source Reference: [permalink]
## Recommendations
1. [actionable]
## Open Questions
1. [unanswered]
```

## Citation Requirements (mandatory)
Every factual claim must include:
- **Permanent link** — `https://github.com/owner/repo/blob/<sha>/path#L<start>-L<end>` (commit SHA, never a branch name).
- **Version context** — specific version or commit referenced.
- **Direct evidence** — actual code or documentation text, not just interpretation.

## Quality Gates
- **Source verification** — all claims traceable to a source.
- **Link permanence** — all links use commit SHA.
- **Direct evidence** — code/examples included, not just references.
- **Completeness** — all aspects of the question addressed.

Remember: provide evidence-based answers with traceable sources so decision-makers can verify and build on your findings.
