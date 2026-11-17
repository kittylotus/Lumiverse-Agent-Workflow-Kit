---
name: css-refactor
description: Refactor, deduplicate, and fix CSS cascade issues at their source. Use when selectors are duplicated, style overrides are stacked, specificity wars appear, responsive CSS collides, or a component needs visual cleanup. Strongly prohibits append-only override patches.
---


# Canonical CSS refactor — NO LAYER-CAKE STYLESHEETS

**Non-negotiable: when changing a first-party style, edit the owning/base rule and remove obsolete competing rules. Do not append a new counter-rule at end-of-file because it is fast.**

## Before editing (mandatory)

1. Find the component's DOM/class ownership and every relevant stylesheet. Use `rg -n` for selectors, variables, media queries, utility class names, `!important`, and JS-added classes.
2. Read the full cascade chain (source order, specificity, inheritance, `@layer`, media/supports rules and inline styles). Check whether a conflicting rule is generated or third-party code you cannot edit.
3. Note baseline behavior, affected breakpoints, and likely consumers of shared classes.
4. Find canonical definitions, intentional variants, dead declarations and duplicated rules. Fail before automated writes if anchors/selectors are ambiguous.

## Make the change

- Modify the canonical selector **in place**. Consolidate relevant declarations; remove superseded declarations/selectors and unreachable styles.
- If the stylesheet architecture is itself wrong, refactor its organization: tokens / base / components / variants / responsive, preserving bundle/import order and existing tooling.
- Responsive variants belong in the established breakpoint or component module, not scattered emergency patches.
- Factor shared values into design tokens only where there is an actual shared contract; don't create 50 one-off variables.
- Avoid extra IDs, nested specificity, `!important`, and brittle DOM-position selectors. Use variants/data attributes for meaningful state.
- When touching shared CSS, audit all components that use the class. Do not overwrite unrelated visuals.

## Anti-patterns: refuse these by default

```css
/* Existing rule */
.panel { padding: 24px; }
/* 900 lines later: 'fix' */
.panel { padding: 18px; }
/* At the end: 'fix fix' */
.page .panel { padding: 12px !important; }
```

Rewrite the **original `.panel` rule** and delete the redundant fight. If a special variant is actually needed, encode a clear `.panel--compact` and its genuine use case; do not mutate every panel to fix one instance.

## Verify and report

- Search again for the selectors touched. Review duplicate/conflicting declarations across matching conditions. Legitimate scoped variants or property fallback chains may repeat; explain any deliberate exceptions.
- Run lint/style checks and available UI/visual tests at affected breakpoints. Check CSS bundle order and remote/PWA asset loading if relevant.
- Provide a short "cascade audit": canonical files/rules changed, removed overrides, legitimate exceptions, tests and residual debt. If tests cannot run, say exactly which were not run.

An **isolated, documented compatibility override** is allowed only for immutable generated/third-party CSS where the canonical source cannot be changed. Place it next to the integration boundary and explain the exception; never use it as the default path.

## Optional read-only duplicate scan

If Python 3 is available, run `python .agents/skills/css-refactor/scripts/scan_duplicate_selectors.py path/to/styles.css` (adjust path for a global install). It reports identical selector blocks repeated inside matching at-rule scopes, exits 1 if it finds any, and **never modifies files**. Treat findings as prompts for cascade review, not as automatic proof of a bug: legitimate fallbacks and deliberate overrides can repeat. It cannot replace a real CSS parser/linter for complex nesting.
