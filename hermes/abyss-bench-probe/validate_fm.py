import yaml
import sys

path = "C:/Users/billy/AppData/Local/hermes/profiles/kraken/skills/abyss-bench-probe/SKILL.md"

with open(path) as f:
    content = f.read()

parts = content.split("---")
if len(parts) >= 3:
    fm = parts[1]
    try:
        data = yaml.safe_load(fm)
        print("Valid YAML frontmatter:")
        for k, v in data.items():
            print(f"  {k}: {v}")
        print()
        print("name present:", "name" in data)
        print("description present:", "description" in data)
        print("Frontmatter is VALID")
    except yaml.YAMLError as e:
        print("YAML ERROR:", e)
        sys.exit(1)
else:
    print("No valid frontmatter found")
    sys.exit(1)
