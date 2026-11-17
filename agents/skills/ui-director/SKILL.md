---
name: ui-director
description: Orchestrate a broad UI/UX task spanning design, prototype, implementation, integration, or QA. Use when the request has multiple surfaces or unclear workflow boundaries. Do not use for a tiny isolated bugfix.
---


# UI director

Lead a coherent multi-step UI change; do not default to the ideology of smallest textual diff.

## Decide the UI task (after choosing `$work-pr` or `$work-extension`)

1. **Audit** for investigation or recommendations without a requested implementation.
2. **Prototype** for an interactive standalone mock awaiting design approval.
3. **Redesign** for an explicitly requested replacement of layout/interaction patterns.
4. **Integration** to wire an already approved interface to real data/actions.
5. **Repair** for a bounded functional or styling defect.

The primary ownership mode governs worktree and delivery; this UI task classification governs only the design procedure. If the user already approved a design and asked for implementation, do not restart design discovery. If they request a design first, do not modify the production app.

## Scope map before edits

- Read existing project instructions, architecture, relevant source and tests. Trace UI -> state -> command/API -> persistence for every affected control.
- Record **in scope**, **explicitly protected** (existing brand/assets/navigation/other surfaces), and **must still work** behaviors.
- Decide which files own the markup, styling, state transitions and remote/mobile variants.
- Define simple concrete acceptance conditions and likely failure modes.

## Direct the work

- Use the smallest number of *workflows* needed, not the smallest number of CSS lines. Refer to `$ui-audit`, `$ui-prototype`, `$ui-redesign`, `$css-refactor`, `$responsive-layout`, `$interaction-states`, `$visual-qa`, `$ui-integration`, `$surgical-ui-fix` when those skills are available and relevant.
- Once design work is authorized, allow purposeful component restructuring, CSS consolidation and deletion of poor prior layout; never pile overrides on an unsuitable structure.
- For backend-only tasks, freeze approved visual structure and route missing capabilities to backend work.

## Exit contract

Explain changed surfaces, preserved functionality, checks actually run, visual evidence, unresolved gaps and source/rollback instructions. Do not claim a mock proves backend functionality or a static test proves desktop rendering.
