#!/usr/bin/env bash
set -euo pipefail

# Scans for common Google-style module and toolchain anti-patterns:
# - default exports
# - namespace usage
# - const enum
# - ts-ignore / ts-nocheck / ts-expect-error
#
# Exits non-zero if any matches are found.

ROOT="${1:-.}"

PATTERN='export[[:space:]]+default|\bnamespace\b|\bconst[[:space:]]+enum\b|@ts-ignore|@ts-nocheck|@ts-expect-error'

if command -v rg >/dev/null 2>&1; then
  rg -n --hidden --glob '!**/node_modules/**' --glob '*.ts' --glob '*.tsx' "$PATTERN" "$ROOT" && exit 1 || exit 0
fi

grep -RIn --exclude-dir=node_modules --include='*.ts' --include='*.tsx' -E "$PATTERN" "$ROOT" && exit 1 || exit 0
