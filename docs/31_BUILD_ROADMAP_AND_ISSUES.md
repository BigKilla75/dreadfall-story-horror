> **GENRE PRIORITY UPDATE:** Before implementing complex simulation details, Claude must prove a **complete replayable 3–5-minute prototype of the round loop** (blackout -> item -> fictional radio -> risk decision -> safe result -> restart) inside the SAME saved Studio game, then expand it to 12–22+ minutes if uncoached testers remain engaged. A 7-day private alpha target is ambitious and optional systems get cut before game completion and safety. See [docs/36](36_GENRE_SELECTION_AND_CORE_LOOP.md). The 18–25-minute old duration is a tuning hypothesis, never forced filler.

# 31 — 7-DAY ALPHA / 14-DAY BETA PLAN WITH HARD GATES
Relative **ACTIVE productive work days**; none of these gates was verified by GitHub planning alone. Owner has requested short development. Do NOT announce public launch date before first playable canonical Studio test.

## The critical path
D0 CHECKPOINT (prerequisite): verify Git HEAD/working tree; make private copy if any dirty data; read current docs; verify Windows Studio/Rojo/Selene; establish one new stand-alone Roblox universe/place ID with owner; Rojo servePlaceIds [] remains locked until approved. Source+Studio backup baseline.
D1 — PROVE CORRECT PLACE + ONE VERTICAL SLICE
- Studio: greybox home, street and corner shop; blackout lighting, torch and radio as dummy interactive props.
- Source: one server-owned session objective, one reliable proximity prompt and visible shared HUD.
- Gate: actual Studio save/close/reopen and private export; 1 and 2 clients can spawn, hear/see blackout cue, complete one objective in SAME game. Log version/time/backup hash.
D2 — CORE SUPPLY AND MONEY LOOP
- Inventory of 3 essentials, safe bag, shopkeeper and one stock source, cash and optional ATM with failure scenario, shared objective updates; no persistent currency.
- Gate: one solo and 2-client run where both cannot duplicate, buy with insufficient funds or lose critical items on death/disconnect; cash never required for success.
D3 — BROADCAST-DRIVEN CHOICE AND FIRST ENDING
- Original text-first radio schedule, one curated scenario, hub OR home outcome, reliable last-state join, clear results/retry. Basic end-to-end map connectivity.
- Gate: SOLO starts and ends in SAME canonical place, 2 clients finish without softlock, save/reopen and backup. If not, cut to one ending/one shop and reforecast. No fabricated day-by-day achievement.
D4 — ONE FAIR HUMAN THREAT
- Scripted looter states and nonlethal short escape; safe path alternative; recoverable single-item theft. No entire combat economy.
- Gate: cannot spawncamp, no inaccessible vital loot, no broken solo completion, no serious frame/perf collapse.
D5 — ATMOSPHERE, MOBILE, CO-OP REGRESSION
- Original radio voice optional; subtitles required. UK signage/lighting, editable UX, low-end device pass, 4-client disconnect/rejoin.
- Gate: 1/2/4 can complete, mobile user can complete without sound, objective states recover after player disappearance.
D6 — SECOND CURATED SCENARIO AND ENDING POLISH
- If P0 is green, add second constrained scenario, clear alternate route, journal/replay, home/hub ending, free outcome badge if persistence safe.
- Gate: no impossible scenario seed, late join at all states, at least 2 complete runs per scenario with 1 and 4 players, versioned seed captured for reproducibility.
D7 — PRIVATE ALPHA RELEASE GATE
- 5–10 invited unbiased players; complete first-time session, input performance, source/scene restore rehearsal, bug triage; release only privately with owner approval and honest known issues.
- Gate: zero S0/S1, two complete multi-client runs, critical actions available on mobile, accurate fictional-disaster disclaimer, no live purchases, no real broadcaster assets. If red, continue fixing rather than releasing.
D8–D10 — BETA STABILITY: Fix onboarding drop-offs, navigation, AI, latency, mobile, scenario inconsistency, persistence if needed; do not add speculative features.
D11–D12 — MORE REPLAY: Additional broadcast/event path only after scenario matrix pass; community/helpful NPC moments; optional earned cosmetics and badges.
D13 — COMMERCIAL READINESS: Owner approves sample cosmetic assets, product IDs and fair prices; DevEx/creator eligibility not assumed. Purchase handling and expiry/rejoin tested in staging; keep purchases disabled if not robust.
D14 — BETA GO/NO-GO: 20–50 outside testers, trustworthy retention/finish data, safety/metadata review, bug severity and recovery evidence, privacy, original media ready. Public launch NOT guaranteed.

## Ruthless priority cut order
Cut: extra buildings/interiors -> second scenario -> additional enemy variants -> ATM detail -> persistent cosmetics -> cutscenes -> secondary ending. Do NOT cut: understandable first minute, radio truth/in-world causality, one achievable ending, 1–4 stability, no forced-paid progress, save/reopen safety, subtitles, mobile legibility. If need be, ship first private alpha with 12–18 minutes rather than faking 22-minute runtime.

## Issue workstreams (create GitHub issues or track individually)
BS-01 environment/canonical place/Studio export and rollback
BS-02 home/street/shop/hub greybox and readable routes
BS-03 synchronized objective + snapshot/recovery + replay
BS-04 original radio broadcast scripts/captions/event triggers
BS-05 food/water/light/cash/ATM/stock inventory, safe transaction
BS-06 one looter NPC, avoidance, item recovery, safety
BS-07 home/hub endings, helper NPC, 2 curated scenario matrix
BS-08 PC/mobile accessibility/performance and 1/2/4 multiplayer QA
BS-09 private alpha feedback and funnel instrumentation
BS-10 cosmetic prototype/monetisation security owner-gated
BS-11 marketing assets/organic beta outreach post-quality-gate

## Definition of playable
Not a folder containing scripts: a verified Roblox Studio place with spawn, blackout, radio bulletin that changes an objective, tangible supplies and at least one threat/safety decision, full ending, restart, correct co-op, and a saved+independently recoverable scene. No known loss of progress through a trivial join/leave. Proof is actual run recording/log/date, not CI alone.

## What the owner must decide / provide
- Confirm keeping the existing standalone repo slug until optional rename (we keep it for now); potential name collision/trademark clearance before commercial launch.
- Create/confirm a NEW separated Roblox place and approve numeric place ID for allowlist; original places never touched.
- Confirm public/private destination before any private-source licensed asset copy. Current repo publicly visible when audited.
- Approve any real spending, cosmetics/pass/product IDs, external ads, influencer fees and public release.
Claude chooses reversible design defaults and implements until blocked, documenting unknowns in docs/22.
