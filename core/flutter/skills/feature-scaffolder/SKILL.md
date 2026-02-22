---
name: feature-scaffolder
description: Creates a new feature skeleton under lib/features/<feature>/{ui,state,data}: a base screen, state/controller, a data-layer stub, and minimal wiring so the app compiles and runs.
---

# Feature Scaffolder Skill

This skill scaffolds a new vertical slice for a feature in a Flutter project, adhering to strict architectural constraints and project rules.

## Scaffolding Guidelines

When requested to scaffold a new feature (for example, `user_profile`), follow these exact steps:

### 1. File Structure

Create the following directory structure and files:
`lib/features/<feature_name>/`

- `ui/<feature_name>_screen.dart`: The main UI screen.
- `state/<feature_name>_controller.dart`: The business logic and state manager.
- `data/<feature_name>_repository.dart`: The data layer stub.

### 2. Architectural Rules

- **UI (Dumb UI)**: The UI must not contain business logic or data fetching. It only renders based on the state and dispatches actions to the controller. If a widget becomes complex, extract it into smaller widgets.
- **State (Smart State)**: All async operations, data fetching, and business logic live here.
- **Async States**: Every async operation MUST expose and handle `loading`, `success`, `empty`, and `error` states. The UI must render each of these states explicitly (e.g. showing a loading indicator, empty state message, or error message with a retry pathway).
- **Data (Vertical Slice)**: The repository should contain a simple stub implementation (with mock data/delays) to ensure the slice compiles and works end-to-end immediately after generation.

### 3. Code Style & Conventions

- **Naming**:
  - Subfolders and files: `lower_snake_case` (e.g., `user_profile_screen.dart`).
  - Classes/Extensions: `UpperCamelCase`.
  - Variables/Functions: `lowerCamelCase`.
- **Flutter Practices**:
  - Use `const` constructors wherever possible.
  - Avoid deep nesting; extract widgets instead.
  - No magic numbers. Assume shared constants exist for spacing, radius, etc., or use localized constants.
- **Imports**: Use relative imports inside a feature to avoid chaotic cross-feature imports. Remove any unused imports.

### 4. Boilerplate Example Generation

To scaffold, generate complete runnable Dart files for each of the three layers.
Ensure that the final output provides a functional and demonstrable "vertical slice" that the user can immediately test and build.
Provide any necessary routing or minimal wiring code (if requested) so the app can compile and navigate to the new screen.
