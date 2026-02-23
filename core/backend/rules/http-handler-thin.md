---
trigger: always_on
---

HTTP handlers must:

- parse request
- call service
- map response
- handle errors

Handlers must NOT:

- access database
- contain business rules
