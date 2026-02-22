---
name: refactor-splitter
description: Detects duplication, god-widgets, and oversized files, then extracts reusable widgets/services, aligns code with features/... + shared, and keeps diffs small and readable.
---

# Refactor Splitter Skill

This skill is responsible for identifying and resolving code smells such as God-widgets, massive files, deeply nested widget trees, and duplicated logic. It systematically breaks down complex code into smaller, maintainable, and highly cohesive components while adhering strictly to the project's folder structure and style guide.

## Priorities and Triggers

Activate this skill when:

- A file becomes too large or difficult to read.
- A widget contains deeply nested conditions (`if`/`else`) or build trees.
- The same UI layout or business logic is duplicated across multiple areas.
- Code is dumped in the root `lib/` directory or outside of specific feature/shared modules.

## Refactoring Guidelines

### 1. File and Class Splitting

- **One Public Entity Per File**: Ensure there is only one public widget, class, extension, or enum per file (with the exception of tiny, tightly-coupled private helpers).
- **God-Widget Dismantling**: Break large widgets down. Extract distinct visual sections (e.g., headers, lists, forms) into their own private or shared sub-widgets.
- **Avoid Deep Nesting**: Instead of stacking multiple Builders, Columns, and conditional logic within a single `build` method, extract these branches into separate stateless widgets or methods.

### 2. Structural Alignment

- **Shared Code Extraction**: When extracting reusable UI segments, helper methods, or services, place them in the `lib/shared/` directory.
- **Feature Modules**: Keep feature-specific widgets, state, and data layers scoped purely to their respective feature folder: `lib/features/<feature_name>/{ui,state,data}`.
- Do NOT deposit newly extracted generic components haphazardly into `lib/`. Ensure they are accurately categorized within `lib/shared/` (e.g., `lib/shared/widgets/`, `lib/shared/utils/`).

### 3. Maintainability and Aesthetics

- **Small, Focused PRs/Diffs**: Perform refactoring incrementally. Keep diffs small, focused on a single logical change, and easily reviewable.
- **Const Constructors**: Always add `const` to newly extracted widgets and their constructors to improve rendering performance.
- **Theming & Localization Constraints**: Ensure extracted widgets do not rely on hardcoded magic numbers or colors. Standardize them to pull from shared constants (e.g., `AppSpacing`) or the `Theme.of(context)` via `flex_color_scheme`.

### 4. Implementation Steps

1.  **Analyze**: Review the target file to identify boundaries where components or logic can be cleanly severed.
2.  **Extract**: Move the disconnected block into a newly created file.
3.  **Name Accurately**: Adhere to `lower_snake_case` for the new filename and `UpperCamelCase` for the class/widget.
4.  **Wire Up**: Fix imports within the original file, preferring relative imports for internal feature components.
5.  **Verify**: Ensure the code formatting matches `dart format` and compiles successfully without regressions.
