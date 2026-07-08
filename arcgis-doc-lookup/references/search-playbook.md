# ArcGIS Search Playbook

Use these query patterns to keep results high-signal and official-first.

## Version Discovery

Search local files before searching docs when a repo/workspace is available.

- `package.json`: `@arcgis/core`, `@arcgis/map-components`, `arcgis-js-api`,
  `esri-loader`, and `@esri/arcgis-rest-*`
- lockfiles: resolved versions in `package-lock.json`, `pnpm-lock.yaml`,
  `yarn.lock`, or `bun.lockb`
- app shells: CDN URLs, script tags, import maps, and vendored ArcGIS paths
- monorepos: determine which app/package the user is targeting before choosing
  a docs version

If no version is discoverable, use current/latest docs and state that fallback.

## ArcGIS Maps SDK for JavaScript

- `site:developers.arcgis.com/javascript/latest/api-reference <class-or-function>`
- `site:developers.arcgis.com/javascript/latest <guide-or-concept>`
- `site:developers.arcgis.com/javascript/latest/sample-code <pattern>`
- `site:developers.arcgis.com/javascript <version> <class-or-function>`
- `site:developers.arcgis.com/javascript release notes <version>`
- `site:github.com/Esri/jsapi-resources <framework-or-template>`

## ArcGIS REST API

- `site:developers.arcgis.com/rest <service-or-operation>`
- `site:developers.arcgis.com/rest api-reference <endpoint>`
- `site:developers.arcgis.com/rest guide <concept>`

## ArcGIS REST JS

- `site:developers.arcgis.com/arcgis-rest-js <package-or-method>`
- `site:github.com/Esri/arcgis-rest-js <package-or-method>`

## ArcGIS Online / Enterprise (portal, auth, items)

- `site:developers.arcgis.com documentation <portal-or-auth-topic>`
- `site:developers.arcgis.com authentication <oauth-or-api-key>`
- `site:developers.arcgis.com portal <items-or-sharing>`

## Selection rules

- Prefer API reference, guides, and samples for implementation.
- Prefer the docs track that matches the detected app/package version.
- Use current/latest only when no local version is available or the user asks
  for current docs.
- Prefer Esri GitHub repos only for official templates, source examples, and
  repo-level setup details.
- Add release notes when behavior might change across versions.
- Label anything unsupported by an official source as `UNVERIFIED`.
