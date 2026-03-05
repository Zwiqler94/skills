# PR Comment Snippets (Google TS Style)

These are short, reusable review comments.

## Default exports
“Google style avoids default exports. Please switch to a named export so imports have a canonical name.”

## Interface vs type
“This is an object shape, so prefer `interface` over `type` to match Google TS style and keep contracts extendable.”

## JSDoc type tags
“In `.ts`, JSDoc type annotations are redundant. Keep the description but remove `{Type}` from `@param/@return`.”

## Throw only Error
“Please throw or reject only `Error` (or subclasses) so stack traces are preserved.”

## Prefer unknown over any
“If the value is unknown, use `unknown` and narrow. Reserve `any` for deliberate escape hatches with a comment.”

