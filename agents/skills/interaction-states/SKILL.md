---
name: interaction-states
description: Specify and implement meaningful UI behavior and state transitions. Use for buttons that do nothing, incorrect online indicators, edit/save/discard flows, modal behavior, filters, async races, loading/error/empty states.
---


# Interaction states and truthfulness

Every control needs a credible contract: **user action -> state transition -> backend effect (if any) -> visible feedback -> persisted result**.

## State inventory

For each touched control record: idle, hover/focus, disabled, loading/pending, success, failure, empty, offline, no permission, stale, and selected states where relevant.

## Behavioral rules

- Do not display “connected”, “saved”, “online”, “open”, “running” or “completed” by default without evidence from a real source.
- Opening a panel with expensive/untrusted content can be opt-in; when returning, unmount or release that resource if the contract requires it.
- When saving, validate inputs; handle requests failing, retrying, rapid repeated taps, stale responses, duplicate dispatch and route changes.
- Keep mutations transactional when possible. Preserve edits until confirmed, or offer deliberate discard confirmation.
- Filters/search must show accurate counts, search results and no-result states. Approximate search fallback must be labeled as a fallback, not a fabricated exact match.
- Modals and menus need keyboard, Escape, focus management, click-away and accessible names.

## Verification

Use real or minimal mock API fixtures to test data flow, null refs, delayed responses, partial failure, reconnect, repeat interaction and reload. A DOM presence test alone is not functional verification. Report any backend contract that is missing rather than faking it.
