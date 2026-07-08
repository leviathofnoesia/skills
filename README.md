# skills

Agent skills by [leviathofnoesia](https://github.com/leviathofnoesia).

Each top-level directory is a skill package (`SKILL.md` + optional `scripts/`, `references/`, `assets/`).

## Skills

| Skill | Description |
|-------|-------------|
| [HOTE-Play](./HOTE-Play/) | **Home of the Entity Play** — multi-surface SEO: classic ranking, AEO, GEO (`llms.txt`), schema entity graphs, E-E-A-T, freshness, authority triangles, and adversarial nemesis probes |

## Install

Copy or symlink a skill directory into your agent skills path, or install the packaged `.skill` file if your harness supports it.

```bash
# Claude Code / compatible harness example
ln -s "$(pwd)/HOTE-Play" ~/.claude/skills/HOTE-Play
```

## Package a skill

```bash
python3 path/to/skill-creator/scripts/package_skill.py ./HOTE-Play ./dist
```

## License

Unless noted otherwise in a skill folder, content is available for use with AI coding agents. Attribution appreciated.
