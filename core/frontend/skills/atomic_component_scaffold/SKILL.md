---
name: atomic_component_scaffold
description: Generates a complete Atomic Design component structure: .tsx, .module.scss, and .test.tsx files in the correct directory.
---

# Atomic Component Scaffold Skill

This skill automates the creation of new React components, ensuring consistency with the Atomic Design methodology and strict TypeScript/SCSS standards.

## Workflow

To create a new component, follow these steps:

1.  **Determine Atomic Level**:
    -   **Atoms**: Basic building blocks (Buttons, Inputs, Labels). Path: `src/components/atoms/`
    -   **Molecules**: Groups of atoms (SearchBox, percentage-field). Path: `src/components/molecules/`
    -   **Organisms**: Complex sections (Header, ProductGrid). Path: `src/components/organisms/`
    -   **Templates**: Page layouts without content. Path: `src/components/templates/`
    -   **Pages**: Specific instances of templates. Path: `src/pages/` (or `src/components/pages/` depending on router setup)

2.  **Create Directory**:
    -   Create a directory with the PascalCase name of the component: `src/components/[level]/[ComponentName]/`

3.  **Generate Files**:

    ### A. Component File (`[ComponentName].tsx`)
    -   **Imports**: React, SCSS module.
    -   **Interface**: Define `[ComponentName]Props`.
    -   **Function**: Use `const [ComponentName]: React.FC<[ComponentName]Props> = ({ ... }) => { ... }`.
    -   **Return**: JSX utilizing the SCSS classes.
    -   **Export**: Default export.

    ### B. Styles File (`[ComponentName].module.scss`)
    -   **Root Class**: Define a main class (e.g., `.root` or `.[componentName]`).
    -   **Imports**: Import variables/mixins if needed (`@import 'styles/variables';`).
    -   **Nesting**: Use standard SCSS nesting.

    ### C. Test File (`[ComponentName].test.tsx`)
    -   **Imports**: React, render, screen (from `@testing-library/react`), and the component.
    -   **Describe Block**: `describe('[ComponentName]', () => { ... })`.
    -   **It Blocks**:
        -   `it('renders correctly', () => { ... })`
        -   `it('handles [prop] correctly', () => { ... })`

4.  **Register Component**:
    -   Add an export to `src/components/[level]/index.ts` (if the barrel file exists) to make it easily importable.
    -   Example: `export { default as [ComponentName] } from './[ComponentName]/[ComponentName]';`

## Example Prompt

> "Create a new molecule called 'SearchBar'. It should have an input and a button."

**Agent Action**:
1.  Creates `src/components/molecules/SearchBar/`
2.  Creates `SearchBar.tsx`, `SearchBar.module.scss`, `SearchBar.test.tsx`
3.  Adds boilerplate code to all three.
