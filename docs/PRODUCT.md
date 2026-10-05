# CampRelay product plan

## ICP and JTBD

**ICP:** dual-income metro parents managing summer coverage for children ages 5–12, with a hard budget, aftercare requirement, and at least one high-demand camp.

**JTBD:** “When camp registration is scattered across sites and opens at specific times, help me approve a primary and backups in advance so I do not lose childcare coverage while I am working.”

## MVP

One city and one enrollment season: parent brief → normalized shortlist → ordered primary/backups → completeness check → opening alerts → parent handoff to the official form. The prototype demonstrates filtering, queue ordering, validation, monitoring state, and a deterministic FastAPI ranking/readiness operation. It never stores credentials, collects payment, or submits external forms.

## Data model

- `FamilyBrief`: month, activity preference, backup category, budget, distance, aftercare requirement.
- `CampProgram`: public program URL, session, price, care options, opening time, last-verified timestamp, demand label.
- `RelayChoice`: rank, parent approval timestamp, price ceiling.
- `ReadinessPacket`: child-profile completeness, consent, payment approval, official handoff URL.
- `MonitorEvent`: expected opening, observed state, alert delivery, acknowledgement.

## Technical architecture

Next.js App Router static frontend uses explicit fictional fixtures for a Pages-compatible demo. FastAPI owns deterministic matching and relay-readiness rules. A real product would add PostgreSQL, a scheduled fetch/monitor worker, source adapters, encrypted references to a PCI provider, and an audit log. The frontend would call a separately approved API host; GitHub Pages does not run Python.

## AI/model strategy

No model is needed for ranking or readiness. Later, a small extraction model could propose field mappings from public camp pages, with schema validation, source citations, confidence thresholds, and human review. Never let model output authorize payment or submission. The moat should be verified structured data and workflow outcomes, not prompts.

## Economics

Test $49 per child/season for the Registration Relay. At a hypothetical 70% gross margin, support and monitoring must stay below ~$15 per order. An optional $12/month family-admin membership is only worth testing after seasonal retention. The $500 concierge price mentioned by the source is an advertised competitor price, not verified realized revenue.

## Validation plan

Run a single-metro concierge cohort: 10 qualified parents, 10 complete planning sessions, target 5 refundable $49 deposits, and at least 4 real alert/readiness uses. Track completion time, stale-detail rate, alert acknowledgement, successful official handoff, refunds, and support minutes. Kill the paid relay below 2 deposits or if data upkeep exceeds 20 minutes per family.

## Go-to-market

Lead with a city-specific “camp opening calendar” and a 60-second registration preflight. Recruit through parent groups, school PTO newsletters, local family publishers, and camps willing to publish normalized details. Avoid broad “AI for parents” positioning until one local workflow converts.

## Moat

Normalized session/opening data, change history, source reliability, actual registration outcomes, and parent trust. A connector alone is copyable; coverage quality and exception handling compound.

## Risks

Stale dates, camp terms prohibiting automation, false confidence, accessibility gaps, privacy of child data, credential/payment handling, bot defenses, local-market operations, refunds, and alert-delivery failures. Mitigate with citations, freshness labels, explicit approval, official-form handoff, minimal data, audit logs, and no auto-submit in the wedge.

## Roadmap

- **0–30 days:** one-city data set, 10 observed planning sessions, manual relay, refundable-deposit test.
- **31–60 days:** public-source adapters, freshness dashboard, alerts, audit log, parent acknowledgement, three camp partners.
- **61–90 days:** measured official handoff, exception queue, second city only if first-city freshness and margin thresholds pass; evaluate a family-admin membership.
