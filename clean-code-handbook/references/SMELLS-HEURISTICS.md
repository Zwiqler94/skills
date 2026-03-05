# Smells and Heuristics (Practical List)

Use these as “review triggers”. If you see one, stop and simplify.

## Names
- “manager/helper/util” without domain meaning
- abbreviations the team doesn’t share
- inconsistent vocabulary for the same concept

## Functions
- more than ~1 screen long without a clear narrative
- mixes data fetching, parsing, validation, and side effects
- boolean flags changing behavior
- deep nesting instead of early returns

## Comments
- comments that restate code
- commented-out code blocks
- TODOs with no owner or condition

## Error handling
- swallowing exceptions
- returning sentinel values (`null`, `-1`) without strong checks
- error handling scattered everywhere instead of at boundaries

## Boundaries
- vendor types used everywhere
- direct SDK calls sprinkled through domain code
