# Unit Tests (Clean Code)

## The three laws of TDD (practical loop)
- Write a failing test before production code.
- Write only enough test to fail.
- Write only enough production code to pass.

## Keep tests clean
- Test code is production code. Sloppy tests rot your system.

## One assert per test (guideline)
- Prefer tests that arrive at one clear conclusion.
- If multiple asserts are needed, keep them within one concept.

## Single concept per test
- Do not bundle unrelated behaviors into “misc tests.”

## F.I.R.S.T.
- Fast: run them frequently.
- Independent: no ordering dependencies.
- Repeatable: run anywhere.
- Self-validating: pass/fail without log spelunking.
- Timely: written just before the code that passes.
