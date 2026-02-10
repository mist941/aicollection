# AI Collection 🚀

A modularized, domain-driven repository for AI assistant configurations. This setup separates **domain knowledge** from **tool-specific implementation**.

## Architecture Philosophy

### 🧠 Core (The Knowledge)
Located in [`/core`](./core), this directory contains the global "Source of Truth" for your engineering standards.
- **Frontend**: Best practices for UI/UX, React, CSS, and modern web.
- **Backend**: API design, Database schemas, and Server-side logic.
- **DevOps**: CI/CD, Containerization, and Infrastructure.

### 🛠 IDEs (The Adapters)
Located in [`/ides`](./ides), these are entry points for specific tools (Antigravity, Cursor, etc.). They reference the `core/` knowledge but format it for the specific IDE's features (like skills or custom workflows).

---

## Repository Structure

- **[core/](./core)**: Shared domain assets (Rules, Skills, Workflows).
- **[ides/](./ides)**: IDE-specific configurations and adapters.
- **[cli/](./cli)**: Configs for AI terminal tools (Aider, etc.).
- **[prompts/](./prompts)**: A library of raw, reusable system prompts.
- **[services/](./services)**: Settings for Claude Projects, ChatGPT Custom Instructions, etc.
- **[scripts/](./scripts)**: Automation tools for environment syncing.

## How to Use

1. **Developing Core Knowledge**: Use rules in `core/` to improve AI performance across all tools.
2. **Tool Integration**: Use the adapters in `ides/` to bring your core knowledge into your favorite editor.
3. **Automation**: Use scripts in `scripts/` to symlink or copy configs into your local projects.

---
*Built for the future of AI-native software engineering.*
