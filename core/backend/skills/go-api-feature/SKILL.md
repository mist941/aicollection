---
name: go-api-feature
description: Scaffolds a new API feature in Go (domain, repository, service, handler, DTOs, wiring) following strict clean architecture.
---

# Go API Feature Creator

This skill generates a complete vertical slice for a new API feature in Go. It strictly adheres to the project's clean architecture and coding standards.

## Execution Steps

When the USER requests a new API feature (e.g., "User" or "Book"), automatically generate the following components in their respective layers. Make sure to adapt the code to the specific routing or database framework in use, without violating domain purity.

### 1. Domain Layer (`domain/{feature}.go`)

- **Responsibility:** Core business models and interface contracts.
- **Rules:** Must be completely pure. NO imports of `database/sql`, `gin`, `http`, `echo`, `grpc`, or external SDKs.
- **Contents:**
  - The core domain Entity struct.
  - The Repository interface (e.g., `{Feature}Repository`).
  - (Optional) Service interface if needed by domain rules.

### 2. Repository Implementation (`repository/{feature}_repository.go`)

- **Responsibility:** Database interactions.
- **Rules:** Implements the domain repository interface. Cannot import `transport`.
- **Contents:**
  - The Repository struct.
  - Constructor: `func New{Feature}Repository(db *sql.DB) domain.{Feature}Repository` (or equivalent DB dependency).

### 3. Service Implementation (`service/{feature}_service.go`)

- **Responsibility:** Business logic.
- **Rules:** Depends ONLY on domain interfaces. Cannot contain DB logic or HTTP logic.
- **Contents:**
  - The Service struct holding domain layer repository definitions.
  - Constructor: `func New{Feature}Service(repo domain.{Feature}Repository) *{Feature}Service`.

### 4. DTO Models & Transport Layer (`transport/{feature}_handler.go`)

- **Responsibility:** HTTP request/response handling.
- **Rules:** Handlers must ONLY parse requests, call the service, map responses, and handle errors. No business or DB rules.
- **Contents:**
  - DTO structs (Requests and Responses).
  - The HTTP Handler struct.
  - Constructor: `func New{Feature}Handler(svc {Feature}Service) *{Feature}Handler` (Interface defined where used, inside transport layer if appropriate).

### 5. Constructor Wiring & Router Registration

- **Responsibility:** Dependency injection setup.
- **Rules:** No global state, no `init()` dependency wiring. Pass dependencies via constructors.
- **Contents:** Setup wiring snippet to inject into the application entry point (e.g., `main.go` or `router.go`):

  ```go
  {feature}Repo := repository.New{Feature}Repository(db)
  {feature}Svc := service.New{Feature}Service({feature}Repo)
  {feature}Handler := transport.New{Feature}Handler({feature}Svc)

  // Example router registration
  // router.POST("/api/{feature}", {feature}Handler.Create)
  ```

## Critical Constraints to Verify

- **Layer Direction:** Dependency direction always inward (`transport` -> `service` -> `domain` <- `repository`).
- **Code Profile:** Functions < 40 lines. Max 3 parameters per function (otherwise use a parameter struct).
- **Error Handling:** Never ignore errors. Wrap errors with context. No panic outside `main()`.
- **Allowed Packages ONLY:** `domain`, `service`, `repository`, `transport`, `config`, `logger`. NO `utils`, `helpers`, `common`, `misc`.
