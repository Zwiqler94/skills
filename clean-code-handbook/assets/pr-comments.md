# PR Comment Snippets (Clean Code)

## Naming
“Can we rename this to reveal intent at the call site? Right now I have to read the implementation to understand what it means.”

## Function size
“This function is doing multiple things. Can we split it so the happy path reads top-to-bottom, with details pushed into well-named helpers?”

## Boolean flags
“Boolean flags make call sites unreadable. Prefer an options object or two explicit functions.”

## Error handling
“Can we keep the happy path clean and move the error handling to a boundary layer, or standardize on a Result type?”

## Boundaries
“This SDK type is leaking into domain logic. Consider an adapter so the rest of the codebase stays stable if the vendor changes.”
