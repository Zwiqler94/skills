# Standards overlay for this skill (must not conflict)

Unless otherwise specified by the user: this skill is subordinate to the repo standards files.
If anything conflicts, the repo standards win, and call out the conflict with a warning.

Enforced priorities:
1) PROJECT_STANDARDS.md is the source of truth for UI component choices and repo conventions.
2) CODING_STANDARDS.md is the source of truth for code hygiene and accessibility expectations.
3) This skill provides Bootstrap + ng-bootstrap guidance only within those constraints.

Hard constraints this skill will enforce:
- Firenet components first when available.
- Bootstrap utility classes before writing custom SCSS.
- No Bootstrap JS bundle behaviors in Angular. Prefer ng-bootstrap for interactivity.
- Keep changes minimal, local, and consistent with existing project patterns.
- Maintain accessibility: labels, keyboard/focus behavior, aria where needed.

Dependency changes:
- This skill does not grant permission to add/upgrade dependencies.
- Only change dependencies if the task prompt explicitly allows it (ex: ALLOW_NEW_DEPENDENCIES).

Testing and structure:
- Follow the repo's rules for file structure and tests (component/service/test expectations).
- Do not introduce new patterns that violate the repo's conventions.
