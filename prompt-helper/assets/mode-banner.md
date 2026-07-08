# Plan-Aware Task Header

Use this when the user asks for a pasteable prompt header.

```md
$prompt-helper

Lane: PLAN ONLY | EXECUTE
Goal:
Scope:
Constraints:

- No new dependencies unless approved.
- No public contract or rollout expansion unless approved.
- Keep the diff surgical; avoid formatting churn.

Plan-mode note:

- Prefer Codex Plan mode (`/plan`; Shift+Tab where available) for
  planning-only work.
- If `/plan` is unavailable because work is already running, state
  `PLAN ONLY` or `NO EDITS`.

Validation:

- Smallest relevant checks:

Receipt:

- What changed / where / validation / risks
```
