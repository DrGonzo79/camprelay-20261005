# Phased build prompts

## Phase 1 — real data pilot

Replace fixtures with one-city camp records. Require public source URL, last-verified timestamp, session dates, price, aftercare, opening time, and reviewer. Add freshness blocking and an admin exception queue. Keep official-form handoff.

## Phase 2 — monitoring

Add scheduled, idempotent source checks and change events. Instrument lag, errors, opening drift, alert delivery, and acknowledgement. Provide manual override and a visible degraded mode.

## Phase 3 — paid concierge

Integrate an approved payment provider for refundable $49 deposits; do not store card data. Add terms consent, data deletion, audit log, support-time tracking, and refund workflow. Gate rollout on explicit cohort thresholds.

## Phase 4 — assisted extraction

Use a model only to propose structured fields from cited public pages. Validate against a strict schema, surface confidence and diffs to reviewers, and exclude child, credential, and payment data from model inputs.
