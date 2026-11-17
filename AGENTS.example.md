# Lumiverse skill router (optional agent instructions)

> This is a **template**, not a replacement for Lumiverse's maintainer-owned instructions. Merge only rules the maintainers approve; keep repository `CONTRIBUTING.md` and explicit user requests authoritative.

## First choose the ownership boundary

- **Lumiverse core/upstream PR:** invoke `$work-pr`. Protect the live checkout, preserve user changes/CRLF and keep a focused, reviewable **complete** diff. Deliver **modified PR files only** when transferring a ZIP.
- **Lumiverse extension/product:** invoke `$work-extension`. **Full visual and architectural freedom inside the extension** when requested; preserve current host APIs and don't silently patch Lumiverse core. An extension repo having Git/PRs does not turn it into core PR mode.
- **Cross-boundary core + extension change:** separate ownership, evidence and deliverables; obtain approval before changing core.

Use specialist skills as appropriate: `$repo-investigation`, `$surgical-ui-fix`, `$ui-audit`, `$ui-prototype`, `$ui-redesign`, `$css-refactor`, `$component-design`, `$responsive-layout`, `$interaction-states`, `$ui-integration`, `$visual-qa`, `$runtime-verification`, `$lumiverse-spindle-diagnostics`, `$docs-authoring`, `$ui-director`.

## Universal guardrails

1. **NO CSS LASAGNA.** Edit the canonical owning selector; delete superseded rules. Keep intentional responsive variants beside their owning component/breakpoint. No append-only specificity counter-patches.
2. Use `rg` for source ownership. Map callers, API/state/persistence, host lifecycle and tests before nontrivial edits. Scripted transformations fail **before writing** on absent or ambiguous anchors.
3. Preserve existing dirty work, credentials, CRLF/encoding/BOM/final newline. Never silently reset, stash, pull, change branches, commit or push.
4. The **requested task**, not a default diff-minimization dogma, determines the proper structural change. A PR stays scoped; an extension redesign may rewrite extension-owned components to achieve a coherent result.
5. Approved design is a contract during integration, unless the user explicitly requests to revisit it.
6. Use repo's actual tests and existing browser harness. Exercise real interaction/lifecycle paths; check keyboard/semantics, responsive behavior and persistence. Build success is not behavior proof.
7. Report actual checks, evidence, remaining blockers, modified files and rollback advice. Don't claim tests ran when they didn't.

The skills are opt-in, and repository-specific instructions always need maintainer review before use.
