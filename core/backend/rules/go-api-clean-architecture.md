---
trigger: always_on
---

Enforce layered architecture:

Layers:

- transport (HTTP/gRPC)
- service (business logic)
- domain (entities + interfaces)
- repository (DB implementation)

Rules:

- transport cannot access repository directly
- repository cannot import transport
- domain has zero external dependencies
- services depend only on domain interfaces
- dependency direction always inward
