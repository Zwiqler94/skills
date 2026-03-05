# Smells and Heuristics (Curated, high-signal)

This is a curated subset of the larger catalog. Use these as triggers.

## General
- G22: Make logical dependencies physical (ask the dependency instead of assuming).
- G23: Prefer polymorphism to if/else or switch/case when behavior varies by type.
- G34: Keep one level of abstraction per function (extract lower-level detail).

## Functions
- F1: Too many arguments.
- F3: Flag arguments.

## Boundaries
- G36: Avoid transitive navigation (train wrecks).

## Tests
- T9: Tests should be fast.
