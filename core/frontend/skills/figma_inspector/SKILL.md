---
name: figma_inspector
description: Allows the agent to read precise dimensions, colors, and margins from Figma layouts.
---

# Figma Inspector Skill

This skill enables the agent to inspect Figma designs directly using the browser subagent to extract precise measurements, colors, and design tokens. This ensures pixel-perfect implementation and eliminates guesswork.

## Workflow

To use this skill, follow these steps:

1.  **Request Figma Link**: Ensure the user has provided a link to the Figma design or specific frame. If not, ask for it.
2.  **Launch Browser Subagent**: Use `browser_subagent` to open the provided URL.
3.  **Inspect Elements**:
    *   Instruct the browser subagent to wait for the design to load.
    *   If the design is in "View Only" mode, look for the "Inspect" panel (often on the right side).
    *   If "Dev Mode" is available, toggle it on.
    *   Click on the specific element(s) the user wants implemented.
    *   Taking a screenshot of the "Inspect" or "CSS" panel is highly effective for gathering all properties at once.
4.  **Extract Data**:
    *   **Dimensions**: Width, Height, Margin, Padding.
    *   **Typography**: Font Family, Size, Weight, Line Height, Letter Spacing.
    *   **Colors**: Hex codes, RGBA, or variable names.
    *   **Effects**: Shadows, Borders, Radius.
5.  **Apply to Code**:
    *   Translate the extracted values into the project's styling system (e.g., SCSS modules, Tailwind classes).
    *   Use exact values where appropriate, or map to existing theme tokens if they match (e.g., `spacing-4` for 16px).

## Example Browser Subagent Prompt

When invoking the browser subagent, use a prompt like this:

> "Navigate to [Figma URL]. Wait for the design to load. Locate the [Element Name/Description]. Click on it to select it. Look for the 'Inspect' or 'Code' tab on the right sidebar. Take a high-resolution screenshot of the CSS/Properties panel so I can see the exact values for width, height, color, and typography. If you can, copying the CSS text would also be helpful."

## Troubleshooting

*   **Login Required**: If the Figma file is private, the browser subagent might hit a login screen. Ask the user if they can provide a public link or if they want to guide the agent through login (which might be security sensitive).
*   **Canvas vs. HTML**: Figma renders on a canvas, so standard DOM inspection tools won't work for the design elements themselves. You MUST rely on the Figma UI's "Inspect" or "Dev Mode" panels to get the data.
*   **Complex Components**: For complex components, ask the browser subagent to inspect the parent container first, then child elements, to understand the layout structure (Flex/Grid).
