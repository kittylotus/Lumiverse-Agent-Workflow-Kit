---
name: work-pr
description: Use for a live upstream/core pull request, for Lumiverse core. Protect the Git worktree, keep the change surgical and reviewable, and deliver only changed files. Do not use for standalone apps or self-owned extensions.
---

# PR mode — a reviewer must understand the diff

**PR means a change intended for review and merge into someone else's maintained core, especially Lumiverse.** Git presence alone is not enough. The worktree is user-owned state, never disposable. Smallest **complete** change means no weak hacks, not an arbitrary line-count limit. If the requested PR itself is a redesign, make the necessary bounded structural changes.

For detailed Lumiverse-specific situations (Suite, dirty checkout, iPhone safe top, package scripts), read [references/lumiverse-pr-review.md](references/lumiverse-pr-review.md) as relevant. This skill sets mandatory boundaries; the reference gives deeper procedures.

## Preflight before any writes

1. Inspect actual root, state, branch, tracking and remotes:

   ```powershell
   git rev-parse --show-toplevel
   git status --short
   git status -sb
   git branch --show-current
   git branch -vv
   git remote -v
   ```

2. Read repository CONTRIBUTING/rules, neighboring implementation, tests and actual extension boundaries. Use `rg`, not `grep`/recursive PowerShell emulation.
3. Determine **core vs extension ownership** and the intended base/branch from facts, not assumptions (`origin`, `upstream`, `staging` may vary).
4. Inspect existing dirty changes. For files you must touch, `git diff -- path/to/file`. If ownership/anchors conflict, **stop before writes**.
5. Do **not** silently fetch, pull, reset, clean, stash, switch, rebase, commit or push. Editing is not authorization for history/network changes.

## Map and bound the change

- Trace visible caller -> state owner -> API/extension hook -> persistence -> tests -> lifecycle; find old/alternative implementations and feature gates.
- Keep Lumiverse **core** and **extensions** separate. Never move one extension's feature into generic core or modify core to make an extension easier without explicit core PR scope.
- Treat historical **Lumiverse Suite / enhanced suite** code as **quarantined legacy**, not a source of modern architecture. `rg -ni 'lumiverse.?suite|\bsuite\b' frontend tests scripts` where relevant. Do not expand Suite feature gates, attributes, state, helper reach or imports. Do not blindly delete legacy; trace references and migrations before removal. Record unrelated contamination separately.
- No drive-by refactors, dependency/toolchain upgrades, all-file reformatting, broad cleanup, or unrelated bugfixes. Documentation-only work stays documentation-only.

## Direct edits, preconditions, and Windows preservation

- Automated edits must verify file existence, exact/unique anchors or proven AST matches, and expected structure **before writing any file**. Stage transformations in memory, then validate, then write.
- Detect CRLF/LF, BOM, encoding and final newline. Normalize matching **in memory** only; preserve on write. If a tiny logical edit turns into thousands of changed lines, stop and investigate before proceeding.
- Edit canonical CSS selectors instead of appending override mountains, even for surgical PRs.
- Avoid `git apply` unless a well-justified exception. Don't send install scripts when direct edits are possible; if a small Bun `.mjs` installer is explicitly needed, make it self-checking/atomic, preserve newlines, and ZIP it.
- Inspect `git diff --stat`, `git diff --numstat`, `git diff --name-only` after each meaningful stage; `git diff --check` near completion. All unexpected diffs are bugs until explained.

## Verification that matches the risk

- Start with smallest relevant test, then existing typecheck/lint/build commands actually defined in the repo. Do not run global autofix as a diagnostic.
- Source/spindle integration changes require a minimally viable mock host/DOM pipeline covering absent/late elements, stale callbacks, desync, remount/teardown, null refs and future refactors.
- For Lumiverse browser/Spindle/lifecycle work, use the existing `scripts/e2e-diagnostics` Playwright harness and `bun run diagnose` / `bun run diagnose:spindle` as relevant, not disposable random browser scripts.
- On top-edge mobile surfaces, locate **Lumiverse's existing safe-top variable**. Reuse it instead of hardcoded notch offsets or duplicated `env(safe-area-inset-top)`. Check notched mobile/PWA behavior and avoid double padding.
- Perform a semantic/ARIA pass on materially changed UI (labels, role, names of icon-only actions, dialog naming, focus/restoration, keyboard, tabs and hidden SVGs). Prefer native semantics to false ARIA.
- Test with controlled fixtures, never personal characters/chats/keys/presets. A build pass alone is not a behavioral test.
- After tests, inspect generated `frontend/dist`, reports, coverage, screenshots, caches, logs and lockfiles. Keep generated artifacts only when explicitly required. Do not reset unrelated user-owned changes to clear test output.

## Packaging and finish

- **PR ZIP = modified files only, in exact relative paths.** Not a cumulative source tree. No unrelated config, credentials, generated output, or private fixtures.
- Commit, push, force-push, branch switching, rebase and PR creation require explicit authorization; don't conflate edit approval with repository mutation permission. Never force-push without authorization.
- Report base/branch, intentional changed files, functionality, test commands and results, accessibility and browser evidence, dirty-tree handling and unresolved blockers. Do not claim the change passed an unrun check.
- Stop on ambiguous anchors/branch ownership, poisoned diffs, incompatible generated output, unapproved cross-boundary changes, or mismatched architecture. Fix only if within scope; otherwise report.

**Reviewer standard:** they should understand what changed, why, how it was tested, and why nothing unrelated moved.
