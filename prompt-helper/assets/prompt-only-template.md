# Plan-Only Prompt Template

Use this for one-off read-only planning prompts.

```md
/plan Use $prompt-helper to prepare a short implementation plan.

Goal:
<one sentence>

Scope:
<bounded folders, repos, files, or TBD>

Constraints:

- No edits.
- No new dependencies unless approved.
- No public contract or rollout expansion unless approved.
- Prefer existing shared primitives over app-local glue.

Please inspect only enough context to identify ownership, contracts, rollout,
reviewer-friction triggers, and the smallest useful validation path. End with
3-5 steps, assumptions, at most one blocking question, and the next smallest
edit set.

If `/plan` is unavailable, use this as a normal prompt and treat it as
PLAN ONLY / NO EDITS. This is a pasteable one-off prompt, not a custom prompt
file.
```
