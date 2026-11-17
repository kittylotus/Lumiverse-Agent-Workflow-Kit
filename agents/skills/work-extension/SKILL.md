---
name: work-extension
description: Use for building, redesigning, integrating, or packaging a Lumiverse extension as an independently owned product. Full implementation/design liberty inside the extension, but never silently modify Lumiverse core.
---

# Extension mode — full liberty inside the extension boundary

**This is NOT PR mode.** The extension is an owned product surface: redesign components, reorganize folders, replace obsolete architecture, consolidate CSS, rewrite tests, update extension-owned types/assets/config and remove dead code when justified. Optimize for a cohesive working extension, not minimum changed lines.

For host-mount, Spindle, browser/PWA, and mock harness details, consult [references/lumiverse-host-lifecycle.md](references/lumiverse-host-lifecycle.md) as relevant.

## Host boundaries still matter

1. Identify the extension's actual repository/root, manifest, entrypoints, package scripts, lifecycle hooks, extension API and bundle/register semantics. Use `rg` and actual code.
2. Respect Lumiverse's *current public extension APIs*. Avoid reaching into private core internals or copying core implementation when an exposed primitive exists. Feature-gated or old Suite implementations are not recommended architecture.
3. Extension -> host calls should be deliberate and resilient (late/missing mount nodes, dynamic navigation, host rerenders, chat lifecycle). Do not mutate global DOM or styles broadly; scope extension classes, tokens, listeners and portals.
4. **Do not modify Lumiverse core** to unblock the extension without explicit authorization. If missing core functionality is genuinely necessary, report a separate core requirement/PR. Keep the two diffs and test reports distinct.
5. Honor user-approved design contracts and protected assets even with full freedom. For an approved redesign, restructure extension markup/CSS rather than piling patches.

## Product-quality workflow

- Map UI/data/state/persistence and existing behavior; establish the desired end state and which old structure is intentionally being replaced.
- Refactor **canonical CSS** in its owning source. Remove superseded selectors and duplicate media hacks. Preserve behavior while correcting architecture; no override layering.
- Model loading/empty/error/disabled states, race conditions, proper teardown/unload, remount, hot reload, persistence and missing optional host primitives.
- Test via realistic **mock Lumiverse host** with minimal DOM structure + lifecycle hooks. Cover host navigation, absence/arrival of mount points, repeated initialization, unmount, event listener cleanup, nullable refs and local-state desync.
- Run extension unit/build/lint/type checks, plus Lumiverse's actual E2E diagnostics when integration requires it (`scripts/e2e-diagnostics`, Playwright if available).
- Check mobile/PWA safe-area behavior using the existing Lumiverse safe-top primitive where the extension lives in that shell; no independent hardcoded notch approximation.
- Check keyboard/ARIA semantics and browser visuals for touched surfaces.

## Delivery

- Default for **extension overlay delivery:** full **cumulative editable extension source** with original relative paths (source, tests, scripts, assets, matching types, configs). Exclude node_modules, outputs, caches, private configs, personal runtime data.
- An **extension remains extension mode** even if its own repository uses PRs. If editing a separate upstream-maintained checkout, additionally follow the relevant live-worktree safeguards from `$work-pr`; do not sacrifice legitimate extension refactoring merely to minimize changed lines.
- Include a manifest, tests and rollback instructions; do not silently overwrite unrelated local work. When delivering code from chat, a ZIP with direct source is preferred over an installer.
- Explain any required host/core change as a separately scoped blocker; never sneak it into the extension package.

**Design freedom is not permission to break host isolation or user's approved art.**
