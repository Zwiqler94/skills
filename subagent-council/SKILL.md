---
name: subagent-council
description: Use for Jake's personal development tasks when Codex should install, refresh, or route a compact custom subagent council. Installs memory-aware Codex custom subagents from bundled templates into ~/.codex/agents and teaches the parent agent when to delegate to repo mapping, architecture, docs verification, implementation, testing, API contract, security, accessibility, performance, documentation, release, and final-review specialists. Avoid for tiny one-file edits unless Jake asks for the council.
---
<!-- markdownlint-disable MD013 -->

# Subagent Council

Use this skill as the parent-agent playbook for Jake's personal development
subagent council. Keep the council compact, explicit, and scoped to the current
task.

## Hard Boundaries

- Do not edit Codex memories.
- Do not treat Codex memory as policy.
- Keep durable repo rules in `AGENTS.md` or checked-in docs.
- Keep this as one compact skill.
- Do not install or spawn the full council by default.
- Prefer the smallest useful council.
- Do not attach MCP servers or external tools to templates unless Jake asks.
- Do not install bundled agents unless the user asks to install or refresh them.

## Install Or Refresh Subagents

Preview the recommended set:

```sh
bash scripts/install-subagents.sh --recommended --model-profile gpt-5.6 --dry-run --explain
```

Install the recommended set:

```sh
bash scripts/install-subagents.sh --recommended --model-profile gpt-5.6 --backup --force
```

Install all bundled agents:

```sh
bash scripts/install-subagents.sh --all --backup --force
```

Refresh only bundled agents already installed in the target:

```sh
bash scripts/install-subagents.sh --installed --model-profile gpt-5.6 --dry-run --explain
bash scripts/install-subagents.sh --installed --model-profile gpt-5.6 --backup --force
```

List bundled agents:

```sh
bash scripts/install-subagents.sh --list
```

List model profiles:

```sh
bash scripts/install-subagents.sh --list-model-profiles
```

The installer scans `~/.codex/memories` read-only, emits only category labels,
and copies selected TOML templates into `~/.codex/agents`. It must not quote raw
memory content or mutate memory files.

## Model Profiles

`gpt-5.6` is the default role-optimized profile. It renders explicit
`gpt-5.6-luna`, `gpt-5.6-terra`, or `gpt-5.6-sol` model settings with each
role's configured reasoning effort.

`inherit` omits `model` so Codex uses the parent-session model while retaining
role-specific reasoning effort.

Use `--installed` only for an explicit refresh. It selects recognized bundled
TOMLs already present in the target, never deletes files, and leaves unrelated
custom agents untouched. `--explain` prints the selected profile and each
agent's rendered model and effort.

## Bundled Subagents

| Subagent | Default | Sandbox | Use For |
| --- | --- | --- | --- |
| `repo_cartographer` | yes | read-only | Repo structure, scripts, commands, instructions, ownership |
| `implementation_surgeon` | yes | workspace-write | Small targeted patches after behavior is understood |
| `test_sentinel` | yes | workspace-write | Focused regression tests and narrow test repair |
| `final_reviewer` | yes | read-only | Owner-style final diff review |
| `docs_oracle` | memory-selected | read-only | Official-doc checks for APIs, SDKs, CLIs, frameworks |
| `product_architect` | memory-selected | read-only | Scope, MVP, architecture, migration tradeoffs |
| `api_contract_keeper` | memory-selected | read-only | Routes, schemas, env/config, persistence, compatibility |
| `security_privacy_guardian` | memory-selected | read-only | Auth, secrets, logs, storage, privacy |
| `ux_accessibility_reviewer` | memory-selected | read-only | UI behavior, copy, focus, keyboard, semantics |
| `performance_dx_reviewer` | memory-selected | read-only | Runtime performance, build friction, tests, local DX |
| `docs_writer` | memory-selected | workspace-write | README, setup docs, ADRs, changelogs, migration notes |
| `release_captain` | memory-selected | read-only | PR/release readiness, versions, rollback, validation |

## Routing Rules

Use no subagent for tiny, obvious edits where the owner files and expected
behavior are already clear.

Use `repo_cartographer` when the repo, owner files, scripts, or validation
commands are unclear. Ask it to identify active instructions, package manager,
entry points, test setup, CI config, env examples, likely owner files, and
smallest validation commands. Stay read-only.

Use `repo_cartographer` plus `product_architect` for fuzzy feature requests or
design decisions. Let the parent synthesize the bounded plan before any
implementation agent runs.

Use `docs_oracle` for version-sensitive behavior involving Angular, TypeScript,
Node, npm, Firebase, OpenAI, browser APIs, SDKs, CLIs, or Codex behavior. Prefer
official docs and mark unresolved claims as `Unverified`.

Use `implementation_surgeon` only when target files and desired behavior are
clear, with no unresolved API contract, security, privacy, UI, or docs-research
risk.

Use this default bug-fix council:

```text
repo_cartographer
test_sentinel
implementation_surgeon
final_reviewer
```

Prefer a focused failing regression test before the fix when practical.

Use this default API/schema/config/persistence council:

```text
repo_cartographer
api_contract_keeper
test_sentinel
implementation_surgeon
final_reviewer
```

Do not implement until request/response shape, schema impact, env/config
contracts, migration risk, rollback risk, and test targets are understood.

Use `security_privacy_guardian` for auth, secrets, logging, storage, uploads,
or user data. Add `api_contract_keeper` when request/response, schema,
persistence, or config changes are involved.

Use `ux_accessibility_reviewer` for UI behavior or accessibility. Review
keyboard flow, focus management, labels, semantics, forms, dialogs, copy, error
states, and screen-reader risk.

Use `performance_dx_reviewer` for performance or developer-experience issues.
Measure before optimizing, or propose a lightweight benchmark or trace.

Use `docs_writer` for documentation updates. Add `docs_oracle` when docs mention
APIs, CLI flags, framework behavior, SDK behavior, or version-specific details.

Use `release_captain` plus `final_reviewer` for PR or release readiness. Add
specialists only for touched risk areas.

## Spawn Limits

- Use at most three subagents in the first wave unless Jake asks for broad
  review.
- Start read-only when owner files or behavior are unclear.
- Use `final_reviewer` only after a concrete plan or diff exists.
- Do not spawn `implementation_surgeon` in parallel with reviewers.
- Do not allow child subagents to spawn deeper child agents unless requested.
- Do not spawn the full council for tiny edits.

## Receipt Format

End council runs with:

```md
## Summary
## Subagents used
## Files touched
## Tests run
## Manual validation
## Risks
## Next action
```

If no files changed, write `Files touched: none.`

## Maintenance Notes

- Remove installed agent files from `~/.codex/agents` to uninstall agents.
- Remove `~/.agents/skills/subagent-council` and
  `~/.codex/skills/subagent-council` to uninstall the skill.
- Re-run `scripts/install-subagents.sh --installed --model-profile gpt-5.6`
  with `--dry-run --explain` before refreshing installed templates.
- Validate with `scripts/install-subagents.sh --list`,
  `scripts/install-subagents.sh --list-model-profiles`,
  `python3 scripts/test-install-subagents.py`,
  `python3 -m py_compile scripts/install-subagents.py`, and the `skill-creator`
  quick validator.
