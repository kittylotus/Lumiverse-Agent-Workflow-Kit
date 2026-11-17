---
name: surgical-ui-fix
description: Fix a small UI bug, compatibility issue or compatibility issue with tightly bounded changes. Use for isolated functional failures when no redesign is authorized; still fix canonical CSS rules rather than adding override patches.
---


# Surgical UI fix — bounded but complete

**Smallest reliable root-cause change, not shortest possible diff.** This is a narrow **technique** usable inside PR, extension, or app ownership; it does not change delivery rules. It is intentionally different from `$ui-redesign`.

## Procedure

1. Reproduce the behavior from source/test/screenshots. Map affected selectors, state handlers and related consumers.
2. Confirm the likely root cause with a precise test or an explanation of what is observable.
3. Apply a localized fix in the original owner of the behavior. If it's CSS, change its canonical selector and remove obsolete overrides; don't append a new one.
4. Avoid unrelated reformatting, icon changes, component swaps, and dependency upgrades.
5. Test the failing case and near neighbors, including mobile where layout is involved.
6. Provide changed files, test results, known uncertainties, and rollback strategy.

If a proper fix requires structural changes beyond the initial assumption, explain the reason and make the smallest **complete** restructuring; don't conceal it under a fragile hack. If the user requests a real redesign, switch to `$ui-redesign` rather than applying this mode forever.
