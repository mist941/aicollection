---
name: go-api-security
description: Adds automatically to API handlers: request validation, input sanitization, rate limiting middleware, and an auth middleware placeholder.
---

# Go API Security Skill

This skill automatically enforces essential security measures across Go API endpoints by implementing request validation, input sanitization, rate limiting, and integrating an authentication middleware placeholder.

## Execution Steps

When securing an existing API feature or creating a new one, strictly follow these steps to integrate security components without violating the Clean Architecture rules (especially keeping business logic out of the `transport` layer).

### 1. Request Validation (Transport Layer)

- Validate incoming DTOs immediately in the `transport` layer (HTTP Handler).
- Do not let invalid data reach the `service` or `domain` layers.
- If validation fails, return an HTTP 400 Bad Request immediately.
- Use an established validation library (e.g., `go-playground/validator`) or implement structured custom validation methods directly on the DTO structs.
  ```go
  // Example validation on a DTO
  func (r *Create{Entity}Request) Validate() error {
      if len(r.Name) < 3 {
          return fmt.Errorf("name must be at least 3 characters")
      }
      return nil
  }
  ```

### 2. Input Sanitization (Transport Layer)

- Sanitize inputs to prevent XSS or unexpected characters _before_ calling the service layer.
- Use functions like `html.EscapeString` or string trimming directly inside the handler mapping phase (or inside a sanitized request DTO method).
  ```go
  func (h *{Entity}Handler) Create(w http.ResponseWriter, r *http.Request) {
      // Decode, Validate...
      req.Name = strings.TrimSpace(html.EscapeString(req.Name))
      // Call Service...
  }
  ```

### 3. Rate Limiting Middleware (Transport Layer Routing)

- Implement or attach a rate limiting middleware at the router level.
- Ensure the middleware uses `context.Context` effectively (if applicable) and returns HTTP 429 Too Many Requests when limits are exceeded.
- Place it before business-heavy routes.
  ```go
  // Example wiring structure
  func SetupRoutes(r Router, handler *transport.{Entity}Handler) {
      // Assuming a RateLimit middleware exists
      protected := r.Group("/api/secured").Use(middleware.RateLimit(100, time.Minute))
      protected.POST("/{entity}", handler.Create)
  }
  ```

### 4. Auth Middleware Placeholder

- Add an authentication middleware placeholder to protect endpoints.
- The middleware should extract the identity (e.g., from a JWT or session token), validate it, and inject the user context into the request context `context.WithValue`.
- If authentication fails, return HTTP 401 Unauthorized.

  ```go
  package middleware

  import (
      "net/http"
      "context"
  )

  // AuthMiddleware is a placeholder for authentication logic.
  func AuthMiddleware(next http.Handler) http.Handler {
      return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
          // TODO: Extract token, validate, and get user identity
          // token := r.Header.Get("Authorization")
          // if !isValid(token) { http.Error(w, "Unauthorized", http.StatusUnauthorized); return }

          // ctx := context.WithValue(r.Context(), "userID", userID)
          // next.ServeHTTP(w, r.WithContext(ctx))

          next.ServeHTTP(w, r)
      })
  }
  ```

- Make sure to wrap the relevant routes with this middleware during router registration.

## Critical Verification Checklist

- [ ] Is validation occurring exclusively in the `transport` layer before the service is called?
- [ ] Are inputs being sanitized against XSS or extra whitespace before being passed to the service layer?
- [ ] Is the rate limiter middleware attached to the correct endpoint routes?
- [ ] Is an authentication middleware stub present and correctly attached to protected routes?
- [ ] Are all handlers still under 40 lines after adding validation and sanitization calls? (Extract parsing/validation to private functions if needed).
- [ ] Are dependencies injected via constructor (no `init()`, no global state)?
