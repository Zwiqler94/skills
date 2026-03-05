---
name: arcgis-doc-lookup
description: Use when you need official ArcGIS documentation links and implementation takeaways for any ArcGIS API question (Maps SDK for JavaScript 4.x, ArcGIS REST API, or ArcGIS Online/Enterprise auth/items). Return 3-6 links, version context, and a short "what this means" summary.
license: MIT
allowed-tools:
  - web_search
metadata:
  short-description: ArcGIS docs lookup (official-first)
  compatibility: Requires web search access for developers.arcgis.com; no scripts required.
---

# Goal
Return grounded, official ArcGIS references for a question, plus concise implementation notes.

# References
- ArcGIS doc quicklinks: `references/arcgis-doc-quicklinks.md` (use for fast official links; update as needed)
- Search playbook: `references/search-playbook.md` (use for consistent, high-signal queries)

# Source policy (order)
1) Esri official docs on developers.arcgis.com (API reference, guides, samples)
2) Esri release notes / breaking changes when behavior or version risk is likely
3) Esri official blogs only when docs are unclear
Avoid community posts unless the user explicitly asks.

# Workflow
1) Restate the question in 1 sentence.
2) Identify the surface area (choose one; if ambiguous, ask exactly one clarifying question and wait):
   - ArcGIS Maps SDK for JavaScript (4.x)
   - ArcGIS REST API (services, identify/query, geocoding, routing, etc.)
   - ArcGIS Online / Enterprise (portals, items, OAuth, API keys, tokens)
3) Select the doc track and search strategy (prefer live web search when available; use the search playbook).
4) Fetch 3-6 references:
   - 1-2 API reference pages (exact class/function/module)
   - 1 guide page if concept-heavy
   - 1 sample page if it demonstrates the pattern
   - Release notes / breaking changes if relevant
5) Output contract (use these exact section titles):
   - Best references (bullets with links)
   - Key takeaways (3-6 bullets)
   - Implementation notes (2-5 bullets, practical)
   - Version context (what doc track/version was used)
6) If no official source supports a claim, label it UNVERIFIED and stop guessing.

# Style
- Concise, code-oriented.
- Prefer ESM/module identifiers when applicable.
- No fluff, no vibes.
