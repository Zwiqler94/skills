# Objects, Data Structures, and Boundaries

## Objects vs data structures
- OO: easier to add new types without changing functions.
- Procedural: easier to add new functions without changing data shapes.
- Use both intentionally.

## Law of Demeter (LoD)
- “Talk to friends, not to strangers.”
- Avoid call chains that require knowing internal structure.

## Train wrecks
- Long call-chains are a smell: split, introduce locals, or hide internals behind methods.
- Better: introduce an adapter/facade so domain code doesn’t depend on vendor internals.
