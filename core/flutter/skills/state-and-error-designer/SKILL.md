---
name: state-and-error-designer
description: Designs flow states and transitions, enforcing loading/success/empty/error plus a retry path for every async operation, and keeps business logic out of widgets.
---

# State & Error Designer Skill

This skill enforces strict state management and error handling across the application, ensuring a robust and predictable user experience. It focuses on clearly defining the possible states of any asynchronous operation and ensuring the UI reacts perfectly to these states without containing the logic itself.

## Core Rules & Responsibilities

1.  **Dumb UI, Smart State**:
    - **Widgets must NOT contain business logic or data fetching.** They only listen to state streams/notifiers and render visual representations.
    - **State Controllers/Managers handles all logic.** They orchestrate data fetching, transformations, and state transitions.

2.  **The Four Immutable Async States**:
    Every asynchronous operation (e.g., API call, database query) MUST explicitly model, emit, and handle these four states:
    - `loading`: The operation is in progress. The UI must show a progress indicator.
    - `success`: The operation succeeded and returned actionable data. The UI renders the content.
    - `empty`: The operation succeeded, but returned no data (e.g., empty list). The UI renders an explicit empty state.
    - `error`: The operation failed. The UI MUST display a clear error message AND provide a retry mechanism (e.g., a "Try Again" button) that re-triggers the operation.

3.  **State Transition Flow**:
    - **Initial State**: Usually `loading` if fetching data on screen load, or a default idle state if waiting for user interaction.
    - **Action Triggered**: Transition to `loading`.
    - **Resolution**: Transition to `success`, `empty`, or `error` depending on the outcome.
    - **Retry**: From `error`, triggering a retry must transition back to `loading`.

4.  **Error Handling Requirements**:
    - **Actionable Errors**: Error states must clearly indicate what went wrong in user-friendly terms.
    - **Retry Pathways**: Every error state must be accompanied by a retry action (e.g., a callback function or event dispatcher) that the user can trigger to attempt the operation again.

## Usage Guide

When tasked with designing or implementing state for a new feature or refactoring an existing one:

1.  **Define the State Model**: Create a clear representation (e.g., sealed classes or state enums) of the `loading`, `success` (with payload), `empty`, and `error` (with message/exception) states.
2.  **Implement the Controller**: Write the logic to transition through these states during the async operation. Ensure any catch block correctly emits the `error` state.
3.  **Implement the UI**: Create the UI widget that listens to the state model and maps each state explicitly to a corresponding widget.
4.  **Wire the Retry Mechanism**: Connect the retry button in the Error state UI back to the trigger method in the Controller.

Ensure that the resulting code remains clean, idiomatic Dart/Flutter, and adheres to the project's styling and structural guidelines.
