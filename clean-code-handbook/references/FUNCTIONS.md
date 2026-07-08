# Functions (Clean Code playbook)

## Small and single-purpose

- Functions should be small, with minimal nesting.
- If a function has obvious "sections" (setup, parsing, validation,
  persistence), it is doing multiple things.

## One level of abstraction

- Avoid mixing high-level intent with low-level details in the same function.
- The caller should read like a story: high-level first, details below.

## Stepdown rule

- Put callers above callees so you can read top-to-bottom, one abstraction
  level at a time.

## Arguments

- Prefer 0–2 parameters.
- Avoid boolean flags: split into two functions or use an options object.
- Avoid output parameters. Return a value or mutate through a clearly named
  command, not both.

## Splitting discipline

- Extract when the new name explains intent or separates abstraction levels.
- Do not split purely to make functions tiny if the caller becomes harder to read.
- Keep side effects visible: separate calculation, validation, persistence, and
  logging when they are mixed.

## Command-Query Separation

- Either mutate state (command) OR return info (query), not both.
- Do not make commands return "success flags" that end up in `if (...)`
  statements.
