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

## Install

Copy or symlink a skill directory into your agent skills path, or install the
packaged `.skill` file if your harness supports it.

```bash
# Claude Code / compatible harness example
ln -s "$(pwd)/SEO/HOTE-Play" ~/.claude/skills/HOTE-Play
```

## Package a skill

```bash
python3 path/to/skill-creator/scripts/package_skill.py ./SEO/HOTE-Play ./dist
```

## License

Unless noted otherwise in a skill folder, content is available for use with AI
coding agents. Attribution appreciated.
