# Sonar / Lint Playbook: Google TS Style

This file maps common lint findings to Google-style fixes.
It is meant for “fix the warning without refactoring the universe”.

---

## Types
### “Use interface instead of type”
Use `interface` for object shapes. Keep `type` for unions, tuples, mapped/conditional types.

### “Prefer optional over undefined union”
Convert `foo: T | undefined` to `foo?: T` when semantics match “may be absent”.

### “Avoid any”
Prefer `unknown` for unknown values, then narrow with type guards.
If `any` is intentional (tests, partial mocks), document why and locally suppress the rule.

---

## JSDoc
### “JSDoc @param/@return types are redundant”
Remove the `{Type}` portion and keep the description if it adds meaning.
Avoid `@typedef` in `.ts`.

### “JSDoc list formatting”
Convert plain text bullets into Markdown `-` lists.

---

## Modules
### “Avoid default exports”
Switch to named exports and update imports accordingly.

### “Avoid namespaces / require”
Use ES imports and module boundaries instead of `namespace` or `import x = require(...)`.

---

## Correctness and safety
### “Use ===”
Replace `==` with `===` except `x == null` for null-or-undefined checks.

### “Throw Error objects”
Replace `throw 'msg'` and `Promise.reject('msg')` with `new Error('msg')` or an `Error` subclass.

### “Avoid const enum”
Replace `const enum` with `enum`.

### “Do not rely on ASI”
Add missing semicolons and avoid ASI-sensitive patterns.

---

## Minimal patch strategy
- Fix one bucket at a time.
- Avoid renaming public APIs unless required.
- If a fix requires bigger redesign (like `any` everywhere), propose a staged plan instead of doing it in one patch.
