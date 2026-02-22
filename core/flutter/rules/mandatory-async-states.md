---
trigger: always_on
---

RULE:

- Every async operation must expose and handle:
  - loading
  - success
  - empty (success but no data)
  - error (message + retry action)
- UI must render each state explicitly.

REQUIREMENTS FOR AI OUTPUT:

- Include UI rendering for all states.
- Provide a retry pathway for errors.
