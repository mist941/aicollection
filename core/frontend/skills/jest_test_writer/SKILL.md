---
name: jest_test_writer
description: Analyzes a component's props and structure to automatically generate comprehensive Jest/React Testing Library test suites, covering rendering, props, and user interactions.
---

# Jest Test Writer Skill

This skill automates the creation of robust unit tests for React components. It statically analyzes the component's TypeScript interface and JSX structure to ensure high test coverage for both UI rendering and user behavior.

## Workflow

### 1. Component Analysis
-   **Read File**: Use `view_file` to read the target component (e.g., `MyComponent.tsx`).
-   **Extract Props**: Identify the `interface` or `type` defining the props.
    -   *Mandatory Props*: Must be provided in all tests.
    -   *Optional Props*: Create test cases for both presence and absence.
    -   *Event Handlers*: Identify props starting with `on` (e.g., `onClick`, `onChange`) to test interactions.
-   **Identify Elements**: Look at the JSX to see what roles/elements are rendered (buttons, inputs, text).

### 2. Test Strategy Formulation
-   **Rendering Tests**:
    -   "Renders correctly with default props".
    -   "Renders [propName] when provided".
    -   "Does not crash when optional props are missing".
-   **Interaction Tests**:
    -   "Calls [handlerName] when clicked/changed".
    -   "Updates input value when typed into" (if controlled).
    -   "Is disabled when [disabledProp] is true".
-   **Accessibility Checks** (Bonus): 
    -   Verify `aria-label`, `alt` text, or roles if present in code.

### 3. Test Generation
-   **Imports**: standard `render`, `screen`, `fireEvent` (or `userEvent`) from `@testing-library/react`.
-   **Mocking**: Create mock functions for event handlers using `jest.fn()`.
    -   `const mockOnClick = jest.fn();`
-   **Structure**:
    -   Use `describe('Component Name', () => { ... })`.
    -   Use `beforeEach(() => { jest.clearAllMocks(); })`.
-   **Implementation**:
    -   **Render**: `render(<Component {...defaultProps} />);`
    -   **Select**: `const element = screen.getByRole('button', { name: /save/i });`
    -   **Interact**: `fireEvent.click(element);`
    -   **Assert**: `expect(mockOnClick).toHaveBeenCalledTimes(1);`

## Best Practices Enforced
-   **User-Centric Queries**: Prefer `getByRole`, `getByLabelText`, `getByText` over `testId` or class selectors.
-   **Isolation**: Each test should be independent.
-   **Clarity**: Test descriptions should form a readable sentence.

## Example Prompt
> "Write unit tests for `UserProfile.tsx`. It has props for `name`, `avatarUrl`, and `onEdit`."
