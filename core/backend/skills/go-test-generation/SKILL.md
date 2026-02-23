---
name: go-test-generation
description: Generates service unit tests, repository integration tests, and HTTP handler tests in Go.
---

# Go Test Generation Skill

This skill generates robust tests for Go applications, specifically targeting services, repositories, and HTTP handlers. It adheres strictly to the project's clean architecture and code style guidelines.

## 1. Service Unit Tests (`service/{entity}_service_test.go`)

- **Scope:** Pure business logic.
- **Rules:**
  - Mock the repository interface (e.g., using `golang/mock` or manual mock structs).
  - Do NOT connect to a real database.
  - Test validation rules, error handling, and business calculations.
  - Test both success (happy path) and failure (error) scenarios.
- **Example Pattern:**
  ```go
  func Test{Entity}Service_Create(t *testing.T) {
      // 1. Arrange: Setup mock repository and service
      mockRepo := new(Mock{Entity}Repository)
      svc := New{Entity}Service(mockRepo)
      ctx := context.Background()

      // 2. Act: Call the service method
      // err := svc.Create(ctx, validEntity)

      // 3. Assert: Verify expectations and results
      // assert.NoError(t, err)
  }
  ```

## 2. Repository Integration Tests (`repository/{entity}_repository_test.go`)

- **Scope:** Database queries and data persistence.
- **Rules:**
  - Use a real test database (e.g., PostgreSQL via `testcontainers-go` or a dedicated test DB).
  - Use `context.Context` (with timeouts if necessary).
  - Verify that records are correctly inserted, updated, deleted, and retrieved.
  - Test edge cases like "not found" (`sql.ErrNoRows`).
- **Example Pattern:**
  ```go
  func Test{Entity}Repository_GetByID(t *testing.T) {
      // 1. Arrange: Setup DB connection, create test data
      db := setupTestDB(t)
      repo := New{Entity}Repository(db)
      ctx := context.Background()

      // 2. Act: Execute the repository query
      // entity, err := repo.GetByID(ctx, testID)

      // 3. Assert: Verify the returned entity matches DB contents
      // assert.NoError(t, err)
      // assert.Equal(t, expectedName, entity.Name)
  }
  ```

## 3. HTTP Handler Tests (`transport/{entity}_handler_test.go`)

- **Scope:** Request parsing, validation, and response formatting.
- **Rules:**
  - Use `net/http/httptest` to create mock HTTP requests and responses.
  - Mock the service layer (do not execute real business logic or DB calls).
  - Verify HTTP status codes (e.g., 200 OK, 400 Bad Request, 201 Created).
  - Verify JSON request mapping and response serialization.
- **Example Pattern:**
  ```go
  func Test{Entity}Handler_Create(t *testing.T) {
      // 1. Arrange: Setup mock service and handler
      mockSvc := new(Mock{Entity}Service)
      handler := New{Entity}Handler(mockSvc)

      reqBody := `{"name": "Test"}`
      req := httptest.NewRequest(http.MethodPost, "/api/{entity}", strings.NewReader(reqBody))
      req.Header.Set("Content-Type", "application/json")
      rec := httptest.NewRecorder()

      // 2. Act: Serve the HTTP request
      // handler.Create(rec, req)

      // 3. Assert: Check status code and response body
      // assert.Equal(t, http.StatusCreated, rec.Code)
  }
  ```

## Critical Constraints to Verify

- **Layer Isolation:** Are handlers isolated from DB? Are services isolated from HTTP?
- **Error Handling:** Are tests checking for specific, wrapped errors where appropriate?
- **Context Usage:** Is `context.Background()` or `context.TODO()` initialized and passed correctly in tests?
- **Clean Code:** Are test functions concise? Reusable setup logic should be extracted into helper functions `< 40 lines`.
