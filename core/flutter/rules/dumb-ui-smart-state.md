---
trigger: always_on
---

RULE:

- Widgets must not contain business logic.
- No data fetching inside widgets (except triggering actions via state/controller).
- All async operations live in state/controller or repository/service.

REQUIREMENTS FOR AI OUTPUT:

- Put logic in state/controller; UI only renders + dispatches actions.
- If a widget grows complex, extract sub-widgets.
