# Error Handling (Clean Code)

## Prefer exceptions (or a consistent Result type) over error codes

- Error codes create deeply nested “pyramid” control flow.
- Exceptions let you keep the happy path clear and move failure handling to a boundary.

## Guard clauses and validation

- Prefer guard clauses when they make invalid states exit early and leave the
  happy path flat.
- Extract complex conditions into positive, intention-revealing predicates.
- Keep validation separate from orchestration when validation rules are more
  than a trivial precondition.

## Try/catch discipline

- Try/catch blocks are structural noise. Extract try/catch bodies into
  well-named helpers.
- If a function contains `try`, it should do error handling and not mix other responsibilities.

## Null discipline

- Do not return null: prefer empty collections/objects, a special-case object,
  or an exception.
- Do not pass null: treat it as forbidden by default unless the API explicitly
  expects it.

## Special-case objects

- When callers must branch for "no data", a special-case object can remove
  conditional noise.
