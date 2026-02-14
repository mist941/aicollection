---
name: dry_refactorer
description: Analyzes the codebase for duplicated logic and refactors it into reusable custom hooks or pure utility functions, adhering to Functional Programming principles.
---

# DRY Refactorer Skill

This skill is designed to identify "WET" (Write Everything Twice) code and ruthlessly refactor it into "DRY" (Don't Repeat Yourself) abstractions. It prioritizes Functional Programming (FP) style, favoring pure functions and composable hooks over classes or imperative loops.

## Workflow

### 1. Identification (The Hunt)
- **Scan**: Look for repeated code blocks, similar `useEffect` patterns, or identical helper functions scattered across components.
- **Signals**:
  - Components with > 200 lines usually hide extractable logic.
  - Multiple components importing the same third-party libraries (e.g., specific Lodash chains or formatting libraries) often share implementation details.
  - "Copy-paste" comments or suspiciously similar variable names in different files.

### 2. Strategy Selection
Once duplication is found, decide the target abstraction:

- **Stateful Logic (Lifecycle, API calls, Form handling)**
  - **Target**: Custom Logic Hook (`src/hooks/use[Feature].ts`)
  - **Naming**: Must start with `use`.
  - **Style**: Return an object or tuple of reactive values/functions.

- **Stateless Logic (Math, String manipulation, Data transformation)**
  - **Target**: Pure Utility Function (`src/utils/[domain].ts`)
  - **Style**: Pure functions (deterministic, no side effects). Use currying or composition if it simplifies usage.
  - **FP Rule**: Avoid `let` and loops. Use `map`, `filter`, `reduce`, and immutable data structures.

- **UI Patterns (Wrapped elements, Conditional rendering)**
  - **Target**: Higher-Order Component (HOC) or Compound Components.

### 3. Execution (The Refactor)
1.  **Isolate**: Create the new file for the hook or utility.
2.  **Migrate**: Move the logic, ensuring all dependencies are passed as arguments (for utils) or handled via `useRef`/`useCallback` (for hooks).
3.  **Test**: Write a unit test for the new abstraction *immediately*. It's easier to test a pure function/hook in isolation than inside a component.
4.  **Integrate**: Replace the code in **one** component first to verify behavior.
5.  **Propagate**: Apply the change to all other occurrences.

## FP Style Guide for Refactoring

**Bad (Imperative/WET):**
```typescript
// Found in multiple files
const total = items.reduce((acc, item) => acc + item.price, 0);
const formatted = `$${total.toFixed(2)}`;
```

**Good (Declarative/DRY):**
```typescript
// src/utils/currency.ts
export const calculateTotal = (items: HasPrice[]): number => 
  items.reduce((acc, item) => acc + item.price, 0);

export const formatCurrency = (amount: number): string => 
  `$${amount.toFixed(2)}`;

// In components:
const total = formatCurrency(calculateTotal(items));
```

## Example Prompt

> "I see we have the same email validation logic in distinct Login and Register forms. Use the dry_refactorer skill to extract this into a `useFormValidation` hook or a `validators.ts` utility."
