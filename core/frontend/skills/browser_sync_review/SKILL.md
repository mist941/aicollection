---
name: browser_sync_review
description: Automated visual review of localhost, comparing it against design specs. Detects layout shifts, responsiveness issues, and visual bugs.
---

# Browser Sync Review Skill

This skill empowers the agent to act as a QA engineer, visually inspecting the running application on `localhost` to ensure it matches the design and behaves correctly across different devices.

## Workflow

### 1. Preparation
- **Verify Server**: Ensure the local development server is running (e.g., `npm run dev`). If not, ask the user to start it or start it yourself (if safe).
- **Get Reference**: Obtain the target design reference (Figma link, screenshot, or detailed description).

### 2. Browser Inspection (The "Look")
- **Launch Subagent**: Use the `browser_subagent` tool to visit the local URL (typically `http://localhost:3000` or similar).
- **Responsive Checks**:
  - **Desktop**: Set the window size to a standard desktop width (e.g., 1440px or 1920px). Take a screenshot.
- **Capture State**: Ensure screenshots capture the relevant UI states (hover, active, etc.) if that's what's being tested.

### 3. Visual Analysis (The "Compare")
- **Layout Integrity**:
  - Does the mobile view have unwanted horizontal scrolling?
  - Are elements overlapping or cut off?
  - Is the spacing consistent with the Atomic Design system?
- **Figma Comparison**:
  - Compare the `localhost` screenshot with the known design (from `figma_inspector` or user uploads).
  - Note differences in:
    - **Typography**: Check for correct font family, size, weight, and line-height.
    - **Spacing**: Check if margins and paddings match the design tokens.
    - **Colors**: Verify that primary, secondary, and accent colors are accurate.
    - **Alignment**: Ensure grids and flex alignments are respected.

### 4. Reporting
- **Discrepancy Report**: List specific visual bugs found with clear descriptions.
  - *Example*: "On mobile (375px), the header logo overlaps the hamburger menu."
  - *Example*: "The hero button padding is 12px, but design specifies 16px."
- **Action Plan**: Propose code fixes (CSS/SCSS adjustments) to resolve the identified issues immediately.

## Example Browser Subagent Prompt

> "Navigate to http://localhost:3000. Wait for the page to load completely.
> 1. Resize window to 1440x900. Take a screenshot named 'desktop_view'.
> 2. Check for any horizontal scrollbar on mobile.
> 3. Return the screenshots and any observation about layout shifts."
