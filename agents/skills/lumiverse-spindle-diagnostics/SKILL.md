---
name: lumiverse-spindle-diagnostics
description: Verify Lumiverse Spindle, browser DOM lifecycle, portal or extension-host integration with the repository's E2E diagnostics harness and a minimal mock host. Use when runtime mounting, state synchronization, rendering, or unmount/remount can regress.
---

# Lumiverse Spindle diagnostics

1. Read repository scripts and inspect `scripts/e2e-diagnostics`; don't assume scripts/paths exist in a different checkout. Use existing `bun run diagnose` or `bun run diagnose:spindle` when supported.
2. Define an observable user journey and the expected DOM/state/API result. Reproduce first, then test the fix on the same path.
3. For logic-only source/spindle changes, build a minimal realistic host fixture with mount targets, mocked APIs, persisted state and delayed/missing targets. Include null refs, desynchronization, stale callbacks and teardown/reinit.
4. Verify relevant browser modes: desktop, mobile and notched/PWA safe-top using Lumiverse's established layout variable. Cover portalled surfaces and theme scaling if affected.
5. Protect personal chats/characters/configuration/keys; use fixtures and scrub logs/screenshots.
6. Report each check separately as PASS, FAIL, BLOCKED or NOT RUN, with command, environment and evidence. A build pass is not an E2E pass.

If the harness fails to launch due to environment policy, report the blocker and still run narrower source/mock tests. Never invent browser coverage.
