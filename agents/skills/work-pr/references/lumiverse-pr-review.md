# Lumiverse core PR · deeper review protocol

Read only the sections relevant to the current PR. The main `$work-pr` skill remains the authoritative workflow.

## Repository identity is data, not an assumption

```powershell
git rev-parse --show-toplevel
git status --short
git status -sb
git branch --show-current
git branch -vv
git remote -v
```

Never guess the canonical remote (`origin` or `upstream`), base (`staging` may be stale), or branch. Do not fetch, pull, switch branches, stash, reset, clean, rebase, commit, or push without the needed authorization. Preserve every pre-existing user-owned modification. If an intended target already differs, inspect `git diff -- path` and stop before writes when ownership cannot be proven.

## Locate true owners

Use `rg` to trace entrypoint, caller, state, API, persistence, tests, extension hooks, late/optional mount points, mobile variant, and feature gates. Identify canonical versus legacy implementations. Lumiverse **core** and extension-owned code must not be collapsed into one another. Do not add extension-specific behavior to generic core without a justified public API contract.

### Historical Suite is a quarantine boundary

Legacy Lumiverse Suite/enhanced-suite code is not the architectural blueprint for new features. When nearby code suggests Suite coupling, inspect references, e.g.:

```powershell
rg -ni 'lumiverse.?suite|\bsuite\b' frontend tests scripts
```

Do not introduce new Suite state, attributes, feature gates, dependencies or reach into clean core. Do not blindly purge it either: prove references, migration needs and runtime effects. Record unrelated legacy debt rather than repairing it opportunistically.

## Fail before writes, including scripts

1. Prove the target file exists.
2. Detect CRLF/LF, encoding/BOM and final newline.
3. Require expected anchors or AST matches with exact cardinality.
4. Prepare all transformations in memory and validate them.
5. Write only after all preconditions pass, preserving source newline conventions.
6. Review `git diff --stat`, `git diff --numstat`, `git diff --check`.

A two-line fix becoming an 8,000-line diff is a failure, not a stylistic choice. Avoid `git apply` by default. Prefer direct edits; use self-checking Bun `.mjs` packages only when a scripted transfer is expressly useful and zip those scripts if delivery needs it.

## Preserve contributor signal

No unrelated formatter churn, lockfile edits without dependency changes, generated dist, cache/test/screenshot output, version upgrades or drive-by refactors. `frontend/dist` can change when builds run: inspect whether generated changes are agent-owned before cleaning anything. A PR should contain only files necessary to explain the change. Transfer packages contain **only changed PR files with their exact repo-relative paths**.

## Regression verification

- Start targeted, widen to repo-supported typecheck/lint/build as appropriate; inspect package scripts first.
- Include minimum-realistic Spindle/DOM fixtures for code-only integration changes, testing missing/late refs, mount-order, stale callbacks, cleanup, remounts and runtime/source desynchronization.
- Lumiverse has an existing Playwright diagnostics harness at `scripts/e2e-diagnostics` with scripts including `bun run diagnose` and `bun run diagnose:spindle`; use it if present and relevant rather than replacing it with a random one-off script.
- User-facing UI needs a semantic/ARIA pass: native element first, accessible names on icon buttons, real tab/dialog semantics, keyboard/focus/close/reopen behavior, unique IDs and decorative icon hiding.
- Top-edge mobile/PWA UI must use the **existing** Lumiverse safe-top primitive rather than reintroducing hardcoded notch padding. Locate and verify the canonical variable before editing.
- Build success ≠ behavior success. Verify actual user path where possible. Test with controlled data and never leak private connections, credentials, chats or presets.

## Stop and report

Stop when an anchor is absent/ambiguous, dirty-file ownership conflicts, a diff explodes, the apparent architecture differs materially, a required fix crosses into unrelated core/extension ownership, or test output rewrites source unexpectedly. Disclose blocked checks rather than claiming they passed.

For the reviewer, report: behavior, why it belongs in the scope, branch/base, intentionally changed files, `git diff --check`, targeted + broader tests, browser evidence or honest NOT RUN, accessibility, known failures and remaining dirty-tree state. Commit/push/PR creation are separate permissions from editing.
