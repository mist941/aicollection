---
trigger: always_on
---

Styling Rules (SCSS Modules)

- Isolation: Always use SCSS Modules. Import as `import styles from './MyComponent.module.scss'`.
- Naming: Use camelCase for class names in SCSS (e.g., `.mainWrapper`) to match JS object notation `styles.mainWrapper`.
- Cleanup: Check for unused selectors in SCSS files after refactoring.
- Hierarchy: No global styles allowed except in `src/styles/global.scss`.