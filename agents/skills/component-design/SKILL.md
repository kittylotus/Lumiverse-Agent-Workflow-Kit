---
name: component-design
description: Create or consolidate reusable UI components and design tokens such as headers, sidebars, modals, menus, tabs, buttons and form controls. Use when visual styles have drifted or shared CSS causes regressions.
---


# Component design system

Build coherent and reusable presentation without turning an entire application into one generic box component.

## Define the language

- Identify existing color, typography, spacing, border-radius, elevation, density, icon and focus conventions. Preserve approved identity when present.
- Establish small, expressive tokens; map existing component rules to tokens before inventing parallel constants.
- Identify where shared components belong versus where a specialized view needs its own layout.

## Core component contracts

- **Header**: one page title, meaningful contextual subtitle when useful, compact status and actions; no redundant bars.
- **Navigation**: high-density but readable, active/focus/hover states distinct; mobile drawer properly dismisses.
- **Dialogs**: deliberate header, content body, footer, escape/focus handling, clear destructive action. Avoid unstyled native prompt/confirm when design requires a themed experience.
- **Menus/dropdowns**: menu placement, click-away, keyboard navigation, `aria-*`, selected state, disabled item semantics, scroll boundaries.
- **Forms**: associated labels, validation, save/discard behavior, error feedback and unsaved changes flow.
- **Cards/list items**: clear information priority, stable widths, no icons-as-placeholders or truncation of vital names without a recovery affordance.

## Avoid

- Blindly applying one global `.button` or `.panel` style across unrelated components.
- Reimplementing the same modal/menu separately in each feature without a reason.
- Splitting CSS into patch layers rather than updating shared canonical rules and explicit variants.

## Confirm

Compare all component consumers before editing shared styles. Test keyboard/remote/mobile and error states. Report shared API and variant names so feature teams can consume them without CSS duplication.
