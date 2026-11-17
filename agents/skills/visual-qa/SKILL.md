---
name: visual-qa
description: Verify UI appearance and interactions against approved references across desktop, mobile and browser/embedded surfaces. Use after redesigns or when regressions appear; combine screenshot review, Playwright if available, accessibility and regression tests.
---


# Visual QA and regression evidence

A clean build is not a screenshot. A mock API success is not live integration.

## Collect evidence

- Identify approved DOCTYPE/screenshot and actual target devices/containers. Record viewport size, pixel ratio/zoom, theme and actual runtime (browser, PWA, Tauri, embedded webview).
- Use existing project browser diagnostics/playwright harness before adding dependencies. Take consistent screenshots of main screen, dialogs, drawers, menu open, empty/loading/error and long-content states.
- Compare layout, icon placement, title hierarchy, background blend, corner treatment, scroll regions, typography, clickable hit areas and responsive overflow.
- Check display of native dialogs or unstyled controls; verify state and focus behavior, not merely the screenshot.

## Regression matrix

At minimum cover small phone, typical phone, tablet-ish width, desktop, and shortest supported window. For each: header fits, navigation works, cards fully visible, modals reachable, no horizontal overflow, actionable controls centered, scrolling boundaries correct.

## Test behavior

- Keyboard tab order, Enter/Space, Escape, focus visibility, tooltips as needed, screen-reader labels, reduced motion.
- Commands and API paths via mocks plus live integration when possible. Test success, offline, timeout, permission denied, 0 items and large lists.
- No skipped PWA/remote surface simply because desktop passed.

## Reporting

Explicitly mark each check **PASS / FAIL / BLOCKED / NOT RUN**. Include reproducible failures, affected screenshots, files, and whether the test is static, mock-browser, real-browser or live backend. Never claim a Chromium render or Windows/Tauri test if it was blocked or unavailable.
