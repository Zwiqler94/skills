# TypeScript and JavaScript Adaptation Guide (Clean Code)

This file converts classic Clean Code guidance into practical TS/JS patterns.

## Naming
- Prefer “domain nouns” over `helper`, `manager`, `util`.
- Prefer explicit units:
  - `timeoutMs`, `expiresAtUtc`, `maxRetries`

## Functions: avoid boolean flags
Bad:
```ts
render(user, true, false);
```

Better:
```ts
interface RenderOptions {
  showAvatars?: boolean;
  compact?: boolean;
}

render(user, { showAvatars: true, compact: false });
```

Best when flags imply two different behaviors:
```ts
renderCompact(user);
renderFull(user);
```

## Error handling: boundary-first
### Option A: throw at boundaries
- Use exceptions for exceptional cases.
- Catch at outer layers (API handlers, UI shell), add context, map to user-facing errors.

### Option B: explicit Result types for expected failures
```ts
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: Error };
```

Pick one approach per subsystem and stay consistent.

## “One thing” in async code
- Split “fetch, parse, validate, persist” into small functions.
- Avoid mixing retries, parsing, and domain rules in one async blob.

## Tests
- Prefer deterministic tests.
- Hide noisy setup behind small builders, not giant factories.
- Use meaningful test names: “returns 404 when user is missing”.

## Boundaries: adapters
- Wrap SDKs behind a small interface:
  - Keeps vendor churn from leaking into domain logic
  - Makes tests cheaper and faster
