# CampRelay

A runnable prototype for a parent-approved camp registration relay: filter fictional programs, rank a primary plus backups, validate readiness, and simulate monitoring before handing off to the official form.

## What works

- Responsive Next.js App Router + TypeScript product UI with filters, shortlist queue, validation, loading, empty, and armed states.
- Deterministic FastAPI `/matches` and `/relay-plan` operations with explicit invalid-input and failure behavior.
- Playwright desktop/mobile interactions and Python integration tests.
- GitHub Pages static export with repository base-path support.

All camps, availability, fit scores, and workflow state are fictional. The monitor is simulated. No payment is collected, no external form is submitted, and Python is not publicly deployed.

## Run

```bash
npm ci
npm run dev

uv sync --directory api --locked
uv run --directory api uvicorn main:app --reload
```

## Verify

```bash
npm run typecheck
uv run --directory api pytest
npm run test:e2e
npm run audit:prod
npm run build
```

## Product docs

- `docs/OFFICE_HOURS.md` — customer, pain, wedge, and validation
- `docs/OPPORTUNITY_SCORE.md` — scored evidence and uncertainty
- `docs/PRODUCT.md` — ICP, JTBD, MVP, economics, GTM, risks, roadmap
- `docs/CEO_REVIEW.md` — premise challenge and decisions
- `docs/ARCHITECTURE.md` — prototype and production boundaries
- `docs/BUILD_PROMPTS.md` — phased path beyond the demo
- `research/notes.md` — summarized source notes and limitations
