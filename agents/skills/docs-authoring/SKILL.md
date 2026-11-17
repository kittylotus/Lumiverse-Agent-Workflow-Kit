---
name: docs-authoring
description: Use for documentation-only assignments in Lumiverse core PRs and independently owned Lumiverse extensions. Verify every stated command/path/API against current source without silently modifying runtime code.
---

# Documentation is a first-class scoped task

Read the primary ownership mode (`$work-pr` or `$work-extension`) for delivery rules, then keep **documentation-only work documentation-only** unless implementation changes are explicitly requested.

1. Establish the reader and document type: tutorial, user guide, API/developer docs, architecture, migration, troubleshooting, contribution rules, inline docs.
2. Search actual source/config/scripts/UI labels and existing docs with `rg`; verify commands, defaults, import paths, routes, settings, values and examples. Do not quote stale docs as proof.
3. Preserve the page's audience and information architecture. Do not turn a short focused page into an encyclopedia or rewrite unrelated docs.
4. If source disagrees with docs, decide which is authoritative from the request; report mismatch rather than altering implementation to make docs true.
5. Make examples runnable/structurally sound. Run link checks, Markdown lints, generated documentation checks or simple reference verification where available.
6. PR docs -> docs-only diff (unless explicitly requested otherwise); extension docs -> delivery follows their mode. Report exact verification and known uncertainties.
