---
name: responsive-layout
description: Design or repair responsive layouts for narrow phones, tablets, desktop and resizable windows. Use for overlapping headers, horizontal scroll, clipped cards, mobile navigation, offscreen modals or touch controls.
---


# Responsive layout

Build one coherent experience across viewport sizes, not a desktop screen squeezed smaller.

## Inspect

- Test representative widths around 320/360/390/430/768/1024/1440px plus the application's real minimum window and enlarged text/zoom when feasible.
- Locate the actual CSS/DOM owner of overflowing elements. Check `min-width: auto` on flex/grid children, fixed widths, intrinsic content, sticky/fixed positioning, safe-area insets, keyboard overlays and `100vh` vs dynamic viewport needs.
- Capture information priority: what remains visible, moves into a menu, becomes a drawer, or switches from columns to cards.

## Design

- Give headers a clear primary title; secondary actions collapse or move instead of colliding with it. No redundant double headers.
- Choose rows versus grids by task density and content: a mobile grid can be excellent for app launchers, a full-width row for text-heavy items. Never impose one pattern universally.
- Keep touch targets usable, typography legible, titles readable and control alignment consistent. Don't shrink font sizes to conceal structure problems.
- Use stable scroll boundaries: headers/nav visible, content scrolls intentionally, dialogs stay inside viewport, lists don't cut through buttons.
- Keyboard focus and swipe/scroll must not trap or move the whole screen sideways. Preserve semantic controls.

## Implement / verify

Update canonical breakpoints and affected component markup; remove stale overrides and dead media queries. Check both portal and embedded/modal layouts, not only the main page. Verify real screenshots and hit targets where tools exist; otherwise provide a viewport test matrix for the user.
