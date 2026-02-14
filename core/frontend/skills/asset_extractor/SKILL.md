---
name: asset_extractor
description: Automates the extraction of icons and images from Figma directly into the src/assets folder.
---

# Asset Extractor Skill

This skill streamlines the process of getting assets from design files (Figma) into the codebase. It handles the identification, download, optimization, and placement of image and icon assets.

## Workflow

### 1. Asset Identification
- **Locate in Figma**: Use the `figma_inspector` skill or user instructions to identify the specific assets (icons, illustrations, photos) needed.
- **Determine Format**:
  - **Icons**: Prefer SVG for scalability and meaningful code structure.
  - **Images**:
    - **Photos**: Use WebP or JPG (optimized).
    - **Transparent**: Use PNG or WebP.
  - **Naming**: Establish a strict naming convention (e.g., `kebab-case`, `icon-[name].svg`).

### 2. Extraction Process
- **Browser Subagent**: Navigate to the Figma file.
- **Select & Export**:
  - Select the asset.
  - Look for the "Export" section in the right sidebar.
  - Choose the correct format/scale (e.g., 1x for photos, SVG for icons).
  - **Action**: Since the browser subagent cannot "download" files to the local disk directly in a way that is easily accessible to the agent in all environments, the primary method is:
    - **SVGs**: Copy the "Copy as SVG" code directly from Figma.
    - **Images**: Get the image URL (if public/accessible) or ask the user to provide the direct link/file if authentication prevents direct download. *Alternatively, take a high-res screenshot of the specific element if it's simple enough, though this is a fallback.*

### 3. Implementation
- **SVGs**:
  - Create a new file in `src/assets/icons/` (or appropriate folder).
  - Paste the SVG code.
  - **Optimization**: Clean up the SVG (remove `width`, `height`, `fill` if needed for CSS control).
- **Images**:
  - If a URL is obtained, use `run_command` with `curl` or `wget` to download it to `src/assets/images/`.
  - Example: `curl -o src/assets/images/hero-bg.webp [URL]`

### 4. Integration
- **Export**: Add the new asset to `src/assets/index.ts` (if a barrel file exists).
- **Usage**: Provide a snippet of how to import and use the asset in a component.

## Example Browser Subagent Prompt for SVG

> "Navigate to definition of 'Search Icon' in Figma. Right-click the icon > 'Copy as SVG'. Return the SVG code string."

## Automation Script (Future Enhancement)
*If a Figma API key is available, a script could be added here to use `curl` against the Figma API to download nodes programmatically.*
