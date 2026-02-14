---
description: Use this workflow when creating a new UI component or a functional feature. Follow the project's hybrid architecture (Atomic Design for UI) and strict Functional Programming (FP) style.
---

Steps

1. Requirement Analysis
   - Ask the user for:
     - Component name and its level in Atomic Design (Atom, Molecule, Organism).
     - Figma URL or screenshot (if applicable).
     - Brief description of the business logic/API interaction.

2. State & Data Setup (Redux Toolkit)
   - If the feature requires global state, create/update a Redux Slice:
     - Use `createSlice` from `@reduxjs/toolkit`.
     - Define `initialState` and `Interface` in TypeScript.
     - Create `createAsyncThunk` for API calls using the established `axios` instance.
     - Ensure logic is pure and follows FP principles.

3. Component Scaffolding
   - Create a new directory in `src/components/[level]/[ComponentName]`.
   - Generate the following files:
     - `index.ts` (for clean exports).
     - `[ComponentName].tsx` (Functional component, TS, dry style, JSDoc for props).
     - `[ComponentName].module.scss` (CamelCase classes).
     - `[ComponentName].test.tsx` (Basic Jest tests: render and main interaction).

4. I18n & Assets
   - Check for hardcoded strings. Apply translation for them.
   - Use `useTranslation` hook from `i18next`.

5. Visual Verification (Skill Trigger)
   - Trigger `browser_sync_review` (if available) to verify the rendered component against the design.

6. Final Review
   - Run a quick lint check on generated files.
   - Present the "Artifact" (file tree and summary) to the user.