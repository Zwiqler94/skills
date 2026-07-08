---
name: prompt-helper
description: >-
  Compact Codex code-practice router for scoped, evidence-grounded work. Use
  for reviewer-friction prevention, shared ownership checks, first-party mocks,
  test infrastructure, async UI/map readiness, contract/consumer/rollout gates,
  Codex/OpenAI docs-surface routing, optional memory-aware personalization,
  bounded subagent planning, scoped explore/plan/edit/review workflows, and
  receipt outputs.
---

# Prompt Helper

## Metadata

- Author: Jacob Zwickler
- Version: 2.1.0
- Updated: 2026-07-08
- License: MIT
- Scope: Reusable Codex code-practice router.

Use this skill to keep coding work small, grounded, and routed to the right
Codex surface. Prefer the user's explicit instructions and the nearest
`AGENTS.md` over this skill when they conflict.

## Core Rules

- Stay inside the requested scope. If the right fix requires broader scope,
  pause and name the tradeoff.
- Prefer the shortest correct maintainable change in the right ownership layer.
- Reuse existing primitives before adding helpers, abstractions, fallbacks, or
  manual sync code.
- Do not change public contracts, UX, dependencies, or rollout scope unless
  explicitly approved.
- Treat the first failing file as a symptom, not proof of ownership.
- End substantial work with a receipt: what changed, where, validation, and
  real risks.

## Source Routing

- For current OpenAI, Codex, model, skill, MCP, plugin, subagent, or config
  behavior, use `openai-docs` first. Do not use this skill as source of truth
  for Codex product facts.
- For framework, SDK, CLI, or cloud-service claims, prefer the most official
  available docs source with repo/version context when available, such as a
  dedicated skill, MCP, or Context7.
- For repo behavior, verify local files, scripts, package manifests, tests, and
  call sites before relying on memory or stale docs.

## Personalization

Stay generic by default. Treat personalization as an optional local overlay, not
as policy baked into this public skill.

- Resolve `${CODEX_HOME:-$HOME/.codex}` only when local shell context is
  available.
- If the installed copy has `references/personalization.local.md`, read it only
  when the task benefits from local preferences, surface quirks, or prior
  decisions.
- If no local personalization file exists and the user invokes `$prompt-helper`
  for setup or a first substantial coding workflow, ask once whether to continue
  generic or personalize from `assets/personalization-template.md`. If the user
  ignores the prompt, continue generic.
- If `${CODEX_HOME:-$HOME/.codex}/memories/MEMORY.md` exists, use it only as
  optional context for stable preferences, project routing, or prior lessons.
  Search narrowly, avoid broad transcript scans, and verify current facts from
  local files or official docs.
- Do not treat memory as policy, source of current truth, or a place to expose
  secrets.
- If the `subagent-council` skill is installed, read it before routing broad
  subagent planning. If its custom agent files are missing and the task would
  benefit, offer a separate install/refresh step; never auto-install them from
  this skill.
- If `subagent-council` is missing, offer separate create/install help only
  when the user wants that workflow.

## References

Load only the reference needed for the task:

- `references/codex-surface-routing.md`: use when deciding whether guidance
  belongs in a prompt, `AGENTS.md`, skill, MCP, subagent, config, memory, or
  hook.
- `references/reviewer-friction.toon`: use for shared ownership, app-local
  glue, first-party mocks, async/map readiness, canonical tooling, or
  review-comment prevention.
- `references/subagent-council.toon`: use for generic companion-skill checks
  when the user asks for subagents or parallel agents. Do not treat it as the
  current council roster; read the installed `subagent-council` skill when
  available.

## TOON Maintenance

When editing `.toon` reference files, prefer the official TOON CLI for
conversion and validation instead of hand-validating syntax.

- Encode JSON to TOON without installing globally:

  ```bash
  npx @toon-format/cli input.json -o output.toon
  ```

- Decode or validate existing TOON with the same no-install path:

  ```bash
  npx @toon-format/cli data.toon -o output.json
  ```

- Keep strict decoding as the default. Use `--no-strict` only when deliberately
  diagnosing legacy or malformed TOON.
- For model-generated TOON, show the expected `key[N]{fields}:` header, use
  two-space indentation, avoid trailing spaces, and keep `[N]` matched to the
  row count.

## Prompt Assets

Use assets only when the user asks for a pasteable prompt or template:

- `assets/mode-banner.md`: compact Plan-mode-aware task header.
- `assets/personalization-template.md`: optional local overlay template.
- `assets/prompt-only-template.md`: read-only `/plan` starter. Do not treat it
  as a custom prompt file.

## Default Workflow

1. Explore just enough to find ownership, existing patterns, and validation
   commands.
2. If the implementation shape is unclear or risky, produce a compact plan
   before editing.
3. If the shape is clear and edits are allowed, make the smallest viable
   change.
4. Run the smallest relevant validation first; broaden only when risk
   justifies it.
5. Summarize blockers honestly, including baseline failures or validation that
   could not run.

## Subagent Discipline

- Stay single-agent for tiny, obvious, or write-heavy tasks.
- Propose subagents only for independent, parallel-friendly work where noise
  would pollute the main thread.
- Prefer read-only subagents for first-wave mapping, docs verification,
  architecture review, test-gap scans, and final review.
- Do not spawn implementation agents in parallel with reviewers unless the user
  explicitly asks for that workflow.
- Consolidate subagent results into decisions, evidence, and next steps; do not
  dump raw logs.
