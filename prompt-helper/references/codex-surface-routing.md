# Codex Surface Routing

Use the smallest durable surface that matches the scope.

## Surface Map

- Prompt/thread: use for one-off constraints, temporary task scope, and local
  acceptance criteria. Avoid durable behavior that should survive future
  sessions.
- `AGENTS.md`: use for compact always-on repo or personal rules, commands,
  review expectations, and repeated mistakes. Avoid long checklists,
  task-specific workflows, and stale model tables.
- Skill: use for reusable workflows, routing checklists, references, scripts,
  and domain procedures. Avoid facts that must be verified live or one-time
  task preferences.
- MCP/app connector: use for live external docs, private workspaces,
  browser/devtools, issue trackers, and authorized tools. Avoid static policy
  or local repo truth that can be read from files.
- Subagent: use for bounded parallel exploration, docs verification,
  architecture/test/final review. Avoid tiny tasks, unclear write ownership, and
  broad unbounded delegation.
- Config: use for sandbox, approvals, MCP servers, model/reasoning defaults,
  and tool availability. Avoid codebase conventions or workflow prose.
- Memory: use for stable user preferences and prior lessons to re-check. Avoid
  current facts, secrets, policy, or raw transcript truth.
- Hook: use for mechanical enforcement around tool calls or commands. Avoid
  nuanced engineering judgment.

Rules:

- Prefer local repo truth before memory for code behavior.
- Use `openai-docs` before Codex/OpenAI product claims.
- Keep global guidance small; move reusable task details into skills.
- Put repo-specific rules in the closest relevant `AGENTS.md`.
