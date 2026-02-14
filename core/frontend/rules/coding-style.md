---
trigger: always_on
---

Front-end Coding Style (FP & Dry)

General Principles
- Functional Programming (FP): Use pure functions, immutability, and declarative code (map/filter/reduce instead of for-loops).
- Conciseness: Prefer "dry" and "laconic" code. No fluff or obvious comments.
- Components: Use functional components with arrow function syntax (`const Comp = () => ...`).

TypeScript & Migration
- TS First: All new files MUST be `.ts` or `.tsx`.
- Strict Typing: Avoid `any`. Use interfaces for component props.
- Migration Strategy: When editing legacy JS files, suggest converting to TS if more than 30% of the file is touched.

Documentation (JSDoc)
- Only document:
  1. Complex business logic or math functions.
  2. Component descriptions (briefly).
  3. Redux Thunk actions (purpose and payload).
- Use `@deprecated` for legacy code that doesn't follow Atomic Design.