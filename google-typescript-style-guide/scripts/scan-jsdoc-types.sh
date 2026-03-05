#!/usr/bin/env bash
set -euo pipefail

# Finds JSDoc type declarations in TypeScript files:
# - @param {Type}
# - @return {Type}
# - @typedef
#
# Exits non-zero if any matches are found.

ROOT="${1:-.}"

if command -v rg >/dev/null 2>&1; then
  rg -n --hidden --glob '!**/node_modules/**' --glob '*.ts' --glob '*.tsx'     '@param\s*\{[^}]+\}|@return\s*\{[^}]+\}|@typedef' "$ROOT" && exit 1 || exit 0
fi

# Fallback to grep
grep -RIn --exclude-dir=node_modules --include='*.ts' --include='*.tsx' -E   '@param[[:space:]]*\{[^}]+\}|@return[[:space:]]*\{[^}]+\}|@typedef' "$ROOT" && exit 1 || exit 0
