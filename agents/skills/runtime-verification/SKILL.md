---
name: runtime-verification
description: "Use when unit tests or builds cannot prove behavior: browser/Tauri/PWA/extension lifecycle, integration APIs, focus, accessibility, persistence, and visual regressions. Collect actual evidence."
---

# Runtime verification — test what the user actually does

1. Reproduce the requested user journey and expected result. List failure modes rather than blindly running every test.
2. Use existing project test harness first; run focused tests before broad suites. For Lumiverse browser/Spindle checks prefer `scripts/e2e-diagnostics` and `bun run diagnose` / `bun run diagnose:spindle` when appropriate.
3. Build a minimum realistic mock environment: host/root DOM, API responses, state store, mount timing, async failures, missing refs and teardown. Verify desynchronization, repeated mounting and stale callbacks explicitly.
4. When UI is affected test mouse/touch, keyboard, focus restoration, inaccessible icon buttons, semantic names, mobile notched safe-top area, zoom, overflows, PWA persistence, portal overlays, multiple surfaces and close/reopen behavior.
5. Use personal/secret data only when explicitly needed and authorized; prefer fixtures, fake tokens, generated user content. Keep logs/screenshots free of private credentials.
6. Distinguish source inspection, syntax checks, unit tests, integration tests, visual screenshots and true live runtime checks. Do not claim one proves another.
7. Report each check with PASS / FAIL / BLOCKED / NOT RUN, command/harness, expected vs actual, environment and actionable missing evidence. A built bundle is not evidence that the button works.
