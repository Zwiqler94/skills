# Prompt Helper Personalization Template

Copy or adapt this file to `references/personalization.local.md` in an
installed personal copy when local behavior should differ from the generic repo
skill. Keep it concise and avoid secrets.

## Local Surfaces

- CLI:
- IDE extension:
- Codex app:

## Memory Policy

- Use memory for:
- Do not use memory for:
- Verification rule:

## Companion Skills

- `subagent-council`:
- `subagent-council` custom agents:
- Documentation skills:
- Repo-specific skills:

## Preferred Receipts

- Default receipt shape:
- Extra validation notes:
- Manual validation preferences:

## Local Constraints

- Never assume:
- Ask before:
- Safe defaults:

## Sufficiency Checklist

- [ ] Local Surfaces names each Codex surface this install uses.
- [ ] Memory Policy says when memory helps, when not to use it, and how to
  verify drift-prone facts.
- [ ] Companion Skills records whether `subagent-council` is installed and
  whether custom agent TOMLs are installed under `${CODEX_HOME:-$HOME/.codex}`.
- [ ] Preferred Receipts gives a concrete default receipt shape.
- [ ] Local Constraints has no secrets and no public/global policy leakage.
