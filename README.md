# AI Collection

A centralized repository for AI assistant configurations, prompts, and automation scripts for various IDEs and services.

## Repository Structure

- **[core/](./core)**: The heart of the repository. Contains shared rules, skills, and workflows organized by domain.
  - **[general/](./core/general)**: Cross-cutting rules and tools (e.g., skill-creator).
  - **[frontend/](./core/frontend)**: UI/UX, React, CSS, and browser-specific logic.
  - **[backend/](./core/backend)**: Server-side logic, Databases, API design.
  - **[devops/](./core/devops)**: CI/CD, Docker, Infrastructure as Code.
- **[ides/](./ides)**: IDE-specific configuration files that reference the `core/` assets.
- **[cli/](./cli)**: Configuration files for AI CLI tools.
- **[prompts/](./prompts)**: A library of reusable templates.
- **[services/](./services)**: Instructions and settings for web-based services like Claude (Projects) and ChatGPT (Custom Instructions).
- **[scripts/](./scripts)**: Automation scripts for syncing settings across the system.

## Setup & Usage

### Antigravity
To use the Antigravity configurations, ensure the `.agent` directory is recognized by your project. If you are working in a different directory, you can create a symbolic link to the shared rules in this repository.

---
*Created with love for high-performance AI-assisted development.*
