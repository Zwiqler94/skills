# Functions (Clean Code playbook)

## Small and single-purpose
- Functions should be small, with minimal nesting.
- If a function has obvious “sections” (setup, parsing, validation, persistence), it is doing multiple things.

## One level of abstraction
- Avoid mixing high-level intent with low-level details in the same function.
- The caller should read like a story: high-level first, details below.

## Stepdown rule
- Put callers above callees so you can read top-to-bottom, one abstraction level at a time.

## Arguments
- Prefer 0–2 parameters.
- Avoid boolean flags: split into two functions or use an options object.

## Command–Query Separation
- Either mutate state (command) OR return info (query), not both.
- Don’t make commands return “success flags” that end up in `if (...)` statements.
