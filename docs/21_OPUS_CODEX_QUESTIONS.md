> **SUPERSEDED WORKFLOW — OWNER OVERRIDE, 15 NOVEMBER 2026:** Claude Opus / Claude Code is the **ONLY** development agent for SIGNAL LOST. Codex and all multi-agent/rotating schedules are CANCELLED. Preserve the gameplay objectives and acceptance gates below but reassign ALL implementation, testing and review to Claude. Do not start/dispatch Codex, a two-agent supervisor or the quarantined original Dreadfall controller. For current instructions read [CLAUDE.md](../CLAUDE.md), [docs/25_CLAUDE_MASTER_PROMPT.md](25_CLAUDE_MASTER_PROMPT.md) and [docs/26_CLAUDE_SOLO_OPERATIONS.md](26_CLAUDE_SOLO_OPERATIONS.md). Old text is retained only to preserve history. 

# 21 — Agent challenge questions and decision protocol (Claude Opus + Codex, very high effort)
STATUS: PLANNING QUESTIONS. The user names models as "Opus 5.5 Max" and "Codex SOL 6.1 Very High". These are TARGET REQUESTS, not verified model IDs or entitlement; report installed labels exactly and choose strongest reasoning mode actually available. Do not impersonate the other agent's readback. Claude is the only Studio integrator. Codex may act as scoped second developer after verified sequential controller handoffs; otherwise review-only. No parallel active development.

## How to answer EVERY question
Give: proposal (max 3 sentences), alternatives, tradeoffs, required files, exact SHA/source evidence, measurable acceptance gate, security/perf impact, estimated engineering hours p50/p80, failure recovery, confidence level (LOW/MED/HIGH), decision owner and whether owner approval is needed.
A recommendation without a verifiable test is a hypothesis, not a completed task. If one agent disagrees, log the disagreement in a shared decision register, produce a discriminating test, then let actual evidence decide. Don't burn shifts in rhetorical debate.

## Claude Opus — primary architecture, production and player experience
O01. Given current exact source, what is the smallest ONE-PLACE, two-client vertical slice that proves the same executable game exists in Studio today?
O02. Which Studio geometry and config are canonical and persistent after save-close-reopen? Show precise backup, Roblox place ID and restore evidence.
O03. Which assets in original Dreadfall and Feudfall are genuinely reusable? Produce path/commit/licensing/dependencies and a no-mutation audit; prioritize top ten by saved time.
O04. Which 5–10 Blender-original modular assets make Relay Nine distinct with minimum import/collision/mobile cost? What can remain greybox?
O05. Draft exact phase and objective transition table, join/death/replay paths, no solo softlocks, precise client-server message contract.
O06. Can the first 5 minutes deliver a clear objective, meaningful action, anomaly and co-op moment without text overload? How will a naive tester prove it?
O07. How will the two puzzles remain legible for colorblind/no-audio/mobile players and solvable if only one teammate remains?
O08. Which Echo implementation has the lowest runtime risk while delivering tension: finite authored chase or pathfinding? What is measurable fail/retry fairness?
O09. Which StudioTestService plugin/runner capabilities are verifiably installed, and which tests must be run manually? No fabricated automation.
O10. How will source Git + Studio-only scene + Blender exports be snapshotted as ONE recoverable build? Demonstrate restoring the tuple.
O11. With actual 72-hour throughput, what p50/p80 private-alpha ETA is credible and what nonessential content gets cut first?
O12. Can one complete playthrough run with zero Robux prompts and allow free replay? Show evidence.
O13. What production-grade constraints block open beta (mobile, party joins, reach, age questionnaire, rollback)? Name accountable owner.
O14. Is the working title SIGNAL LOST distinctive enough for search/brand? Propose two truthful alternatives if not, but do not rename assets automatically.

## Codex — strict sequential engineering adversary and test designer
C01. Identify the exact failure mode of any Rojo/Studio ownership mismatch; design an automated pre-sync guard without changing original projects.
C02. Is the exclusive Windows lock atomic and crash-safe? How do we reject zombie processes, dirty branches, wrong repos and stale handoffs without force-killing an unsaved Studio session?
C03. Design isolated branch handoff validation: base SHA, HEAD, PR diff, ACK identity, main merge, clean integration sync. How to stop on stale data?
C04. Can an exploit client forge interaction object IDs, skip range, spam prompts, request invalid phase or reward twice? Provide reproducible unit cases.
C05. In 1, 2, 4-client tests, how do we detect duplicated phase transitions, late-join desync, player death and all-party leave cleanup?
C06. What is the leanest deterministic Luau state reducer and typed remote schema to maximize testability without overengineering?
C07. Which exact automated StudioTestService operations are supported by local Studio today? Design 1/2/4 scripted smoke, evidence capture and explicit manual fallback.
C08. Design a fail-closed save/reopen checksum system that proves Git SHA + Studio scene backup belong to the same build.
C09. What happens on quota, auth expiry, agent crash, Windows reboot and orphaned Rojo server? Demonstrate no competing model writers afterward.
C10. How should Blender assets and Studio scene content be tracked without committing enormous binaries, losing imports or trusting unsafe free models?
C11. Which profiler and remote-volume measurements would expose mobile FPS/memory/network issues before beta?
C12. Audit optional pass/developer product architecture for client trust, receipt idempotency and persistence failures WITHOUT enabling payments.
C13. Can a 60/30-minute rotation outperform fewer handoffs? Measure time lost to context load, builds, tests and merge rework after two days.
C14. What are the most probable 3-day blockers and what concrete proof will promote them from UNKNOWN to VERIFIED?

## Joint formal handshake (never simultaneous sessions)
Step A: Claude produces a signed-by-context handoff (branch, SHA, exact task, tests and queued Codex questions). Claude process exits.
Step B: Controller passes that precise record to Codex; Codex independently confirms SHA and answers C questions affecting current issue. Codex may implement a narrowly scoped branch improvement only once safe development mode is activated. Codex exits.
Step C: Controller passes Codex's answered record to Claude. Claude must read it, ACK actual SHA, integrate if tests/evidence justify it, run MAIN Studio smoke, commit status. No agent may self-claim the other's approval.
Step D: Where conflict persists, run the smallest discriminating test. An unresolvable architecture/security conflict becomes owner question or blocked task; agents may continue independent safe research only if it does not require changing the main game.

## Owner decision register (ask once, not every shift)
DECISION O-OWNER-1: Game name/brand. Default working SIGNAL LOST, keep reversible.
DECISION O-OWNER-2: Create/verify NEW Roblox place and game owner. Do not reuse existing Dreadfall/Feudfall place IDs.
DECISION O-OWNER-3: Turn on unattended controller AFTER proof of exclusive lock, stop/restart, quota, backup and Studio smoke. Manual sequential shifts can run before approval.
DECISION O-OWNER-4: Content maturity intent and true Roblox questionnaire. No invented audience rating.
DECISION O-OWNER-5: Public release, real passes/product IDs/prices, paid marketing and any account fees — NOT approved by this document.
DECISION O-OWNER-6: Whether to make current public GitHub horror repo private; original two source repos currently private.

## Response template
AGENT / OBSERVED_MODEL_LABEL / SOURCE_MAIN_SHA / SHIFT_ID / QUESTIONS_ANSWERED / EVIDENCE_LINKS / OPTIONS / RECOMMENDATION / FIRST_IMPLEMENTABLE_ACTION / FILES_ALLOWED / TESTS_EXPECTED / P50_HOURS / P80_HOURS / OWNER_DECISION_NEEDED / STATUS.
No generic "done" without test and source evidence.