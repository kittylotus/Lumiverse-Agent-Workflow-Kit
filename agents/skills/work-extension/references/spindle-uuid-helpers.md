# Lumiverse Spindle UUID contract (verified against staging source)

> **Mandatory:** Use Lumiverse's supported UUID generators instead of `crypto.randomUUID()`. The supported UUID versions in this staging snapshot are **v4 and v7**, not v6. Do not fabricate an API named `v6`.

## Backend extension: asynchronous Spindle API

```ts
declare const spindle: import('lumiverse-spindle-types').SpindleAPI

const randomId: string = await spindle.uuid.v4()
const timeOrderedId: string = await spindle.uuid.v7()
```

This requires no permission or user ID. For compatibility with older host versions, inspect the advertised capability `spindle.host.capabilities['uuid-v1']` before invoking `spindle.uuid`. Each call returns `Promise<string>`; **await it**. If your extension requires the capability and the host lacks it, explain/update the host or stop with a clear error; don't silently substitute `crypto.randomUUID()`.

## Frontend extension: synchronous context API

```ts
import type { SpindleFrontendContext } from 'lumiverse-spindle-types'

export function setup(ctx: SpindleFrontendContext) {
  if (!ctx.uuid || (ctx.host.capabilities['frontend-uuid-v1'] ?? 0) < 1) {
    throw new Error('This extension requires frontend-uuid-v1. Update Lumiverse.')
  }
  const randomId: string = ctx.uuid.v4()
  const timeOrderedId: string = ctx.uuid.v7()
}
```

Frontend calls return `string` immediately and do **not** need `await` or network access. The frontend capability `frontend-uuid-v1` is **not** implied by the backend `uuid-v1` capability. Captured frontend methods may throw after context teardown; do not call them after unload. Frontend v7 ordering is local to one frontend runtime, **not** global ordering across browsers/servers.

## Core implementation (not an extension)

- Server-side core: use `uuidv4()` or `uuidv7()` exported by `src/utils/uuid.ts`.
- Frontend core: use `uuidv4()` / `uuidv7()` from `frontend/src/lib/uuid.ts` (usually imported via the existing `@/lib/uuid` alias).
- Do not copy the core helper into extensions when `ctx.uuid` or `spindle.uuid` is available.

## Why this is non-negotiable

`crypto.randomUUID()` is unavailable on insecure origins, including a remote Lumiverse page opened over plain HTTP. Lumiverse's frontend UUID helper uses `crypto.getRandomValues()`, which remains usable there. Replacing it with native `crypto.randomUUID()` can break frontend extensions only on real devices while passing localhost tests.

## Source-of-truth paths in the user-provided Lumiverse staging snapshot

- `developer-docs/docs/backend-api/uuid.md`
- `developer-docs/docs/frontend-api/uuid.md`
- `src/spindle/uuid-contract.ts`
- `src/spindle/worker-runtime.ts` (`spindle.uuid` implementation)
- `frontend/src/lib/spindle/uuid-api.ts`
- `src/utils/uuid.ts` and `frontend/src/lib/uuid.ts`
- `scripts/e2e-diagnostics/check-spindle-uuid.mjs` (plain-HTTP browser regression check)

Verify against the target checkout whenever its version differs.
