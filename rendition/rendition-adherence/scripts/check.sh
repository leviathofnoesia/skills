#!/usr/bin/env bash
# Rendition design-system adherence lint.
#
# The shipped config (assets/_adherence.oxlintrc.json) is ESLint-shaped: it uses
# no-restricted-syntax (ESLint-only) to catch raw hex / raw px / banned font-family
# literals. It validates under ESLint, not oxlint. This runner loads ESLint (installed
# locally in node_modules) and uses a thin wrapper config that pulls the rules from the
# shipped file and adds module parser options (so `const`, JSX, TS parse cleanly).
#
# Rules are "warn", not "error", so CI can gate on the warnings.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="$SKILL_DIR/assets/_adherence.oxlintrc.json"
ESLINT="$SKILL_DIR/node_modules/.bin/eslint"

if [[ ! -x "$ESLINT" ]]; then
  echo "rendition-adherence: eslint not found at $ESLINT" >&2
  echo "Install it with: npm install --prefix \"$SKILL_DIR\" eslint@^8 eslint-plugin-react eslint-plugin-import" >&2
  exit 1
fi

# Wrapper config: reuse the shipped rules, add parser options for modern syntax.
# Must live inside the skill dir so ESLint resolves node_modules plugins from there.
WRAPPER="$SKILL_DIR/.adherence-wrapper.json"
cat > "$WRAPPER" <<JSON
{
  "root": true,
  "extends": ["$CONFIG"],
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "ecmaFeatures": { "jsx": true }
  }
}
JSON

trap 'rm -f "$WRAPPER"' EXIT
exec "$ESLINT" -c "$WRAPPER" --no-eslintrc "${@:-.}"
