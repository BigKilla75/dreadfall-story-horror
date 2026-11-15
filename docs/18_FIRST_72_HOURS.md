# 18 — FIRST THREE DAYS (72 CLOCK HOURS): staged acceleration and forecast control
Date written: 15 Nov 2026. Timeline is a first-three-calendar-day plan with **~8–12 productive work hours per day**, NOT 72 consecutive active model-hours, 24/7 access or a claim of previous progress. Days assume ~8–12 productive host hours each; extend if tests/quotas/Studio access prevent safe execution. Day 3 gate decides if 14-day private alpha remains plausible. No public shipping commitment.

## Absolute startup / shift-zero checklist
1. Owner-approved correct repo, main SHA, no dirty worktree, original source repos untouched. Review GitHub open issues, docs/17–21 and actual current code. Confirm no separate competing horror Studio games.
2. Claude verifies local Windows Studio, Rojo, Selene and any Blender availability; verify one new universe/place and backup. If unknown, stop live sync; CLI work may proceed.
3. Map files controlled by Rojo vs Studio. Record the Studio model tree and save/reopen a harmless test object to prove the persistence path, backed by dated .rbxlx export in an owner-controlled private backup path.
4. Controller adoption is gated: original Dreadfall controller #27/#28 was quarantined; do NOT run, clone/activate or trust it as safe. New autonomous controller is PROPOSED until local lock/restart/stop/Studio canary proves safe and owner activates it.
5. During safety setup only ONE Claude manual session may write. Codex can perform a bounded handoff readback AFTER Claude exits; no simultaneous processes.
6. Start with GitHub issue #1 and close it only against actual Studio evidence. Build 5-minute vertical slice before decorative modelling.

## Day 1 — Make ONE authoritative game recoverable
Hour 0–1: CLAUDE — fetch/review exact main, existing Studio target, permissions; compare with original handoff safeguards without applying Dreadfall project-specific canon. Pick actual folder paths; write files-to-be-owned and baseline SHA.
Hour 1–2: CLAUDE — verify correct new place, placeId, Rojo allowlist, Studio-only vs Git-backed ownership. Save a dated Studio backup; test close/reopen persistence with a harmless change. If no new place exists, request owner help and continue safe CLI preparation only.
Hour 2–3: CODEX (read-only protocol audit, only after Claude session fully exits) — examine scene-saving method, Rojo mapping, allowlist, git status safety, duplicate listener risk, dirty-state guard and recovery sequence. Return precise findings and a written acknowledgement, no Studio or file changes.
Hour 3–4: CLAUDE — implement minimal server session + objective + interact request and clear HUD; one shared objective and one safe room. Add pure tests.
Hour 4–5: CLAUDE — connect only approved place and execute 1/2-client smoke; log exact SHA, place ID, evidence and failing steps. Save Studio checkpoint and verify file-backed code.
Hour 5–5.5: CODEX (now eligible for isolated branch edits ONLY if controller/manual protocol has passed authorizations) — review networking, add targeted input/revision regression tests; do not run Studio or edit main.
Hour 5.5–7: CLAUDE — inspect Codex changes in separate branch, integrate if checks pass, rerun Studio smoke and save/reopen. Fix actual blockers first.
Hour 7–8: CLAUDE — rough workshop/power gallery greybox and first breaker mechanic, add gameplay video capture if possible. EOD handoff: one verified game, exact saved place, 1/2-player interact, backup and rollback identity.
DAY 1 MUST PASS: correct standalone place ID confirmed; verified code+Studio restore; same objective visibly updates on two Studio clients; test evidence references exact head; no source projects altered. If any fail: Day 2 begins repairing Day 1, not creating additional systems.

## Day 2 — Route and first complete loop
Hour 0–1: CLAUDE — reconcile previous actual SHA and known-good Studio backup; examine Codex feedback and unresolved broken tests.
Hour 1–3: CLAUDE — build six-zone WHOLE facility as cheap greybox with clear spawn-to-finish path, door states, checkpoints and visible direction. Keep one connected scene, not six projects.
Hour 3–3.5: CODEX — test/readback, target co-op lifecycle, duplicate interaction and stale event handling, propose narrow changes on own branch.
Hour 3.5–5: CLAUDE — implement power routing (three breakers, stable server progression, solo path, retries), integrate bounded fixes, 1/2-client Studio test.
Hour 5–6: CLAUDE — implement archive clue and basic signal console, first enemy silhouette placeholder, ending stub. Produce 5-minute prototype full loop.
Hour 6–6.5: CODEX — review unauthorized interactions, late-join state, resetting flags, and test harness gaps. NO Studio connection.
Hour 6.5–8: CLAUDE — integrate tested fixes, 1/2/4 simulated client smoke, restart/replay, save/reopen, profile core performance. Backup and release known-good tag after verified passes.
DAY 2 MUST PASS: traversable complete six-zone greybox; power puzzle and stub ending; solo and 2-player whole-loop clear; 4-player replicated objective smoke; no blocking progression on one player disconnect. If not, cut decorative detail, do not claim chapter is close.

## Day 3 — Narrative vertical slice and trustworthy forecast
Hour 0–1: CLAUDE — git/Studio identity sanity, inspect all tests and read Codex handoff; write day-three risk list.
Hour 1–3: CLAUDE — flesh two puzzles, subtitle/signal cue and 3-act sequence along actual traversable map; meaningful visual event within first few minutes.
Hour 3–3.5: CODEX — server contract/security and stale state audit; update deterministic unit tests on isolated branch after handoff.
Hour 3.5–5: CLAUDE — integrate, add scripted Echo encounter and recoverable chase with clear hazard warnings. Greybox art sufficient.
Hour 5–6: CLAUDE — ending + debrief + reset, options for volume/reduced flashing, first touch UI pass.
Hour 6–6.5: CODEX — review input/respawn/late join/asset dependency regressions, no main writes and no Studio.
Hour 6.5–8: CLAUDE — 1/2/4 Studio flow, phone emulator, real mobile when available; save/reopen backup, estimate honest measured first-run duration and remaining tasks.
DAY 3 MUST PASS: one same-place playable narrative slice from spawn to result, server-authored objectives, recoverable chase, repeatable reset, no source loss and evidence logged. This does not mean polished 30-minute chapter is complete.

## Daily deliverables (evidence, not assertions)
- main SHA, approved place/universe ID, last successful full scene backup checksum/path, current Rojo target and agent lock owner.
- screenshot/video or test logs of the same build; exact player count, device, Studio or published mode, result PASS/FAIL/NOT RUN.
- list of implemented objectives by ID, measured playthrough duration, outstanding severity-0/1 bugs, reused/licensed assets actually verified.
- current issues/PR links and next single WIP task; quota/backoff status, not invented.
- reversion path: last known-good main SHA AND matching Studio backup are both required for gameplay rollback.

## Forecasting and prediction-efficiency model
Estimate work in independent feature units (1–3 active engineering hours); do not equate commits with progress. After every two handoffs, record:
- E_h = estimated hands-on minutes for task; A_h = actual productive minutes (exclude quota waiting and unverified claim); R_h = verified rework minutes; H_h = handoff overhead; T_h = actual Studio test minutes.
- Prediction error ratio = abs(A_h - E_h) / max(E_h, 1). Rolling median of completed tasks exposes over-optimism; also report proportion of estimates within 25% of actuals.
- Verified throughput = accepted gameplay milestones / total staffed hours; rejected or untested work contributes ZERO.
- Forecast remaining time = sum(residual estimates x observed error multiplier) + measured integration/rework + mobile test buffer + risk reserve. Use p50 and p80 estimates, with range, not a magic single deadline.
- Gated priority: restore integrity > close a whole-loop gameplay gap > prove multiplayer > accessibility/performance > art polish > optional replay > monetization.
- Decision at Day 3: if main game does not save/reopen or cannot complete one two-player route, 14-day private-alpha target is HIGH RISK; shrink map/decor before expanding hours. Re-estimate based on observed throughput and evidence.

## Constant-development conditions
Only while (a) PC on/unlocked with authorized Studio control, (b) provider limits legitimately permit operation, (c) exclusive runner + safe lock + clean handoff working, (d) tests recoverable, (e) owner has approved autonomous local operations. A schedule alone does NOT start the models, and chat/GitHub messages are not schedulers. If any condition fails, checkpoint and stop; do not claim 24/7 work.
