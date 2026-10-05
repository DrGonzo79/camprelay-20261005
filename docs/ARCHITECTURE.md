# Architecture

## Prototype

`data/demo_camps.json` is the explicit shared UI fixture. `app/page.tsx` provides an interactive static experience. `api/main.py` independently exposes the same domain vocabulary through `/matches` and `/relay-plan`. Python is runnable and tested source, not deployed.

## Production boundary

Browser → Next.js web client → authenticated FastAPI → PostgreSQL. A scheduler enqueues source checks; per-source adapters write timestamped observations; an alert worker sends idempotent notifications; official registration remains a parent handoff. Metrics: source freshness, monitor lag, alert latency, acknowledgement rate, readiness failures, handoff rate, support minutes, refund rate.

## Safety and failure modes

- Stale source: show last verification and block “ready” status past a freshness threshold.
- Opening change: store observations and alert on schedule drift.
- Duplicate alerts: idempotency key per relay/opening/event.
- Partial provider outage: retry with backoff, expose degraded status, never claim registration.
- Sensitive child/payment data: minimize fields, encrypt at rest, use a PCI provider, and keep payment tokens out of model context.
- Bot or terms conflict: disable adapter and revert to manual reminder/handoff.
