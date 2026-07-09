# skills

[![skills.sh](https://skills.sh/b/leviathofnoesia/skills)](https://skills.sh/leviathofnoesia/skills)

Agent skills by [leviathofnoesia](https://github.com/leviathofnoesia).

Skills are grouped by topic to avoid collisions as the collection grows. Each
skill lives at `TOPIC/SKILL-NAME/` and is a self-contained package
(`SKILL.md` + optional `scripts/`, `references/`, `assets/`).

## Skills

| Topic | Skill | Description |
|-------|-------|-------------|
| SEO | [HOTE-Play](./SEO/HOTE-Play/) | **Home of the Entity Play** — multi-surface SEO: classic ranking, AEO, GEO (`llms.txt`), schema entity graphs, E-E-A-T, freshness, authority triangles, and adversarial nemesis probes |
| meta | [lean-turns](./meta/lean-turns/) | **Token-optimized conversational turns** — write intermediate turns lean, reserve full prose for the final deliverable turn |
| meta | [lean-turns-strict](./meta/lean-turns/lean-turns-strict/) | **Token-suppressed intermediate turns** — one status token per intermediate turn, full prose reserved for the final deliverable; agent understanding unchanged |

## Install

Use the [`skills`](https://www.npmjs.com/package/skills) CLI to install a
skill straight from this repo:

```bash
# Install one skill by topic/name path
npx skills add leviathofnoesia/skills/SEO/HOTE-Play

# Or install the whole repo's skills
npx skills add leviathofnoesia/skills
```

Manual fallback (symlink into your harness skills path):

```bash
ln -s "$(pwd)/SEO/HOTE-Play" ~/.claude/skills/HOTE-Play
```

## License

Unless noted otherwise in a skill folder, content is available for use with AI
coding agents. Attribution appreciated.
