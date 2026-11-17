---
name: ui-integration
description: Wire an already approved UI to real APIs, filesystem, persistence, process control or backend commands while preserving its design. Use for integration audits, missing hooks, backend state mismatches, remote/PWA parity, and save/load flows.
---


# UI integration — visuals frozen unless explicitly reopened

Approved design is an API contract for the user's eyes. Backend work should not silently redesign it.

## Trace every control

Build a mapping: **UI control -> handler -> IPC/fetch/service -> backend command -> response -> UI state -> persistence**. Inventory missing hooks and error cases before editing.

## Implement carefully

- Keep approved DOM class names and CSS as stable as possible. When new states are required, use existing design-system variants; don't add an ugly form as a workaround.
- Never substitute canned demo data for real results. Don't interpret placeholder state as persisted.
- Save operations must handle validation, authorization, errors, round-trip reload and unexpected backend responses.
- Secure secrets (never put credentials into logs/snapshots), validate paths and permissions at the backend boundary, and respect desktop/remote feature differences.
- Show status only from real probes/health results. Avoid globally “alive” defaults.
- Mirror behavior across client variants where intended; verify that packaging, asset serving, caching and route exposure work in the real runtime.
- If required backend work does not exist, report the gap and implement a real contract if authorized; do not fabricate an editable control that silently fails.

## Test evidence

Use minimal realistic fixtures for integration tests: successes, null/empty values, stale races, timeout, backend errors, missing permissions and persistence after reload. Exercise touched app controls manually where environment permits. Hand off a PASS/FAIL/BLOCKED tracker and list every remaining backend dependency.
