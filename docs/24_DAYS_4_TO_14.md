> **SUPERSEDED WORKFLOW — OWNER OVERRIDE, 15 NOVEMBER 2026:** Claude Opus / Claude Code is the **ONLY** development agent for SIGNAL LOST. Codex and all multi-agent/rotating schedules are CANCELLED. Preserve the gameplay objectives and acceptance gates below but reassign ALL implementation, testing and review to Claude. Do not start/dispatch Codex, a two-agent supervisor or the quarantined original Dreadfall controller. For current instructions read [CLAUDE.md](../CLAUDE.md), [docs/25_CLAUDE_MASTER_PROMPT.md](25_CLAUDE_MASTER_PROMPT.md) and [docs/26_CLAUDE_SOLO_OPERATIONS.md](26_CLAUDE_SOLO_OPERATIONS.md). Old text is retained only to preserve history. 

# 24 — Days 4–14: practical private-alpha roadmap and production gates
STATUS: TARGET / NOT VERIFIED. Re-estimate after day 3 from completed measurable vertical-slice work. Day numbers mean local planned workdays, NOT actual dates or guaranteed throughput. One main Studio place. Never ship broken co-op to meet a date. All agent work strictly sequential as docs/19.

## Day 4 — Stable narrative from entrance to core
Claude: complete objectives/puzzle graph, recovery checkpoints and game-readable objective UI in same main place. Codex: isolated state machine edge-case tests after clean handoff. Studio: solo and two-player end-to-end dry run with one ending stub. Gate: cannot softlock when teammate leaves; all required paths solvable solo.

## Day 5 — Echo and tension
Claude: original or simple licensed threat silhouette; two telegraphed warning beats, bounded 45–90-second scripted chase and retry without resetting 30 minutes. Codex: exploit and death/late-join audit. Studio: 1/2/4 player encounter and resets. Gate: predictable fair threat, no spawn camping, no instakill while input blocked.

## Day 6 — Co-op resilience and 4-client regression
Claude: late join, disconnect, double interaction, single player alive, session reset and narrative sequence reconciliation. Codex: specific tests for forged remotes and duplicated stage revisions. Studio: 4-client simulated run, pause/drop/rejoin at each checkpoint. Gate: no double resolves, no unrepairable shared state.

## Day 7 — Mobile and accessibility
Claude: safe-area HUD, touch prompts, no-sound visual clue equivalence, subtitles, reduced-flashing/camera-shake settings and simpler low-end lighting. Codex: input schema/UI event review. Studio: device simulator + at least one REAL mobile when available. Gate: phone user can solve mandatory puzzle and finish without audio; performance measured on device.

## Day 8 — Whole chapter pacing review
Claude: 3-act editing pass and sound placement, measure actual first-run times and mystery comprehension. Codex: reconciling instrumentation with objective graph. Studio: first outside-player no-guidance session. Gate: credible 25–35-minute target or explicit owner-approved scope adjustment; no idle padding.

## Day 9 — Asset optimization and Blender import
Claude: audit Feudfall CC0 sound catalogue and Dreadfall MapBuilder research; selectively import verified appropriate rights-cleared assets, plus priority original Blender modular assets. Studio: collision/scale/UV/rig check, memory/performance, scene backup and reopen. Codex: asset manifest/static checks. Gate: no unlicensed or unreferenced dependencies; no source project changes.

## Day 10 — Audio/visual polish, clarity
Claude: layered ambient mix, cues, signage, controlled light changes and original Echo identity. Keep route readable without shadows/audio. Codex: static performance review and telemetry code checks. Gate: no low-graphics navigation failure and no ear-damaging mixes.

## Day 11 — Replay layer (only if P0 green)
Claude: implement one optional evidence log and a validated second scenario variant; add debrief/replay/restart proof. Codex: seed and reset tests. Gate: P0 first run still complete; do not create 3 variants if regression cost too high. Free rewards only if reliable persistence is ready.

## Day 12 — Closed beta reliability rehearsal
Claude + owner: real multiplayer private test, one phone, 1/2/4 users and network latency; fix S0/S1 issues. Codex: read-only focused security/performance bug hunt; engineering only on safe branch. Gate: no reproducible critical softlock; exact test log/evidence. Purchases remain OFF.

## Day 13 — Release candidate packaging
Claude: stable build tag, Studio version notes, private .rbxl backup checksum, source SHA, asset provenance and content questionnaire checklist. Codex: final exact SHA audit, no risky feature work. Owner: verify private place access and capture authentic thumbnails/teaser gameplay. Gate: release candidate can be rebuilt/restored and is playable start-to-end.

## Day 14 — Owner-approved PRIVATE alpha
Claude: regression complete 1/2/4-player story from start to result; publish only to private invite audience after owner signoff; record cloud place version. Codex: no parallel edits; provide scoped final checklist. Owner: invite 5–10 testers, note confusion, scare, bugs, replay interest. Gate: no public access or Robux products by default; release only after QA verified.

## Tasks not permitted to displace the milestone
No new massive map, open world, elaborate co-op matchmaking, alternate universes, trading, weapons, custom complex pathfinding, subscriptions, paid loot boxes, large monetization shop, dramatic lore crossover or expensive promotional campaign.

## If schedule slips
Quality/reliability order: canonical save+reopen > one complete free ending > 1/2/4 co-op correctness > mobile readability > fair threat > atmosphere > curated variant > more evidence > cosmetics > monetization. Cut extra scenery and later variants; DO NOT cut data recovery, source isolation, basic security or honest test reporting.

## End-of-day production dashboard
State each day: accepted milestones / hours spent / p50+p80 remaining / exact main SHA / Studio save hash/version / 1/2/4 results / real device result / critical bug count / remaining owner-only decisions / next WIP=1 task. For forecasting, count verified completions only. Every shift requires docs/22 handoff and no overlapping agents.

## After private alpha: first 30 days
Week 1 after alpha: fix top completion bottlenecks, evaluate player interviews, get stable real-player multiplayer evidence and verify access/rating. Week 2: add first safe optional replay variation; accurate thumbnail and short real gameplay clips. Week 3: controlled larger invite beta (20–50) and analytics funnel review. Week 4: public release decision if bounce, completion, co-play and crash metrics justify it; optional price tests only after commerce/entitlement QA and explicit owner approval. No guaranteed public date.
