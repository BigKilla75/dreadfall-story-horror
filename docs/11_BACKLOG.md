# 11 — Backlog and acceptance criteria

Issue priorities: P0 required for private alpha, P1 post-alpha, P2 commercial beta, P3 future. Suggested owner: Claude primary runtime, Codex review/tests. Assign one module owner per issue. Mark complete only with evidence, not code generation.

## P0
P0-01 New-place setup and Rojo mapping — verify new Roblox universe/place identity, backup, Studio sync with visible bootstrap. **Acceptance:** safe two-client scene test, exact place ID documented.
P0-02 SessionService — server states, runId, late join and 1/2/4 player support. **Acceptance:** staged deterministic transitions; late join safe; no host dependency. Codex checks invalid transitions.
P0-03 Greybox environment — six areas, routes/doors and safe checkpoints. **Acceptance:** whole path traversable, no clip/softlock, low-end readable.
P0-04 Interaction/Puzzle 1 — validated proximity, breaker sequence, feedback/hint. **Acceptance:** solo works; duplicate input one outcome; mobile prompt.
P0-05 Puzzle 2 / ObjectiveService — signal console setup, 2–4 parallel/solo sequential handling. **Acceptance:** objective state synchronized and stage advances exactly once.
P0-06 NarrativeDirector — stage text and cues, three acts, two alternate audio-visual clues. **Acceptance:** all lines accessible via subtitles; exact cue triggers.
P0-07 ThreatDirector — one telegraphed encounter, safe chase/failure reset. **Acceptance:** no unavoidable death/camping, 1/2/4 and lag tests.
P0-08 Recovery/end — death, last player leave, checkpoint restart, complete ending, debrief/replay. **Acceptance:** full clear in solo and 4 clients.
P0-09 UI/accessibility — objectives, menus, subtitles, volume/flash controls, touch. **Acceptance:** real mobile tested, deaf/low flash playable.
P0-10 QA gate and release — test matrix, performance fixes, media, owner private release signoff. **Acceptance:** no open critical blockers; exact evidence.

## P1
P1-01 Seeded 3 authored event variants and regression suite.
P1-02 Optional six evidence clues, journal, simple rewards/badges.
P1-03 Versioned profile saving for earned cosmetics and completion, recovery from errors.
P1-04 Polish: original sound mix, level dressing, procedural ambient nonessential variation.

## P2
P2-01 Purchase service hardened (ProcessReceipt, idempotency, entitlements).
P2-02 First cosmetic pass and supporter pass, owner-approved prices and product IDs.
P2-03 Funnel/economy instrumentation; dashboard and player test cohort analysis.
P2-04 Public party flow and safe reserved-server sessions, real published test.
P2-05 Store UI with transparent products, no pay-to-win; regional eligibility tests.

## P3
P3-01 Second ending earned by evidence, not Robux.
P3-02 Additional story chapter/act, only after audience retention proves appetite.
P3-03 Localized subtitles and optional controller polish.
P3-04 Live operations and repeatable challenges only if sustainable.

## Agent issue quality
Each issue should include: Why, owner and touched modules, user-facing behavior, explicit server security invariants, dependencies, steps/test cases, definition of done, out-of-scope, deliverables, evidence link and blocking questions.
