#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Provide an elite-level description for the Antigravity dispatch system. Clearly state what this skill enables and the specific contexts/triggers for activation.]
---

# {skill_title}

## Overview
[TODO: 1-2 powerful sentences describing the strategic value of this skill.]

## Strategic Framework
[TODO: Define the core workflow or capability set. Choose a pattern that ensures maximum performance:

**1. Strategic Workflow** (Sequential excellence)
- For multi-phase processes requiring deep focus.
- Structure: ## Overview → ## Phase 1: Context Capture → ## Phase 2: Execution → ## Phase 3: Validation

**2. Tactical Capabilities** (Task-oriented collections)
- For versatile toolsets.
- Structure: ## Overview → ## Quick Start → ## Capability A → ## Capability B

**3. Domain Sovereignty** (Knowledge-heavy specifications)
- For project-specific or industry-specific deep context.
- Structure: ## Overview → ## Specifications → ## Operational Guidelines

Patterns can be integrated. Most elite skills combine tactical capabilities with a strategic workflow for complex operations.]

## [TODO: Primary Operational Section]
[TODO: Implement the core logic here. Use high-density examples, strategic decision trees, and direct references to bundled resources.]

## Elite Resources
This skill leverages a suite of optimized resources:

### scripts/
High-performance code for deterministic excellence.
- **Example**: `scripts/optimization_engine.py` - Core logic for data transformation.

### references/
Deep-context specifications and documentation.
- **Example**: `references/api_specification.md` - Complete technical reference.

### assets/
Premium templates and boilerplate.
- **Example**: `assets/starter_template/` - Pre-configured project structure.

---

**Efficiency Note:** Remove any resources or sections that do not contribute to Antigravity's operational success.
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Performance Script for {skill_name}

This script provides deterministic logic for specialized operations.
Replace with actual implementation.
\"\"\"

def main():
    print("Executing Antigravity optimized logic for {skill_name}")
    # TODO: Implement high-performance logic here

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Technical Specification: {skill_title}

This document provides the deep-dive technical context required for elite execution.
Replace with actual specifications.

**Antigravity Note:** Use this for information that is too dense for the main SKILL.md.
"""

EXAMPLE_ASSET = """# Antigravity Asset Placeholder

This represents a premium asset or boilerplate configuration.
Replace with actual templates, images, or project directories.

**Workflow Integration:** Antigravity uses these assets to bootstrap high-fidelity output.
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with template SKILL.md.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md from template
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create resource directories with example files
    try:
        # Create scripts/ directory with example script
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        example_script = scripts_dir / 'example.py'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("✅ Created scripts/example.py")

        # Create references/ directory with example reference doc
        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        example_reference = references_dir / 'api_reference.md'
        example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/api_reference.md")

        # Create assets/ directory with example asset placeholder
        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        example_asset = assets_dir / 'example_asset.txt'
        example_asset.write_text(EXAMPLE_ASSET)
        print("✅ Created assets/example_asset.txt")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # Print next steps
    print(f"\\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print("2. Customize or delete the example files in scripts/, references/, and assets/")
    print("3. Run the validator when ready to check the skill structure")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\\nSkill name requirements:")
        print("  - Kebab-case identifier (e.g., 'my-data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 64 characters")
        print("  - Must match directory name exactly")
        print("\\nExamples:")
        print("  init_skill.py my-new-skill --path skills/public")
        print("  init_skill.py my-api-helper --path skills/private")
        print("  init_skill.py custom-skill --path /custom/location")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print()

    result = init_skill(skill_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
