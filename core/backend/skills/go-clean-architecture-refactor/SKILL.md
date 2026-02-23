---
name: go-clean-architecture-refactor
description: Detects layer violations (fat handlers, business logic in transport, direct DB calls) and refactors code into domain → service → repository separation.
---

# Go Clean Architecture Refactor

This skill is designed to analyze existing Go code for Clean Architecture violations and automatically refactor it into strict `domain` → `service` → `repository` separation.

## 1. Detection Phase

Scan the codebase or specific files for the following architectural violations:

- **Fat Handlers**: HTTP handlers that exceed 40 lines or contain complex branching/logic.
- **Business Logic in Transport**: Handlers making decisions, calculating values, or formatting data beyond simple DTO mapping.
- **Direct DB Calls**: SQL queries (`db.Query`, `db.Exec`), ORM calls, or database driver imports (`database/sql`) present inside HTTP handlers or services.
- **Dependency Inversion Violations**: Inner layers (e.g., `domain`) importing outer layers (e.g., `transport` or `repository` implementations).

## 2. Refactoring Execution Plan

When violations are detected, follow this step-by-step refactoring process to enforce Clean Architecture:

### Step 1: Extract the Domain

1. Identify the core entity managed by the fat handler/logic.
2. Create or update `domain/{entity}.go`.
3. Define the pure Go struct for the entity.
4. Define the `{Entity}Repository` interface containing the necessary data access methods.
5. (Optional) Define a `{Entity}Service` interface if the business rules require it.
   _Constraint:_ The `domain` package MUST NOT import any external dependencies, DB drivers, or transport frameworks.

### Step 2: Extract the Repository

1. Move all database interaction code (SQL, ORM, etc.) into `repository/{entity}_repository.go`.
2. Create a struct that implements the `domain.{Entity}Repository` interface.
3. Ensure the repository struct takes the DB connection via a constructor function: `func New{Entity}Repository(db *sql.DB) domain.{Entity}Repository`.
   _Constraint:_ The `repository` package cannot import `transport`.

### Step 3: Extract the Service

1. Move the business logic (validation, calculations, orchestrating repository calls) into `service/{entity}_service.go`.
2. Create a struct that holds the repository interface: `type {Entity}Service struct { repo domain.{Entity}Repository }`.
3. Implement the business logic as methods on the service struct.
4. Provide a constructor: `func New{Entity}Service(repo domain.{Entity}Repository) *{Entity}Service`.
   _Constraint:_ The `service` package depends ONLY on `domain` interfaces. No DB or HTTP logic allowed.

### Step 4: Thin Out the Transport (Handler)

1. Strip the original handler down to its bare essentials in `transport/{entity}_handler.go`.
2. The handler should ONLY:
   - Parse the incoming request into a DTO.
   - Call the appropriate method on the injected service.
   - Map the service's response to an output DTO.
   - Handle and format errors.
3. Inject the service via constructor: `func New{Entity}Handler(svc *service.{Entity}Service) *{Entity}Handler`.
   _Constraint:_ No database logic and no business logic in the handler. Function must be < 40 lines.

### Step 5: Update the Wiring

1. Locate the entry point where dependencies are injected and routes are registered (typically `main.go` or a `router.go`).
2. Update the initialization sequence to use the new constructors:
   ```go
   repo := repository.New{Entity}Repository(db)
   svc := service.New{Entity}Service(repo)
   handler := transport.New{Entity}Handler(svc)
   ```
3. Register the new handler methods with the router/transport layer.

## Post-Refactor Verification

After applying the refactoring, verify the following user constraints strictly:

- No global state.
- No `init()` dependency wiring.
- Functions are < 40 lines and have max 3 parameters.
- Interfaces are defined where they are used (or in the `domain` layer).
- Errors are not ignored; they are wrapped with context.
- No panic outside `main()`.
- Allowed packages only: `domain`, `service`, `repository`, `transport`, `config`, `logger`.
