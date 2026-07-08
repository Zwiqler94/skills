# Academind Clean Code Course Map

Use this as a lightweight lookup guide for practical examples from:

- Course repo: <https://github.com/academind/clean-code-course-code>
- Course resources branch: <https://github.com/academind/clean-code-course-code/tree/general-resources>
- Course outline: <https://academind.teachable.com/p/clean-code>

Do not copy course PDFs, slides, or full example files into this skill. Use the
branch names as source anchors when a task needs concrete examples or a second
framing of a clean-code topic.

## Branch family map

- Course-level summaries: use `general-resources`, `summary`, and `roundup`
  for checklist and concept refresh before a broad review.
- Naming: use `naming-*` for intention-revealing names, casing, exceptions, and
  common naming pitfalls.
- Comments and formatting: use `comments-formatting-*` for bad vs useful
  comments, vertical formatting, and language-specific formatting tradeoffs.
- Functions: use `functions-*` for parameter count, output parameters,
  one-thing functions, DRY, avoiding useless extractions, side effects, and
  unit-test anchors.
- Control structures and errors: use `control-*` for guard clauses, positive
  phrasing, extracted conditions, validation extraction, error handling, factory
  functions, default parameters, and magic values.
- Objects and classes: use `obj-*` for object vs data-container choices,
  polymorphism, small classes, cohesion, Law of Demeter, and SOLID.

## Smell-to-source lookup

- Boolean flags or hard-to-read calls: start with `functions-01-*` through
  `functions-05-*`; replace ambiguous parameters with clearer functions,
  options objects, or domain types.
- Function has visible phases: start with `functions-07-*` and
  `functions-10-*`; split only when the extracted name adds intent.
- Unexpected mutation or hidden IO: start with `functions-11-*` and
  `functions-12-*`; separate calculation from effects and make effects
  explicit at boundaries.
- Deeply nested conditionals: start with `control-01-*` through `control-06-*`;
  use guard clauses, extracted predicates, and positive condition names.
- Validation mixed with orchestration: start with `control-07-*` and
  `control-08-*`; extract validation and keep the happy path readable.
- Error handling spread everywhere: start with `control-09-*` and
  `ERROR-HANDLING.md`; centralize boundary handling and keep each function to
  one responsibility.
- Switch/if ladder for behavior: start with `control-10-*` and `obj-02-*`;
  consider strategy tables, factories, polymorphism, or discriminated unions.
- Magic strings or numbers: start with `control-12-*`; name domain constants
  when the value is not self-explanatory.
- Overexposed object internals: start with `obj-04-*`, `obj-05-*`, and
  `BOUNDARIES-OBJECTS.md`; improve cohesion, tell-not-ask flow, and Law of
  Demeter boundaries.
- Tests hard to trust: start with `functions-13-*` and `TESTS.md`; isolate pure
  logic, test behavior, and keep setup small.

## How to use during a task

1. Identify the dominant smell before proposing a refactor.
2. Read only the matching branch/resource if examples would clarify the change.
3. Translate the idea into the target codebase's local style and public contracts.
4. Prefer the smallest behavior-preserving patch unless the user asked for a
   larger redesign.
5. Note any source branch used in the final summary when it materially shaped
   the recommendation.
