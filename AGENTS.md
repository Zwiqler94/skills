# AGENTS.md

These instructions apply to the entire repository unless a deeper
`AGENTS.md` overrides them.

## Scope and intent

- Make focused, minimal edits.
- Prefer updating existing skill files over adding new tooling.
- Do only what the user requested.

## Repository conventions

- Each skill should have a single `SKILL.md` as the source of truth.
- Keep helper content in standard folders when needed:
  - `references/`
  - `assets/`
  - `scripts/`
  - `agents/`
- Avoid duplicating guidance across multiple files unless required by tooling.

## Editing guidance

- Preserve existing tone and structure within each skill folder.
- Keep instructions concrete and action-oriented.
- Do not add dependencies unless explicitly requested.
- Use `rg` / `rg --files` for search and discovery.

## Validation

- Run the smallest relevant checks for changed files.
- If a script exists for the changed skill, prefer that script over
  inventing new checks.
- If no checks exist, state that clearly in your final summary.

## Safety

- Never run destructive git commands unless explicitly requested.
- Do not revert unrelated local changes.
- If you detect unexpected modifications you did not make, stop and ask
  the user how to proceed.
