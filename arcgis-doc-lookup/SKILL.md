---
name: arcgis-doc-lookup
description: >-
  Use when Codex needs official ArcGIS documentation links and implementation
  takeaways for ArcGIS Maps SDK for JavaScript, ArcGIS REST API, ArcGIS REST
  JS, ArcGIS Maps SDK components, or ArcGIS Online/Enterprise auth/items.
  Detect the app's ArcGIS SDK/package version when local files are available,
  then return 3-6 official references, version context, and concise
  implementation notes.
---

# ArcGIS Doc Lookup

## Metadata

- Author: Jacob Zwickler
- Version: 1.0.0
- Updated: 2026-07-08
- License: MIT

## Goal

Return grounded, official ArcGIS references for a question, plus concise
implementation notes.

## References

- ArcGIS doc quicklinks: `references/arcgis-doc-quicklinks.md` for fast
  official links.
- Search playbook: `references/search-playbook.md` for consistent,
  high-signal queries.

## Source Policy

1. Prefer Esri official docs on developers.arcgis.com: API reference, guides,
   samples, REST docs, auth, and portal docs.
2. Use Esri official GitHub repos for implementation templates, sample app
   structure, tooling, and REST JS source/examples.
3. Add Esri release notes or breaking changes when behavior or version risk is
   likely.
4. Use Esri official blogs only when docs are unclear.

Avoid community posts unless the user explicitly asks.

## Workflow

1. Restate the question in 1 sentence.
2. Identify the surface area. If ambiguous, ask exactly one clarifying question
   and wait.
   - ArcGIS Maps SDK for JavaScript
   - ArcGIS Maps SDK components
   - ArcGIS REST API (services, identify/query, geocoding, routing, etc.)
   - ArcGIS REST JS
   - ArcGIS Online / Enterprise (portals, items, OAuth, API keys, tokens)
3. Detect the local ArcGIS version before choosing docs when project files are
   available:
   - inspect `package.json` and lockfiles for `@arcgis/core`,
     `@arcgis/map-components`, `arcgis-js-api`, `esri-loader`, and
     `@esri/arcgis-rest-*` packages
   - inspect HTML/script tags, bundler config, and import paths for CDN or
     vendored ArcGIS versions
   - if several apps/packages exist, map the version per app and use the one
     tied to the user's target
   - if the version cannot be found, use current/latest docs and label that
     fallback in `Version context`
4. Select the doc track and search strategy. Prefer live web search when
   available; use the search playbook.
5. Fetch 3-6 references:
   - 1-2 API reference pages (exact class/function/module)
   - 1 guide page if concept-heavy
   - 1 sample page if it demonstrates the pattern
   - 1 official GitHub resource when repo/template/source context helps
   - release notes / breaking changes if relevant
6. Output contract with these exact section titles:
   - Best references (bullets with links)
   - Key takeaways (3-6 bullets)
   - Implementation notes (2-5 bullets, practical)
   - Version context (detected version, docs track, and fallback if any)
7. If no official source supports a claim, label it `UNVERIFIED` and stop
   guessing.

## Style

- Concise, code-oriented.
- Prefer ESM/module identifiers when applicable.
- Label product/version assumptions clearly.
