---
name: ui-prototype
description: Create a standalone interactive HTML/DOCTYPE UI prototype as a design contract before implementation. Use for exploratory mockups, clickable desktop/mobile layouts, and user approval; not for production backend integration.
---


# UI prototype (DOCTYPE laboratory)

Produce an interactive, inspectable design contract rather than a static screenshot with fake affordances.

## Build

- Use existing approved screenshots or project visual language when supplied; otherwise establish a compact design system with color, typography, spacing, border and component rules.
- Prefer a **self-contained HTML file** with inline CSS and JavaScript and no production dependencies if the user wants a portable DOCTYPE.
- Support realistic mock data with varying lengths, missing values and empty/loading/error states.
- Wire every visible control to an honest mock behavior: tabs switch, filters search, dialogs open/close, menu actions produce visible feedback, keyboard interactions work. Label simulated data and operations as demo.
- Show desktop and mobile in the same responsive document, with accessible interactions (labels, focus, Escape for dialogs, reduced-motion handling).
- Use distinct component structure and reusable tokens. Avoid an append-only style section of compensating CSS at the bottom.

## Design contract

Document exactly what is approved: information architecture, desktop/mobile placement, navigation, interaction states, protected art/brand assets, data that must come from the real app, and prohibited regressions.

## Do not

- Replace production real backend state with demo data.
- Claim the mock implements persistence or system commands.
- Generate decorative artwork unless asked for it or included in the design brief.
- Use HTML mock buttons that do nothing while implying working features.

## Verify

Open locally at target widths if browser tooling works; try search, tabs, menus, dialogs, focus, empty states and mobile overflow. If a browser is blocked, run static checks and clearly mark visual QA unverified.
