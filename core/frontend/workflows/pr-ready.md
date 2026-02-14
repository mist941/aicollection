---
description: Ensure code quality, run tests, and generate a clear summary for the reviewer. Focus on "Dry" code and "Functional Programming" principles.
---

Steps

1. Code Audit & Cleanup
   - Scan changed files for `console.log`, `debugger`, and commented-out code blocks. 
   - Verify that all new components follow the Atomic Design structure.
   - Check if all new code is in TypeScript (no `any` types).

2. Style & Principles Check
   - Ensure the code is laconic and follows FP (no mutable state where avoidable).
   - Verify that SCSS Modules are used correctly (no global selectors).
   - Check if all strings are wrapped in `t()` from i18next.

3. Automated Testing
   - Run `npm test -- --findRelatedTests [changedFiles]`.
   - If tests fail, present the errors and offer to fix them automatically.

4. Storybook & Documentation
   - Verify if new components have corresponding `.stories.tsx` files.
   - Add JSDoc for:
     - Complex business logic.
     - Redux Thunk actions.
     - Brief component overview.

5. PR Description Generation
   - Create a Markdown Artifact with:
     - Summary: High-level overview of changes.
     - Checklist: (Tests passed, I18n added, TS types defined).
     - Technical details: List of new components and Redux actions.