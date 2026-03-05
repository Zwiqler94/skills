---
name: google-typescript-style-guide
description: "Enforce the Google TypeScript Style Guide in code reviews and edits: modules and exports (no default exports, no namespaces), language features (const/let, no var, no ASI, no const enum), safe control flow and errors (===, switch default, throw Error), type system conventions (interface vs type, unknown over any, assertions), and JSDoc (Markdown, no redundant type tags). Use when fixing ESLint/Sonar findings or standardizing a TS codebase."
license: "CC-BY-4.0 (this skill text is an original summary; source guide linked)"
metadata:
  author: jake-arbor
  version: "1.1.0"
  created: "2026-02-25"
  source: "https://google.github.io/styleguide/tsguide.html"
---

# Skill: Google TypeScript Style Guide

## Assumption
This skill is for **TypeScript source** (`.ts`, `.tsx`) and is applied as **a minimal-diff style and safety pass**. If your repo intentionally deviates from Google style, follow repo rules and note the exception.

## Compatibility
Use for TypeScript projects using ES modules. Optional scripts use Bash and either `rg` (ripgrep) or `grep`.

## When to activate
Activate when the user asks for:
- “Google TS style” alignment or a review using that guide
- Lint or Sonar findings about TypeScript conventions
- Questions about JSDoc in TS, exports, imports, `interface` vs `type`, `any`, assertions, decorators, or error handling

## Outputs
When applying this skill, produce:
1) **Findings** grouped by section (Exports, Imports, Language features, Types, JSDoc, etc.)
2) **Recommended fixes** as a minimal patch (or small snippet if no repo access)
3) **Risk notes** for anything that could be behavior-changing
4) A short **review checklist** for the author

---

## Workflow (do this in order)
### 1) File and module structure
- Ensure ES module usage. Avoid TypeScript namespaces and `require` style imports.
- Prefer named exports over default exports.
- Avoid mutable exports (`export let` style).

If you need deeper guidance: see `references/REFERENCE.md`.

### 2) Language feature safety pass
- Prefer `const` and `let`. Never `var`.
- Do not rely on Automatic Semicolon Insertion. End statements with semicolons.
- Avoid disallowed features: `const enum`, `with`, `debugger`, `eval`, `Function(string)`, modifying builtins.

### 3) Control flow correctness
- Use `===` / `!==` for equality. Exception: `x == null` is allowed to match `null` or `undefined`.
- Switch: always include `default` and keep it last. No fallthrough in non-empty cases.
- Iteration: prefer `for...of` for arrays. `for...in` only for dict-style objects and must filter with `hasOwnProperty` or use `Object.keys/values/entries`.

### 4) Errors and exceptions
- Throw and reject **only** `Error` (or subclasses). No throwing strings.
- Keep `try` blocks tight to what can throw.
- Prefer `catch (e: unknown)` and narrow before use.

### 5) Type system conventions
- Prefer `interface` over object-literal `type` aliases for data shapes.
- Use `type` for unions, tuples, mapped and conditional types, and utility compositions.
- Prefer optional properties and params (`?`) over `| undefined` in most cases.
- Prefer `unknown` over `any` when the value is genuinely unknown.
- Type assertions use `as` syntax. For object literals, prefer `: Foo` annotations over `as Foo`.

### 6) JSDoc and comments
- JSDoc is for API documentation and meaning, written in **Markdown**.
- Avoid JSDoc type declarations in TS (`@param {Type}`, `@return {Type}`, `@typedef`).
- Use `//` for multi-line non-JSDoc comments, not `/* */`.
- For parameter properties in constructors, document them with `@param` descriptions.

---

## Common fix recipes (copy-paste level)
### Sonar: “Use interface instead of type”
Convert:
```ts
type User = {
  id: string;
  name: string;
};
```
To:
```ts
interface User {
  id: string;
  name: string;
}
```

### JSDoc: “Do not declare types in @param”
Convert:
```ts
/**
 * @param {User} user
 */
function save(user: User) {}
```
To:
```ts
/**
 * Persists a user. Throws if the user is soft-deleted.
 * @param user User to persist.
 */
function save(user: User) {}
```

### Object literal typing: prefer annotation over assertion
Convert:
```ts
const u = {id: '1', nm: 'Jake'} as User;
```
To:
```ts
const u: User = {id: '1', nm: 'Jake'}; // now nm is a type error
```

### Promise rejection: reject Errors
Convert:
```ts
return Promise.reject('nope');
```
To:
```ts
return Promise.reject(new Error('nope'));
```

### Avoid boolean coercion in conditionals
Convert:
```ts
if (!!value) { ... }
```
To:
```ts
if (value) { ... }
```

---

## Optional: Quick scans (scripts)
If your agent can run shell commands, use these helpers:
- `scripts/scan-jsdoc-types.sh` finds JSDoc type tags inside `.ts/.tsx`
- `scripts/scan-module-anti-patterns.sh` finds default exports, namespaces, const enums, and ts-ignore usage

---

## Minimal review checklist
- [ ] No default exports, no namespaces, no mutable exports
- [ ] `const`/`let` only, no `var`, statements end with semicolons
- [ ] `===`/`!==` used (except `x == null` pattern)
- [ ] switch has `default` last, no case fallthrough
- [ ] throws and Promise rejects only `Error`
- [ ] `unknown` preferred over `any` for unknown values
- [ ] object shapes use `interface`
- [ ] JSDoc adds meaning and uses Markdown lists; no JSDoc type declarations

See `references/REFERENCE.md` for the full section map.
