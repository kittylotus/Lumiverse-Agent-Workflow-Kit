---
name: ui-redesign
description: Redesign and implement an ugly, cramped, or incoherent application interface. Use when the user explicitly authorizes substantial visual or structural changes; allow necessary component and CSS rewrites while preserving protected behavior.
---


# UI redesign

**Goal: a substantially better finished interface, not a tiny diff.** Minimal-change discipline belongs to maintenance, not approved design rehabilitation.

## Sequence

1. Locate the current markup, CSS owner, scripts/components, state/commands, matching desktop/remote versions and tests. Identify the real user tasks.
2. Extract any approved mockup requirements. If the user already approved a prototype, implement it faithfully rather than offering alternative aesthetics.
3. Rebuild information hierarchy before styling: page header, navigation, primary action, content density, contextual commands, details, feedback, empty/error states.
4. **Replace** unsuitable layout wrappers, deeply nested forms, duplicate panels and excessive per-item controls. Introduce component boundaries where they clarify responsibility.
5. Implement a canonical CSS/token structure; edit existing rules where appropriate; delete superseded markup and selectors. Use `$css-refactor` principles—not appended counter-rules.
6. Handle mobile, desktop, long names, zoom, focus, keyboard, reduced motion, and realistic data.
7. Reconnect every previously working action; add explicit tests for state and APIs. Do not silently replace backend behavior with demo content.
8. Run visual and integration verification before calling work complete.

## Design quality bar

- Clarity outranks decoration; density is intentional, not an accidental byproduct of tiny fonts.
- One dominant title/header; controls grouped by importance; restrained typography; distinguish content from admin forms.
- Consistent modal and dropdown language; avoid unstyled browser defaults where a custom control is requested, but preserve accessibility.
- Artwork and icons carry meaning; don't replace protected brand or persona art without consent.

## Handoff

List replaced components, deleted obsolete CSS, preserved command contract, responsive breakpoints, test outcomes, and evidence. Distinguish unresolved visual gaps from verified behavior.
