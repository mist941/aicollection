---
trigger: always_on
---

RULES:

- Naming:
  - Files & folders: lower_snake_case (e.g., user_profile_screen.dart)
  - Classes/Enums/Extensions: UpperCamelCase
  - Variables/Functions/Methods: lowerCamelCase
  - Constants: lowerCamelCase + prefix k (e.g., kDefaultPadding) OR use const in a dedicated constants file; choose one style and keep consistent.
- Structure:
  - One public widget/class per file (exceptions: tiny private helpers).
  - Prefer small widgets; extract repeated UI into separate widgets.
  - Keep files readable; if a file becomes too large, split it.
- Imports:
  - No unused imports.
  - Prefer relative imports inside a feature; avoid chaotic cross-feature imports.
- Flutter best practices:
  - Use const constructors where possible.
  - Avoid deep nesting: extract widgets instead of piling conditions/build trees.
  - No magic numbers: spacing/radius/text styles come from shared constants (AppSpacing/AppRadius/AppTextStyles).
- Formatting:
  - Always keep code formatted with dart format/flutter format.
  - No manual alignment for aesthetics that conflicts with formatter.

REQUIREMENTS FOR AI OUTPUT:

- Always generate code that follows these naming rules and uses const where possible.
- Always provide correct file paths and names matching lower_snake_case.
- Prefer clarity over cleverness; keep code idiomatic Dart.
