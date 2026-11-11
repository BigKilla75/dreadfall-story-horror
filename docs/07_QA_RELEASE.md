# 07 — QA matrix, acceptance tests and release process

## QA status (11 Nov 2026)
NOT RUN. This document is test plan, not test evidence. No Studio place, Roblox build, gameplay implementation or published experience was verified when written.

## Core manual matrix
Player counts: 1, 2, 4. Platforms: Windows keyboard/mouse and actual Android/iOS (minimum one real mobile; emulate other sizes). Network: normal, high latency, transient disconnect. Sessions: fresh join, mid-act late join, player leave, rejoin, death, whole party fail, replay after ending.

## Critical test cases with expected results
T01 Start solo: can finish each objective and final ending without requiring another participant.
T02 Two players press same breaker simultaneously: objective resolves exactly once, no duplicated stage.
T03 Four players start, one disconnects mid-puzzle: remaining 3 can finish; disconnected player does not gate progression.
T04 Last player leaves: no orphaned stage requiring empty players; server cleanup safe.
T05 Joining during chase: no immediate kill or corrupt state; safely spectate or wait for next checkpoint.
T06 Player dies midway: rest of team continues; player returns to safe checkpoint and can rejoin.
T07 Bad puzzle attempt: readable feedback/hint, no unrecoverable softlock.
T08 Death/restart: prior act flags reset consistently; no unintended permanent skip.
T09 Duplicate stage cue: clients do not trigger two jumpscares or alternate contradictory texts.
T10 Malicious client sends unknown objectId/negative timing/invalid type: server rejects, no server error or unauthorized completion.
T11 20 rapid interaction events: server rate-limits, progression remains correct.
T12 Mobile HUD: text legible, touch prompts reachable, menu usable, essential clue visible without sound.
T13 Hearing accessibility: full run solvable with volume at zero and subtitles on.
T14 Photosensitivity: reduced flashing removes aggressive flicker and gameplay remains comprehensible.
T15 Graphics low: no fatal lighting requirement; performance reasonable for test device.
T16 All endings: required alpha ending plays once, debrief visible, replay/reset returns to lobby.
T17 Free player: complete game without Robux prompt/payment.
T18 Paid cosmetics (post-P2 only): receipt grant durable, no double reward; purchase failures gracefully handled.
T19 Content compliance: owner submits accurate Roblox Maturity & Compliance Questionnaire before release.
T20 Asset provenance: all imported meshes, textures and audio have owner/legal source or license tracked.

## Automated tests (add as implementation exists)
Pure Luau tests: allowed phase transitions; scenario config validates; puzzle reducers idempotent; input schema rejects unexpected fields and out-of-bounds values; seed selection from approved set; evidence reward uniqueness. CI/static: JSON parse, formatter/lint if installed, no hardcoded secrets, duplicate object IDs, forbidden cross-repo references. Do not claim automated tests cover visual Studio gameplay.

## Profiling / quality instrumentation
Log start/end and stage times, input delays, errors/crashes, disconnect outcomes. Use Studio multi-client and Network Simulator. Profile light count, audio overlap and rendering cost on mobile. Avoid slow experience loads, high-frequency loops and unbounded emitters.

## Release gates
Private-alpha minimum: one usable Roblox place; actual 1/2/4 client test evidence; completion in target range or owner-approved reduction; 0 reproducible critical softlocks; readable prompts; mobile check; no purchase UI; source backed up; owner approves.
Public-beta minimum: complete friend party flow/join/leave, stable persistence where claimed, accurate age questionnaire, owned assets, analytics, moderation/trust, aftercare issue triage, real entitlements for any paid items, live end-to-end payment tests. If any gate fails, stay private.

## Evidence log template
Date/time; commit SHA; place ID (public/nonsecret); Roblox Studio version if available; device; player count; reproduction steps; pass/fail; screenshot/video evidence link if any; known defects; reporter. Distinguish simulated clients from real multiplayer and published teleports.

## Rollback
Tag last known tested build; backup place before major Studio sync/publish; maintain rollback instructions and version label; never force-push/replace game place without owner-approved backup.
