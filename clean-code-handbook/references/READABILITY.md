# Readability and the Boy Scout Rule

## Readability is the speed hack
- Code is read much more than it is written. Optimize the “reading experience” first.
- When you make reading easier, writing becomes easier because you can navigate and modify safely.

## Boy Scout Rule
- Every change should leave the touched area slightly cleaner:
  - rename one misleading identifier
  - extract one overgrown function
  - remove one chunk of duplication
  - simplify one gnarly conditional

## Practical PR rule
- If your PR cannot include a cleanup, at least include a “cleanup note”:
  - what you saw
  - why you didn’t touch it
  - the safest next refactor
