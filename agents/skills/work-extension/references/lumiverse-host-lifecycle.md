# Lumiverse extension · host and lifecycle contract

Use with `$work-extension` when the task touches host APIs, Spindle integration, portals, mounting, navigation, or remote/mobile behavior. Extensions are product-owned: **refactor freely inside the extension boundary**, not inside Lumiverse core.

## Before designing or editing

- Find the extension manifest, entrypoint, registration, extension API version, build script and host integration points. Prefer documented/current host APIs and public primitives over private core DOM or copied internals.
- Trace activation, asynchronous availability, route/chat changes, host rerenders, disable/unload and remount. Look for duplicate global listeners, orphaned observers, timers or overlays.
- Map extension-owned UI, state, storage, assets, type declarations, tests and mobile/desktop variants. Decide which old components/CSS are to be replaced rather than overridden.
- CSS ownership remains scoped: one canonical rule per component/state/breakpoint as appropriate; no unbounded global selectors or bottom-of-file specificity towers.

## Minimum viable host fixture

A small deterministic mock Lumiverse host should demonstrate at least:

1. initial mount when targets are already present;
2. initial mount when host elements arrive late;
3. missing/nullable optional references;
4. navigation and return/remount;
5. disable/unload cleanup and repeat initialization without duplicate listeners;
6. state persistence and rehydration versus rendered DOM;
7. async failure/stale result after view changes;
8. mobile/desktop variance if the surface is shared.

For Spindle/source changes, build a fixture that validates the real pipeline path rather than a single mocked helper returning its own expected value.

## Real-browser and PWA verification

Use Lumiverse's existing `scripts/e2e-diagnostics` Playwright harness when available and relevant. Check `bun run diagnose` and `bun run diagnose:spindle` against actual repository scripts. Verify visible interactions, keyboard focus, touch controls, scrolling, safe-top/notched-PWA constraints, extension activation/deactivation, and the host's actual layout and theme classes. Don't claim this passed if only syntax/tests ran.

## Boundary rule

If the extension needs a missing Lumiverse core API, describe the smallest public primitive and propose a separate core change. Never silently patch core as a convenience. Conversely, do not import Suite-era legacy abstractions into modern extension architecture. A separately reviewed core PR uses `$work-pr` safeguards.

## Delivery

For a user-controlled extension overlay: full **cumulative editable extension source** with original relative paths, including relevant types, tests, scripts, assets and configs. Exclude generated output, caches, dependencies and secrets. For a request to contribute code through an upstream PR, clarify delivery and preserve worktree ownership; extension design freedom still applies within the extension.
