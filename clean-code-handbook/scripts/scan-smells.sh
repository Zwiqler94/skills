#!/usr/bin/env bash
set -euo pipefail

# Very light “smell scan” for TS/JS repos.
# This is not a lint replacement. It is a review starting point.

ROOT="${1:-.}"

PATTERN='TODO|FIXME|HACK|XXX|console\.log|console\.debug|@\s*ts-ignore|@\s*ts-nocheck|@\s*ts-expect-error|return\s+null|==\s*null|!=\s*null|\bnull\b\s*\)|\)\s*\.\s*\w+\(|\)\s*\.\s*\w+\(\)\s*\.\s*\w+\(|\bboolean\b\s+\w+'

if command -v rg >/dev/null 2>&1; then
  rg -n --hidden --glob '!**/node_modules/**' --glob '!**/dist/**' \
    --glob '*.ts' --glob '*.tsx' --glob '*.js' --glob '*.jsx' \
    "$PATTERN" "$ROOT" || true
  exit 0
fi

grep -RIn --exclude-dir=node_modules --exclude-dir=dist \
  --include='*.ts' --include='*.tsx' --include='*.js' --include='*.jsx' \
  -E "$PATTERN" "$ROOT" || true
