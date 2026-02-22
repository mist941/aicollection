---
trigger: always_on
---

RULE:

- The app must use Flutter Material 3 as the primary design system.
- The app must use flex_color_scheme to define and manage the theme (Light/Dark) centrally.
- All screens/widgets must rely on ThemeData (colors, typography, shapes) instead of hardcoded styling.

REQUIREMENTS:

- Enable Material 3:
  - MaterialApp(theme: ..., darkTheme: ..., themeMode: ThemeMode.system, useMaterial3: true)
- Define theme via flex_color_scheme:
  - Use FlexThemeData.light(...) and FlexThemeData.dark(...).
- No hardcoded colors in UI code:
  - Use Theme.of(context).colorScheme / textTheme.
  - Exceptions: only for temporary debugging and must be removed before commit.
- Shared UI constants:
  - Spacing/radius/text styles must come from shared constants (e.g., AppSpacing/AppRadius) if needed, but prefer Theme first.

REQUIREMENTS FOR AI OUTPUT:

- When generating UI code, always use Material widgets compatible with Material 3.
- Always reference theme tokens (ColorScheme/TextTheme) rather than custom colors.
- If a new component needs styling, extend the theme rather than adding per-widget overrides.
