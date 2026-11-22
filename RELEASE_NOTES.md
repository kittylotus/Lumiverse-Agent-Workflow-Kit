# v1.1 · UUID-first host API guidance

- Promoted the verified UUID API contract to the very top of optional `AGENTS.example.md`, the extension workflow, PR workflow, and GitHub README.
- Clarified that staging supports UUID **v4 and v7**, not v6. Backend `spindle.uuid` calls are async; frontend `ctx.uuid` calls are synchronous.
- Added checked examples, version/capability gates, core helper paths, and non-secure HTTP browser regression pointers.
- No Lumiverse runtime code or existing skill names changed.

# v1 · Lumiverse-focused distribution

- Split the general three-mode pack into **Lumiverse core PR** and **Lumiverse extension** ownership workflows.
- Retained 14 reusable UI/development specialists and added Lumiverse-specific Spindle diagnostics.
- Preserved live-repository protection, dirty-tree/branch policy, CRLF safety, fail-before-write discipline, Suite quarantine and current host extension boundaries.
- Included GitHub-ready README with links, workflow chart, callouts, collapsible examples and repo/global installation instructions.
- Shipped `AGENTS.example.md` as optional guidance rather than overwriting maintainer-owned agent instructions.
- None of these skills modify a project without an agent explicitly performing the requested work.
