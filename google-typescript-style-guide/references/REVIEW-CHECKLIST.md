# Review Checklist: Google TS Style

Use this as the final pass output in reviews.

## Modules and structure
- [ ] ES modules only (no namespaces, no require, no reference directives)
- [ ] No default exports
- [ ] No mutable exports (`export let`)

## Language features
- [ ] `const` by default, `let` when necessary, never `var`
- [ ] One variable per declaration
- [ ] No Array() / Object() constructors
- [ ] No `const enum`, `debugger`, `with`, `eval`, `Function(string)`
- [ ] Statements end with semicolons (no ASI reliance)

## Control flow
- [ ] `===` / `!==` used; only `x == null` allowed as exception
- [ ] switch has `default` last; no fallthrough in non-empty cases
- [ ] Prefer `for...of` for arrays; `for...in` only for dict objects and must filter

## Errors
- [ ] Throw only `Error` (or subclasses)
- [ ] Promise rejections use `Error`
- [ ] try blocks are tight; `catch (e: unknown)` and narrow

## Types
- [ ] `interface` for object shapes, `type` for unions/utilities
- [ ] Prefer optional `?` over `| undefined`
- [ ] Prefer `unknown` over `any`
- [ ] Assertions use `as`; object literals use `: Foo` annotation instead of `as Foo`

## JSDoc
- [ ] JSDoc adds meaning, not types
- [ ] Markdown lists used inside JSDoc
- [ ] `@param`/`@return` only when they add information
- [ ] No JSDoc type declarations in `.ts`

