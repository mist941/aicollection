---
trigger: always_on
---

RULE:

- Implement tasks as end-to-end slices: UI -> State/Controller -> Data layer.
- Each slice must compile and run after completion.

REQUIREMENTS FOR AI OUTPUT:

- Generate code that results in a runnable app state (no “pseudo-only” stubs).
- Keep changes limited to the requested slice; avoid unrelated refactors.
