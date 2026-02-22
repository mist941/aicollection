---
trigger: always_on
---

RULE:

- New functionality must live in: lib/features/<feature_name>/{ui,state,data}
- Shared reusable code must live in: lib/shared/
- Do not dump new code into root lib/ or random folders.

REQUIREMENTS FOR AI OUTPUT:

- Always provide file paths for new files.
- Prefer small focused files; avoid “god” files.
