# Raindrop.ai Concepts — Observability for AI Agents

## What Raindrop.ai Is

Raindrop.ai is "the Sentry for AI Agents" — a monitoring and quality platform built specifically for AI agents in production. While traditional observability (Sentry, Datadog, New Relic) tracks uptime, latency, and error rates, Raindrop focuses on **failure modes unique to LLMs and agents**.

## Key Sources

- Homepage: https://www.raindrop.ai/
- Docs: https://www.raindrop.ai/docs/introduction/
- Medium: Raindrop AI article by Anshul Kulhari (Sep 25, 2025)
- Blog: https://www.raindrop.ai/blog/ (incl. "Self Diagnostics")
- SDK: https://www.raindrop.ai/docs/sdk/typescript

## The Agent Observability Gap

Traditional logs and APM miss these LLM/agent failure modes:

1. **Silent tool errors** — tool returns an error but agent doesn't surface it
2. **Forgetting** — agent loses context between turns
3. **Vague replies** — LLM gives a short, unhelpful response
4. **Persona drift** — agent deviates from intended behavior
5. **Hallucinations** — agent generates false information confidently
6. **Loops** — agent repeats same action/tool call indefinitely
7. **Broken tools** — auth failures, API changes, config issues

## Self Diagnostics

Raindrop's "Self Diagnostics" lets **agents proactively report their own issues**:
- Capability gaps ("I can't access the user's calendar")
- Missing context ("I need the user's timezone")
- Persistent tool failures ("My web search has been erroring")

Requires `eventId` to correlate with the interaction trace. SDK wrapping:
```typescript
const { generateText, streamText } = raindrop.wrap(ai, {...});
```

## Signals vs Incidents

- **Signals**: Individual anomaly detections from classifiers, manual tracking,
  or agent self-diagnostics
- **Incidents**: Groups of related signals with shared root cause. Clusters
  signals, tracks issue rates, enables alerting on spikes

## Slack Integration

Raindrop "lives in Slack" — reads traces, sends real failures to Slack.
Teams can ask questions, triage issues, create signals in Slack.

## Implementation in Abyss

1. **Activity recording** via Hermes hooks (traces)
2. **Signal classifiers** detecting silent failures in results
3. **Self-diagnostics** via `/abyss diagnostic <capability> <gap>`
4. **Incident clustering** grouping signals by session (2+ signals)
5. **Slash commands** for querying (CLI equivalent of Slack integration)

## Key Takeaways

- Don't just log — **detect failure patterns**
- Signals should be **actionable** (severity, label, description, session)
- Incidents **group** related signals to reduce noise
- Self-diagnostics let the **agent be first line of defense**
- Traces must include **full context** (args, results, timings, depths)
