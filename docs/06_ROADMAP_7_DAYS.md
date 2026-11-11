# 06 — Seven-day private-alpha execution plan

Start: Wed 11 November 2026. Target private test: Tue 17 / Wed 18 Nov (depends on owner availability). Not a promise of a stable public launch. Priorities P0 blocking, P1 only if all P0 gates pass.

## Day 1 — Identity, infrastructure and vertical-slice proof
OWNER: set repository private if desired; create new Roblox Studio experience/place, record universe/place IDs in a private owner-approved setup file (IDs only, no secrets); ensure Claude local Studio/Rojo environment. Check device availability.
CLAUDE: read docs, inspect repo, prepare project sync, construct first corridor greybox, implement simple start -> interact -> end stub and stage state machine, prove 2 Studio clients see same objective.
CODEX: review state transition design, remote security contract and small unit test plan.
GATE: repository independent; no existing game touched; a scripted interaction replicates between at least 2 simulated clients.

## Day 2 — Whole route + co-op foundation
CLAUDE: build six interconnected greybox spaces, doors, restart, late-join recovery and two-player/solo puzzle path; lighting pass.
CODEX: tests/review for disconnect, invalid interact, duplicate press.
GATE: player can walk from spawn to end region and cannot softlock with 1 or 2 clients.

## Day 3 — Narrative and puzzles
CLAUDE: Act 1 + Act 2, subtitled dispatcher lines, 2 real puzzles, checkpoint, clear hints and mobile prompts. Default no sound required to progress.
CODEX: validate puzzle authorizations and event schema; lint/static checks if configured.
GATE: solo completes each puzzle and 2 clients see same resolved outcome.

## Day 4 — Threat and co-op recovery
CLAUDE: build one original monster/silhouette, authored cues, bounded chase, failure recovery, 4-client stress test, ending stub.
CODEX: exploit and concurrency review; rerun with random client departures.
GATE: 1/2/4 complete encounter with clear cues and bounded failure/retry.

## Day 5 — Full story and polish
CLAUDE: opening, ending, environment dressing, layered audio, subtitled cues, menus/accessibility, branding draft and 3 additional optional atmospheric beats.
CODEX: script profiler/static test review; verify performance fallbacks.
GATE: complete beginning-to-ending playable with no external help, first-run timing measured; no monetization flow.

## Day 6 — QA / device / performance
CLAUDE + OWNER: 3 complete playthroughs across 1, 2 and 4 clients, at least one real mobile test, visual QA, performance profile; fix worst issues.
CODEX: independent red-team suite for forged remotes, duplicate inputs, out-of-order stages, edge-case timing and save policy.
GATE: issue tracker has no open P0 blockers; error-free core path in tests.

## Day 7 — Private-alpha packaging and feedback
CLAUDE: clean README, release notes, update changelog, captures/screenshots, final fixes, release branch/tag and QA report. OWNER approves private Roblox publish and invites testers.
CODEX: final PR review and verification checklist, risk list.
GATE: 1, 2, 4 real player tests if possible; complete narrative, 20–35-minute measured run (target closer to 30), no purchase prompts, at least 3 independent testers' feedback recorded.

## Scope-cut order if behind
1. Remove collectibles/evidence persistence.
2. Reduce scenario variations to one curated seed.
3. Remove optional cinematic and extra atmospheric scenes.
4. Reduce map cosmetics and extra paths; reuse rooms.
5. Simplify monster to a telegraphed scripted chase.
6. Reduce 30-minute target only by explicit owner decision; never pad with timers.
NOT CUTTABLE: server-side security, one complete story ending, solo ability, cooperative synchronization, recovery from death/disconnect, UI readability or truthful testing.

## Daily task ledger
CLAUDE: pick 1–2 P0 issues, work branch, implement, document tested behavior. CODEX: parallel read-only audit or an isolated issue and report within PR. OWNER: 15–30 min Roblox Studio/account access, playtest and creative decisions as required. ChatGPT: scope control, PR/issue verification and prioritization. No assistant can promise unattended execution without an actual running execution environment.

## Definition of done
Source committed, no unapproved file overwrite, tests with exact environment reported, 1/2/4 players behavior documented, no P0 failures in last 3 representative playthroughs, mobile UI verified, explicit owner release signoff.
