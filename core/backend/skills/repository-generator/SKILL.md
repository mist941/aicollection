---
name: repository-generator
description: Generates a Repository implementation with PostgreSQL using pure domain interfaces, prepared queries, context, and error wrapping.
---

# Go Repository Generator

This skill generates a database repository implementation for a given domain entity, specifically tailored for PostgreSQL and strictly following the project's Go clean code guidelines.

## Execution Steps

When generating a repository for a given entity, generate the interface in the `domain` package and the implementation in the `repository` package.

### 1. Domain Interface (`domain/{entity}.go`)

- Create the repository interface in the `domain` package if it doesn't already exist.
- Ensure all methods accept `context.Context` as the first parameter.
- Methods must only return domain entities or built-in types (no infrastructure types).
- **Example Interface:**

  ```go
  package domain

  import "context"

  type {Entity}Repository interface {
      GetByID(ctx context.Context, id int64) (*{Entity}, error)
      Create(ctx context.Context, e *{Entity}) error
      Update(ctx context.Context, e *{Entity}) error
      Delete(ctx context.Context, id int64) error
  }
  ```

### 2. Repository Implementation (`repository/{entity}_repository.go`)

- The repository must be implemented in the `repository` package.
- Avoid business logic here; only database interaction is allowed.
- Must implement the `domain.{Entity}Repository` interface.
- Must not import the `transport` layer or external HTTP frameworks.

#### Constructor (Dependency Injection)

- Define a constructor `New{Entity}Repository(...)` that takes a database connection (`*sql.DB` or `*sql.Conn` depending on context).
- No global database state.

  ```go
  package repository

  import (
      "context"
      "database/sql"
      "fmt"
      // other standard imports
      "your-module/domain"
  )

  type {entity}Repository struct {
      db *sql.DB
  }

  func New{Entity}Repository(db *sql.DB) domain.{Entity}Repository {
      return &{entity}Repository{
          db: db,
      }
  }
  ```

#### PostgreSQL Implementation & Context Usage

- All database operations must use the `ctx` parameter.
- Use `db.QueryContext`, `db.QueryRowContext`, and `db.ExecContext`.

#### Prepared Queries (Security & Performance)

- Always use parameterized queries (`$1`, `$2`, etc. for PostgreSQL) to prevent SQL injection.
- Do not concatenate strings to build SQL queries.
  ```go
  const query = `SELECT id, name, created_at FROM {table_name} WHERE id = $1`
  row := r.db.QueryRowContext(ctx, query, id)
  ```

#### Error Wrapping

- Never ignore errors from `QueryRowContext.Scan` or `ExecContext`.
- Wrap errors with context using `fmt.Errorf("failed to fetch {entity} by id %d: %w", id, err)`.
- If an entity is not found, map `sql.ErrNoRows` to a domain-specific error if applicable (e.g., `domain.Err{Entity}NotFound`), or wrap it clearly.
  ```go
  var e domain.{Entity}
  err := row.Scan(&e.ID, &e.Name, &e.CreatedAt)
  if err != nil {
      if err == sql.ErrNoRows {
          return nil, fmt.Errorf("{entity} not found: %w", err) // or domain error
      }
      return nil, fmt.Errorf("scan error for {entity} %d: %w", id, err)
  }
  return &e, nil
  ```

## Critical Verification Checklist

- [ ] Is the interface defined in the `domain` package?
- [ ] Do all methods take `context.Context` as the first argument?
- [ ] Is PostgreSQL syntax used (`$1`, `$2`) for prepared statements?
- [ ] Are all database calls using the `*Context` variants (`ExecContext`, `QueryContext`)?
- [ ] Are all errors properly wrapped with `fmt.Errorf`?
- [ ] Are functions kept under 40 lines (extract mapping or query construction into private helpers if necessary)?
- [ ] Is the maximum of 3 parameters per function respected?
