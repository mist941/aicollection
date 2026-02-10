---
name: skill-creator
description: Elite guide for architecting high-performance skills within the Antigravity IDE. Use this when you need to extend Antigravity's capabilities with specialized domain knowledge, complex workflows, or custom tool integrations.
license: Complete terms in LICENSE.txt
---

# Antigravity Skill Creator

This skill provides the architectural framework for building elite-tier skills designed specifically for the Antigravity IDE.

## About Skills in Antigravity

Skills are modular, self-contained intelligence packages that extend Antigravity's native capabilities. They serve as "procedural onboarding guides" for specific domains, transforming Antigravity from a general-purpose powerhouse into a specialized elite agent equipped with deep context and optimized workflows.

### The Power of Antigravity Skills

1. **Strategic Workflows** - Advanced, multi-phase procedures for specialized domains (e.g., deep-dive security audits, complex UI/UX design systems).
2. **Advanced Tool Integrations** - Directives for leveraging Antigravity's toolset (Browser Subagent, Command Execution, File Manipulation) for maximum efficiency.
3. **Domain Sovereignty** - Deep, project-specific or industry-specific knowledge, schemas, and proprietary logic.
4. **Rich Resource Bundles** - Integrated scripts, reference specifications, and premium assets that ensure deterministic excellence.

## Core Architectural Principles

### Precision & Token Efficiency
The context window is a premium resource. Antigravity skills are designed to be surgically precise. Only add information that Antigravity cannot infer through its advanced reasoning or find through its research tools.

**Axiom: Antigravity is exceptionally intelligent.** Challenge every line: "Is this essential for execution?" or "Can Antigravity derive this independently?" Use concise, high-density examples over verbose explanations.

### Calibrated Degrees of Freedom
Match the level of prescription to the task's complexity and sensitivity:

**Autonomous (Text-based instructions)**: For creative or heuristic-heavy tasks where multiple high-quality outcomes are valid.

**Guided (Pseudocode/Parameterized scripts)**: For tasks where a gold-standard pattern exists but requires contextual adaptation.

**Deterministic (Specific scripts/Fixed sequences)**: For fragile, mission-critical operations where zero variance is acceptable.

Think of Antigravity as a master artisan: provide the blueprints for the standard work, but allow the space for masterful execution where appropriate.

### Anatomy of an Antigravity Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required) - kebab-case identifier
│   │   └── description: (required) - the elite triggering mechanism
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - High-performance executable code (Python/Bash)
    ├── references/       - Deep-dive documentation and specifications
    └── assets/           - Premium templates, boilerplate, and binary assets
```

#### SKILL.md (The Intelligence Core)

The `SKILL.md` is the heartbeat of the skill. It contains:
- **Frontmatter**: High-density metadata used by Antigravity's dispatch system to identify triggering opportunities.
- **Body**: Strategic guidance and operational procedures.

#### Bundled Resources (The Execution Layer)

##### Scripts (`scripts/`)
Use for tasks requiring deterministic reliability, heavy data processing, or complex file manipulations.
- **Integration**: Antigravity can execute these scripts directly to solve complex problems without manual user intervention.

##### References (`references/`)
For deep specifications, API docs, or domain-specific knowledge items.
- **Antigravity Synergy**: Use these to keep `SKILL.md` lean. Antigravity will proactively research these files using `view_file` or `grep_search` when the context demands it.

##### Assets (`assets/`)
Templates, boilerplate projects, and binary files.
- **Workflow**: Antigravity uses these to bootstrap new projects or provide high-fidelity output (e.g., logo assets, brand templates).

## The Progressive Disclosure Strategy

Antigravity uses a layered loading system to maintain peak performance:

1. **Phase 1: Discovery (Metadata)** - Antigravity scans name and description.
2. **Phase 2: Activation (SKILL.md body)** - Loaded only when the skill is the optimal tool for the job.
3. **Phase 3: Deep Context (Bundled Resources)** - Accessed dynamically as the task unfolds.

**Key Principle:** Keep `SKILL.md` under 500 lines. If complexity exceeds this, partition it into `references/` files and provide a "Strategic Overview" in the main body.

### Antigravity & Knowledge Items (KIs)
Skills should be designed to complement the Antigravity **Knowledge Item** system. While KIs capture distilled project knowledge, Skills provide the **procedural recipes** to act on that knowledge.

## Professional Workflow

1. **Strategic Discovery**: Understand the user's ultimate goal through high-fidelity examples.
2. **Capability Planning**: Identify which scripts, references, and assets will provide the biggest performance leap.
3. **Initialization**: Execute `init_skill.py` to bootstrap the folder structure.
4. **Architectural Implementation**: Write the procedures and implement the resources.
5. **Quality Assurance**: Use `quick_validate.py` and perform real-world test runs.
6. **Packaging**: Run `package_skill.py` to create the final `.skill` artifact.
7. **Iterative Refinement**: Evolve the skill based on live performance data.

### Step-by-Step Execution

#### Step 3: Initialization
Run the elite initializer to ensure perfect compliance with Antigravity standards:
```bash
python .agent/skills/skill-creator/scripts/init_skill.py <skill-name> --path <destination>
```

#### Step 5: Validation & Packaging
Once the skill meets the Antigravity standard of excellence, package it:
```bash
python .agent/skills/skill-creator/scripts/package_skill.py <path/to/skill>
```

## Professional Excellence
Antigravity skills must look and feel premium. Avoid placeholders. Use clean, semantic Markdown. Maintain a tone of professional collaboration and technical mastery.
