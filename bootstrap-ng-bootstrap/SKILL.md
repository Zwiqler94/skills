---
name: bootstrap-ng-bootstrap
description: "Use Bootstrap 5 utilities/Sass theming and ng-bootstrap widgets in this repo's Angular apps. Trigger when doing layout/spacing/typography/forms/tables styling, or when adding interactive UI like modals, accordions, tooltips, popovers, datepickers. Enforce repo standards: prefer Firenet components over raw HTML, utilities-first styling, accessibility, and compatibility checks between Angular/ng-bootstrap/Bootstrap."
---

# Bootstrap + ng-bootstrap (Angular)

## Core rules (non-negotiable)
- Prefer Firenet components over raw HTML elements; check `projects/firenet-core-components/src/public-api.ts` for available components.
- Use Bootstrap utility classes before adding custom SCSS; keep any custom styles scoped to the component/feature.
- Do not load `bootstrap.bundle.js` or rely on `data-bs-*` behaviors in Angular; use ng-bootstrap for interactivity.
- Ensure accessibility: labels, `aria-*` as needed, keyboard navigation, focus visibility, and focus return after modal close.
- Keep code clean: no dead/commented code; add JSDoc for non-trivial logic per repo standards.

## Compatibility workflow
1. Read `package.json` for the Angular major version (`@angular/core`).
2. Use `references/compatibility.md` to verify the matching ng-bootstrap major and required Bootstrap CSS version.
3. If tooltips/popovers are used, ensure Popper version matches the ng-bootstrap guidance.

## Practical patterns
- Layout/spacing: use grid and utilities (`d-flex`, `gap-*`, `align-items-*`, `justify-content-*`, `m*`, `p*`, responsive utilities).
- Buttons/inputs: use Firenet button/input components first; pass Bootstrap classes if supported; otherwise wrap with utility-class containers.
- Modals/tooltips/popovers/datepicker: use ng-bootstrap components/services; ensure proper `aria-labelledby`/`aria-describedby` where applicable and focus management.

## Imports
- Import only required ng-bootstrap modules/components (or standalone imports per repo patterns) to keep bundle size small.

## Troubleshooting (quick checks)
- UI looks off: check duplicate Bootstrap CSS imports or conflicting global styles.
- Tooltip/popover positioning: verify Popper is present and version-matched.
- Modal behind backdrop: inspect stacking context and parent z-index/position.

## References
- Compatibility mapping and upgrade checklist: `references/compatibility.md`.
- Official links (Bootstrap/ng-bootstrap/Agent Skills spec): `references/links.md`.
- Decision tree (Firenet vs ng-bootstrap): `references/firenet-vs-ngb.md`.
- Standards overlay (repo rules take priority): `references/standards-overlay.md`.
