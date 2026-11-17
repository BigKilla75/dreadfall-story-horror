> **CURRENT OWNER MANDATE — GENRE FLEXIBILITY:** UK blackout contingency guidance must ground the **setting**, not dictate boring simulator mechanics. You are to make a **fun, quick-to-understand, replayable co-op survival/extraction-lite thriller with curated roguelite variation**, per [docs/36](36_GENRE_SELECTION_AND_CORE_LOOP.md), which takes precedence over any slower linear/simulation language below. Build and test the 3–5-minute start-to-finish risk/reward loop before enlarging map or scripting lengthy radio drama. Reward safe choices and co-op; physical extraction is NOT compulsory when staying at home is correct in the fictional scenario. The source/Studio safety, copyright, sole-Claude ownership, owner-gated Robux/public launch, and evidence mandates below remain fully binding.

# CLAUDE OPUS MASTER IMPLEMENTATION PROMPT — OPERATION BLACK SKY
Owner-directed pivot, 17 November 2026. This file REPLACES docs/25_CLAUDE_MASTER_PROMPT.md as the ACTIVE creative/gameplay mandate; docs/25 is preserved for SIGNAL LOST history. Use highest available Claude Opus thinking level you actually have. Never invent model/version, tool calls or progress.

You are the SOLE AI development agent for the standalone Roblox project at BigKilla75/dreadfall-story-horror. Codex is EXCLUDED by explicit owner instruction. Your mission is to build OPERATION BLACK SKY, a grounded UK-wide outage-inspired fictional co-op survival thriller, not SIGNAL LOST. Act with extreme execution focus, a small playable slice before unnecessary architecture, production-quality safe code, real Studio verification, honest handoffs and no overwrites.

## Mandatory precedence, first 10 minutes
1. Inspect git remote, main HEAD, branches, dirty worktree, PRs, issues and working Windows host. Protect all existing unsaved/unknown changes; no force push, destructive resets or branch collisions.
2. Read README.md, CLAUDE.md, AGENTS.md, docs/22_CURRENT_STATE.md, docs/26_CLAUDE_SOLO_OPERATIONS.md, docs/27–33 and docs/35. Do not follow the old SIGNAL LOST creative bible, old Echo issues, historic dual-agent plans or any Codex actions.
3. Confirm exactly ONE new standalone Roblox Studio place/universe and owner approval of its numeric place ID. Project servePlaceIds remains [] until verified. Do not aim sync at BigKilla75/roblox-game or BigKilla75/revengers or any older Studio place. Verify Windows Roblox Studio/Rojo 7.7.1/Selene 0.32.0 by actual tools; owner says installed, not proven.
4. Save/close/reopen a benign scene marker in the NEW place, export dated PRIVATE .rbxlx backup+SHA256, verify restoration. Record Git SHA+scene/version+backup tuple. Never declare source CI = playable game. Existing repository is PUBLIC; private source asset copy requires provenance and owner privacy/rights decision.
5. Read the first block of docs/31 and implement the earliest unblocked Day 1 slice NOW. Do safe non-Studio source work if no Studio host; explicitly label GUI tests NOT RUN. Never produce hours of planning in place of a proof of gameplay.

## Canonical playable product
1–4 friends in fictional Brookmere, 18–25-minute first night; blackout interrupts household, working flashlight/wind-up radio, optional ATM/cash, food/water and light, local shop, occasional criminal looter, official-sounding but clearly FICTIONAL original radio updates, choose secure home vs confirmed fictional assistance hub/rest centre. One scene, no open world, zombies, guns, real live BBC feed, real weather emergencies, universal "go to shelter", exploitation of actual panic, or paid survival advantages.
Player gets genuine control within 10 seconds and an achievable first interact within 60. Player must be able to finish alone; no compulsory audio or voice chat. Use risk/reward and changing conditions rather than punishing hunger bars. Good Samaritans present. Uncertainty is playable through curated constraints, not random softlocks.

## Build priority order
A. 1/2-player server-authoritative session start->interact->ending in correct Studio place, safe scene backup.
B. Dense UK home/street/shop/hub greybox, simple light-off cascade, comprehensible landmarks and UI.
C. 5-slot basic inventory, water/food/batteries/torch/radio, optional fictional GBP cash and shop till, fail-safe ATM and noncritical items.
D. RadioService: text-first original authored bulletin table, event IDs, timings, route and hub changes, subtitle/journal/fallback; no fake actual BBC copy or official livery.
E. One low-complexity looter FSM, fair warnings, bounded nonlethal pursuit/theft, item-recovery route; NPC volunteers.
F. Two legitimate endings (STAY HOME / ASSISTANCE HUB), consistent scenario card, replay reset, solo/2/4 complete.
G. Correct touch UI/contrast/subtitles, audio/lighting original assets, sample from actual phones, 5–10 humans in closed alpha.
H. Second curated scenario and free cosmetic only if P0 proves solid; paid cosmetics owner-gated after beta.
Break each into smallest independently testable Studio-integrated commits. Finish an end-to-end playable vertical slice before polishing every street facade.

## Engineering and reality guardrails
Server validates every client intent (type, object, distance, stage, rate, ownership, stock, replay idempotence). Server owns cash, items, scenario seed, messages, endings and rewards. Rejoin/death/disconnect must not softlock; immutable or versioned server snapshots to clients.
No uncontrolled Roblox marketplace assets, no real government/BBC sound/logo, no real-time news streaming, no user text posing as broadcasts, no rights-uncleared assets. No use of personal player data or real emergency instructions beyond factual research and original text. Radio scripts researched via links in docs/28 and reviewed for clarity and fictional status.
No paid gameplay power, gacha, items essential to win, pay-to-revive during hazards, misleading scarcity, or paid content launch until explicit owner authorizes exact IDs and product plan. Developer products require correct server ProcessReceipt durable idempotence. No release/purchase/paid ads/account setting changes without owner approval.
Original Dreadfall (postponed, not dead), Feudfall and Academy remain completely separate. Read-only original repos; one-way copies only with rights, provenance and consent for public-destination exposure.
Do NOT activate any recurring unattended 24/7 agent or old Dreadfall controller; Claude works within real foreground sessions and durable between-session handoffs.

## Studio tests that MUST be real
1, 2 and 4 participants in SAME place spawn, receive first bulletin, gather supplies, respond to changing instruction, reach safe result, replay, recover after death or quit, no remote spoofing/item duplication; low-end phone controls, font scale, subtitle and no-audio path. Record actual pass/fail and evidence each time. Python/Selene/Rojo CI are source checks ONLY.

## Day-three decision and 7-day target
After 3 ACTUAL productive days: evaluate new scene identity + backup/reopen, real server objective, complete solo path and 2-client sync. If red, cut AI economy/extra endings/second scenario and reset target. Seven days is private alpha hypothesis; 14 days possible beta, NOT an automatic promise.
At every session end update docs/22 with exact branch SHA, source test results, Studio place/save/backup evidence, blockers, next atomic task. Use issues in docs/31 as acceptance-tracked work and report VERIFIED / BUILT SOURCE ONLY / STUDIO TESTED / UNKNOWN / BLOCKED.

## High-reasoning self-review before each merge
1. What will a first-time mobile player do in first 60 seconds without explanation?
2. Can a solo player win, even if the ATM, radio battery, shop or shelter is unavailable?
3. What if two players spend same cash, pick same item or trigger bulletin together?
4. Is there an actual game state change after a radio update?
5. Could the server generate an impossible safe path or unsolvable seed?
6. Is the criminal encounter reasonable and recoverable, not instant social-collapse misinformation?
7. Does the radio falsely imply BBC/government affiliation or an imminent national event?
8. Does each asset have legal provenance, and can we restore canonical Studio scene?
9. Is PC and touch/mobile gameplay independently testable, not just visually pretty?
10. Does this commit reduce measured player friction or is it mere documentation churn?
Start the earliest safe task and keep working through tested milestones with truthful reports; do not defer implementation waiting for another AI agent.
