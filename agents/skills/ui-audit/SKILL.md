---
name: ui-audit
description: Audit an existing application or screen for UX friction, visual hierarchy, accessibility, layout failures, broken controls, and CSS debt. Use for screenshots, complaints about ugly design, or a design-quality review before deciding on changes.
---


# UI audit

Diagnose why a screen fails rather than prescribing cosmetic padding changes on instinct.

## Examine the real experience

- Look at the supplied screenshot(s) and actual source when available; note viewport size and whether this is a desktop, browser, mobile or embedded surface.
- Identify the user's primary task, the action frequency, the information users must scan, and which controls obstruct it.
- Review hierarchy, reading order, density, discoverability, status clarity, empty states, labels, contrast, icon consistency, and real content lengths.
- Check touch targets, keyboard flow, focus, dialogs, form validation, responsive clipping, horizontal scrolling and possible browser-default widgets.
- Trace failures to structure (DOM layout), CSS cascade/tokens, state logic, or backend wiring. Do not attribute every visual bug to CSS.

## Audit findings

For each finding provide: **symptom**, **evidence/selector or screenshot region**, **root-cause hypothesis**, **severity**, **recommended structural change**, and **verification method**. Distinguish confirmed source cause from visual inference.

Severity:
- **P0** broken workflow, inaccessible or data-loss issue;
- **P1** obscured action, overflow/collision, severe visual regressions;
- **P2** hierarchy/density inconsistency, confusing placement;
- **P3** optional polish.

## Recommendation style

- Present one coherent direction, not a dozen contradictory style patches.
- Preserve user-approved identity/assets where explicitly protected.
- Flag anti-patterns: multiple competing headers; giant form-like cards; controls disguised as decoration; decorative icons with low information value; fake working buttons; duplicated/conflicting CSS selectors.
- Recommend `$ui-prototype` when a direction needs approval or `$ui-redesign` when implementation is authorized.
