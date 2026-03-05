# Decision tree: Firenet first, ng-bootstrap second

Goal: consistent UI and minimal surprise.

Step 0: Check Firenet inventory
- Look for an existing component first: projects/firenet-core-components/src/public-api.ts

If a Firenet component exists:
- Use it.
- Wrap it with Bootstrap utilities for layout/spacing if needed.
- Do not replace it with raw HTML or ng-bootstrap.

If no Firenet component exists, decide:

A) Styling/Layout only?
- Use Bootstrap CSS utilities and class-based components.
- Do NOT introduce ng-bootstrap.
Examples:
- spacing/alignment, grid, typography, tables, badges, alerts, cards

B) Interactive behavior needed?
- Use ng-bootstrap (if already installed).
- If not installed, do not add it unless the task explicitly permits new dependencies.
Examples:
- modal, accordion, tooltip, popover, typeahead, datepicker, pagination

C) Bootstrap JS plugin temptation?
- Do not do it.
- Bootstrap docs explicitly warn their JS is not fully compatible with frameworks like Angular.
- Use ng-bootstrap instead for Angular-native behavior.

Tie-breakers:
- Prefer the smallest change that matches existing repo patterns.
- Prefer accessibility-safe components (Firenet/ng-bootstrap over div soup).
