---
name: repo-investigation
description: Use for read-only code audits, mapping an unfamiliar repo, regression forensics, API discovery, or design diagnostics when implementation has not been authorized.
---

# Investigation and audit — default is read-only

- Determine the product boundary (PR/extension/app) for architectural context, but **do not write source** unless implementation was explicitly requested.
- Use `rg`, file trees, relevant tests, entrypoints, owners and reference chains to trace visible behavior through state/API/persistence/lifecycle. Inspect current files before guessing.
- Inspect initial Git state when working inside a checkout; do not fetch/pull/reset/clean/stash merely to get a better baseline.
- For legacy/duplicate implementations, distinguish active/runtime paths from archaeological leftovers. Lumiverse Suite remnants are not endorsed foundations.
- Screenshots, QA traces and read-only tests are acceptable when requested; use controlled fixtures rather than personal data.
- Report verified facts, hypotheses, reproduction paths, concrete source locations, candidate fixes and exactly which tests were/weren't run.
- If audit discovers a fix, keep it a recommendation until the user authorizes modification, unless the user's original request already granted implementation scope.
