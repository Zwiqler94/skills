---
name: clean-code-handbook
description: "Apply Clean Code principles to reviews and edits: intention-revealing names, small functions that do one thing, minimal argument lists, clear error handling, clean tests, and boundary isolation around third-party code. Use when improving readability, maintainability, refactoring legacy code, or creating review checklists. Summarizes Clean Code (Robert C. Martin) as practical agent instructions, not a book copy."
license: "CC-BY-4.0 (skill text is an original summary; source referenced)"
metadata:
  author: jake-arbor
  version: "1.1.0"
  created: "2026-02-25"
  source:
    - "Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin)"
    - "https://ptgmedia.pearsoncmg.com/images/9780132350884/samplepages/9780132350884.pdf"
---

# Skill: Clean Code Handbook

## Assumption
This skill is used for **improving code quality**, not for bike-shedding formatting. Prefer minimal diffs that reduce cognitive load, improve error locality, and make future changes cheaper.

## Compatibility
Use for language-agnostic clean-code reviews and refactors. Includes TypeScript/JavaScript adaptations (Node and Angular). Optional scripts require Bash and either `rg` (ripgrep) or `grep`.

## When to activate
Activate when the user asks for:
- “clean code” review, refactor, readability improvements, or maintainability
- guidance on naming, function structure, comments, error handling, tests, or boundaries
- “make this less gross” cleanup of legacy modules
- a PR review rubric focused on clarity and simplicity

## Non-goals
- Do not rewrite architecture unless requested.
- Do not change public APIs without a migration note.
- Do not optimize performance unless requested or the refactor makes it strictly better.

---


## High-signal rules (the ones you actually use)
- **Optimize for reading**: code is read far more than it is written. Make “read path” the default.
- **Boy Scout Rule**: always leave the area you touched cleaner than you found it.
- **Command–Query Separation**: functions either *do* or *answer*, not both.
- **Prefer exceptions (or a consistent Result type) over error codes**: keep the happy path readable.
- **Don’t return null; don’t pass null**: prefer empty objects/lists, exceptions, or special-case objects.
- **Avoid “train wrecks”**: long call-chains leak internals; use Law of Demeter style boundaries.
- **Formatting is communication**: choose team rules and apply consistently; structure files “like a newspaper.”
- **Clean tests are non-negotiable**: follow TDD loop, keep tests readable; use F.I.R.S.T. as the test quality bar.

## Operating principles
### Primary objective
Reduce **WTFs per minute** in code review by making the code read like a story from top to bottom.

### Order of operations
1) Make it **correct**
2) Make it **clear**
3) Make it **simple**
4) Then make it **fast** if needed

### Outputs
When applying this skill, produce:
1) Findings grouped by category
2) Minimal patch suggestions (or snippet-level changes)
3) Risk notes (behavior changes, API breaks, hidden coupling)
4) Tests affected and what to add
5) A short checklist for reviewers

---

## Workflow: Apply Clean Code to a file or PR
### Step 1: Read like a stranger
- Start at the entrypoint and read top-to-bottom.
- Note “context switches”: jumping between files, deep nesting, unclear names.
- Identify the “happy path” and “error path”.

### Step 2: Fix naming first
- Rename to make intent obvious at the call site.
- Prefer names that are:
  - intention-revealing
  - pronounceable
  - searchable
  - consistent with domain language
- Remove misleading or redundant words.
- Remove encodings (type prefixes, Hungarian-ish noise).

### Step 3: Make functions small and single-purpose
- Aim for “one thing” per function.
- Keep a single level of abstraction per function.
- Prefer early returns over deep nesting when it clarifies flow.
- Minimize parameters:
  - Prefer 0–2 args
  - Avoid boolean flags (use two functions or an options object)

### Step 4: Separate responsibilities
- Push details down behind well-named functions.
- Prefer cohesive units (small classes/modules) over “god modules”.
- Keep construction separate from use (especially for systems wiring).

### Step 5: Make error handling a first-class design
- Keep the happy path readable.
- Push error handling to boundaries when possible.
- Avoid returning sentinel values that callers forget to check.
- Standardize error types and messages.

### Step 6: Tests as the safety rail
- Refactor under test coverage.
- Make tests readable and intention-revealing.
- Keep tests fast and deterministic.
- Remove duplication in tests too, but don’t DRY them into unreadable factories.

### Step 7: Isolate boundaries
- Wrap third-party libraries behind adapters.
- Do not leak vendor types all over your domain.
- Test adapters with thin integration tests.

### Step 8: Final pass
- Delete dead code and commented-out code.
- Align formatting enough to support reading.
- Leave the module “cleaner than you found it”.

---

## Practical rules by category
## Naming
- Prefer domain language over generic “manager/helper/util”.
- Avoid abbreviations unless standard in the domain.
- Use symmetric naming for symmetric concepts.
- Use verbs for functions, nouns for values/types.

## Functions
- Prefer pure functions where practical.
- Replace long parameter lists with:
  - an options object (documented fields)
  - or a small domain type
- Replace long if/else chains with:
  - polymorphism
  - strategy tables
  - discriminated unions (TS)

## Comments
- Comments are allowed when they explain **why**, constraints, or non-obvious tradeoffs.
- Avoid comments that restate the code.
- TODOs must be actionable (owner, ticket, or condition).

## Formatting
- Optimize for vertical readability:
  - related code stays close
  - blank lines separate concepts
  - files read top-to-bottom like a newspaper

## Error handling
- Prefer exceptions or a standard Result type, but be consistent.
- Do not swallow errors.
- Add context at boundaries, not everywhere.

## Tests
- Use AAA (Arrange, Act, Assert) or Given/When/Then.
- Test one behavior per test.
- Prefer descriptive test names that read like requirements.

## Boundaries
- Keep third-party code at edges.
- Create small adapters so the rest of the codebase stays stable if vendors change.

---

## TypeScript and JavaScript adaptations
See `references/TYPESCRIPT-ADAPTATION.md` for concrete patterns:
- options objects instead of boolean flags
- discriminated unions for error results
- `unknown` plus narrowing instead of `any`
- small modules with named exports

---

## Optional scripts
- `scripts/scan-smells.sh` finds common “clean code” smells (TODO/FIXME, commented-out code, deep nesting hints, and console noise).

---

## Minimal review checklist
- [ ] Names reveal intent without comments
- [ ] Functions do one thing and are not “scroll novels”
- [ ] Parameters are minimal, no boolean-flag soup
- [ ] Happy path is readable, error handling is consistent
- [ ] Tests exist and read clearly
- [ ] Third-party boundaries are isolated
- [ ] Dead code and commented-out code removed


## Changelog

### 1.1.0 (2026-02-26)
- Added deeper coverage for readability, functions, formatting, Law of Demeter, null handling, tests (TDD + F.I.R.S.T.), and key heuristics.
