# Reference: Google TypeScript Style Guide (Section Map)

Source of truth: https://google.github.io/styleguide/tsguide.html

This reference is intentionally a **condensed map** of the major sections and enforcement points.
It is designed for agents: identify the rule bucket, apply the minimal fix, and avoid drive-by refactors.

---

## Source file structure
- File order: copyright (if any), optional `@fileoverview`, imports, implementation.
- One blank line between sections.

## Imports and exports
### Imports
- Use ES module import forms. Avoid `require` and `/// <reference ...>`.
- Prefer relative imports within a project, and avoid deep `../../../` chains when possible.
- Named imports for frequently used symbols; namespace imports when using many exports from a large API.

### Exports
- Use named exports, avoid default exports.
- Minimize exported API surface.
- Avoid mutable exports (`export let`). If external mutability is needed, expose a getter.

### Type-only import/export
- `import type` is allowed when you only need the type and the toolchain requires it.
- Use `export type` when re-exporting a type for isolated transpilation setups.

---

## Language features
### Local variables
- Use `const` by default, `let` when reassignment is required. Never `var`.
- One variable per declaration.
- Do not use before declaration.

### Arrays
- Do not use `Array()` or `new Array()`.
- Do not add non-numeric properties to arrays.
- Spread: only spread iterables into arrays. Do not spread `null`/`undefined` or primitives.

### Objects
- Do not use `Object()` constructor.
- Avoid unfiltered `for...in`. Prefer `for...of Object.keys/values/entries`.
- Spread: only spread plain objects. Avoid spreading class instances or values with non-Object prototypes.
- Parameter destructuring must be shallow, simple, and default optional objects to `{}`.

### Classes
- No semicolon after class declarations or method declarations.
- Prefer field initializers.
- Do not add or remove properties after construction. If a field may be filled later, initialize to `undefined`.
- Properties accessed from outside the class lexical scope (example: Angular templates) must not be `private`.
- Getters must be pure (no observable side effects).
- Avoid computed properties except symbol keys.
- Visibility: never write `public` unless it is a non-readonly public parameter property.
- Do not manipulate `prototype` directly (framework exceptions may exist).

### Functions
- Prefer function declarations for named functions.
- Avoid function expressions, prefer arrow functions for callbacks.
- Use arrow concise bodies only when the return value is used. Otherwise use block body or `void`.
- Do not rely on implicit `this` binding. Prefer arrow functions for `this` capture.
- Beware higher-order function callback signatures (example: `array.map(parseInt)`).

### Decorators
- Do not define new decorators. Use framework-provided decorators only.
- Decorators must immediately precede what they decorate. No blank lines between.
- Put JSDoc before decorators.

### Disallowed features
- Do not rely on Automatic Semicolon Insertion, end statements with semicolons.
- No `const enum`.
- No `debugger`.
- No `with`.
- No `eval` or `Function(string)` (except code loaders).
- Do not modify builtins or their prototypes.

---

## Control flow and correctness
- Equality: use `===` and `!==`. Exception: `x == null` allowed for null-or-undefined check.
- Boolean coercion:
  - Do not use explicit coercion like `if (!!x)` in conditionals.
  - Do not coerce enum values to booleans. Compare explicitly.
- Switch: include `default` and keep it last. No fallthrough for non-empty cases.
- Exceptions:
  - Prefer throwing exceptions for exceptional cases.
  - Only throw and reject `Error` (or subclasses).
  - Keep try blocks tight. Prefer `catch (e: unknown)`.

---

## Type system
### Inference and annotations
- Omit annotations for trivial literals and `new` expressions.
- Add annotations for complex expressions where readability or error localization improves.
- Return types are optional by default, but may be requested for clarity.

### Null and undefined
- Either `null` or `undefined` is acceptable depending on surrounding APIs.
- Prefer optional `?` over `| undefined` for many properties and params.

### `interface` vs `type`
- Prefer `interface` for object shapes and contracts.
- Prefer `type` for unions, tuples, mapped and conditional types, and utility compositions.

### Assertions and `any`
- Assertions must use `as`.
- Avoid asserting object literals with `as Foo`. Prefer `: Foo` annotation so extra/mistyped fields surface.
- Prefer `unknown` over `any` for unknown values. Narrow before use.
- If `any` is used intentionally (tests, partial mocks), document why and locally suppress the lint.

### Wrapper types and tuples
- Use `string`, `number`, `boolean`, not `String`, `Number`, `Boolean`.
- Do not `new String/Number/Boolean`.
- Prefer tuple types over “Pair” interfaces unless property names add clarity.

### Generics
- Avoid return-type-only generics. If consuming such APIs, specify the generic explicitly.

### Toolchain
- Avoid `@ts-ignore`, `@ts-expect-error`, and `@ts-nocheck` in production code.
  - In tests, `@ts-expect-error` may be used sparingly with caution.

---

## Need fast mappings for lint tools?
See:
- `references/SONAR-PLAYBOOK.md`
- `references/REVIEW-CHECKLIST.md`
