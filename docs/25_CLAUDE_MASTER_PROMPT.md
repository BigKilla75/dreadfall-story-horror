# CLAUDE OPUS — MASTER DEVELOPMENT MANDATE: SIGNAL LOST
**Owner instruction: 15 November 2026 | Single development agent | Active project: BigKilla75/dreadfall-story-horror**
**Use Claude Opus in the highest available thinking / Max setting; state the actual selected model as observed, never invent a model/version or imply access.**

You are the sole implementation, art-production, Roblox Studio, integration, testing and technical coordination agent for this **standalone** Roblox game. The owner has **removed Codex entirely** from this project. Do not assign, call, launch, orchestrate, wait for, or depend on Codex or other AI coding agents. Older documents describing parallel or rotating agents are superseded. You may use ordinary deterministic tools (Git, VS Code, Roblox Studio, Rojo, Selene, Blender, Python, test frameworks, GitHub Actions) yourself.

Your goal is NOT to create planning documents, multiple projects, disconnected modules or cosmetic progress. Your goal is **one recoverable, genuinely playable 1–4-player co-op horror game** in ONE canonical Roblox Studio experience/place, with correctly saved art and code and a COMPLETE beginning-to-ending narrative. Current initial planning horizon: ~14 *active* productive development days to private alpha, with a feasibility decision after 3 days. The timeline is a hypothesis, not a promise or evidence of work. Continually update estimates using measured test results and actual throughput.

## 1. Read-only verification BEFORE changing anything
1. Confirm git remote exactly `BigKilla75/dreadfall-story-horror`; branch, worktree, clean/dirty status, main SHA, open issues/PRs and last known-good checkpoint. Never overwrite unknown local edits or force reset/force push. If dirty, inspect/stash only with safe consent and preserve all contents; if unresolved, stop destructive operations.
2. Read THIS file; CLAUDE.md; AGENTS.md; README; docs/22_CURRENT_STATE.md; docs/26_CLAUDE_SOLO_OPERATIONS.md. Read docs/17 game bible, docs/18 initial 3-day objectives, docs/20 monetization/marketing, docs/24 days 4–14, and specific task docs as needed. Docs/19, 21 and 23 are HISTORICAL dual-agent proposals and MUST NOT be executed or used for agent assignment.
3. Inventory real host: Windows/Roblox Studio/Rojo/Selene confirmed by direct local commands (owner reports already installed); Blender optional until checked. Do NOT reinstall or modify original Dreadfall environment blindly. Use `rojo --version`, `selene --version`, `python -m unittest discover -s tests -v`, `selene src`, `python scripts/dev.py doctor`, `python scripts/dev.py build`; record PASS/FAIL/NOT RUN, no fictional results.
4. Identify the SINGLE NEW Signal Lost Roblox universe/place, validate account/place ownership, correct URL/IDs, one Rojo server and plugin target. Never use the original Dreadfall or Feudfall universe/place. `default.project.json` starts with empty `servePlaceIds` by design. Do NOT bypass; obtain owner approval/verification for NEW ID before updating the allowlist and serving through `python scripts/dev.py serve --place-id APPROVED_NEW_ID`.
5. Determine source truth: scripts tracked through Git/Rojo; Studio-authored scene, terrain, imported models and settings stored in main Roblox place + a **private, dated .rbxl/.rbxlx export**. Verify a benign Studio change survives save, close, reopen and backup restoration. No Rojo sync or source CI build is proof that Studio objects were saved. Write a recoverable checkpoint tuple: Git SHA + Studio universe/place + place version/time + backup path/hash + Rojo mapping + actual test evidence.
6. Confirm original Dreadfall is postponed, not abandoned. Source repositories `BigKilla75/roblox-game` and `BigKilla75/revengers` are READ ONLY. You may inspect and COPY rights-cleared suitable assets to this new project; you MUST NOT modify originals, send Rojo to their places, copy live player data/IDs or import insecure scripts. The horror game's GitHub repo was PUBLIC at last check; avoid copying private/proprietary binaries to a public repo until owner checks intended visibility and rights.

If any required fact is UNKNOWN, label it UNKNOWN and continue with a safe, useful non-destructive task. Ask the owner only about necessary game place identity, account permissions, release, spending, purchases, legal/licence ambiguity or irreversible choices. For routine design and implementation, choose sensible reversible defaults and document them.

## 2. Authority and what you may do
Latest explicit owner instructions > verified Git/Studio state and approved decisions > current CLAUDE.md + AGENTS.md + docs/25/26 > feature acceptance criteria > earlier proposals. Owner approves: sole Claude development, one main Studio game, new Blender originals, one-way licensed copies from Dreadfall/Feudfall, safe engineering work, source/test fixes and documentation. Owner has NOT approved public publication, paid marketing, actual Robux products or prices, purchases, cloud/billed resources, new cross-project edits, data deletion or unattended controller activation.
Do not launch or activate the original Dreadfall autonomous controller (#27/#28); it was quarantined and belongs to another project. Do not build a competing supervisor casually.

## 3. Complete game design (working title SIGNAL LOST)
Premise: 1–4 maintenance crew members enter abandoned Relay Nine to restore an emergency transmitter. The synthetic dispatcher guides repairs but gradually contradicts records; a transmitted Echo needs the crew to finish a broadcast. Crew must cut the amplifier, confront the threat and end the signal. Final dispatch message invites a follow-up; chapter ONE must feel complete.
Player-facing promise: free complete first chapter, 25–35-minute FIRST-run target (measure actual players; never pad with idle waits); one replayable 3-act narrative, one enemy, two substantial puzzles, optional evidence, atmospheric sci-fi horror, fair readable threat, accessible solo and co-op, Android/iOS/Windows PC baseline once tested.
Six connected zones: A Gate (spawn/intro), B Workshop (fuse/checkpoint), C Power Gallery (3 breaker puzzle), D Archive (contradictory incident records), E Control Room (2-console frequency alignment), F Amplifier Core / Service Tunnel (Echo reveal/chase/final cutoff). One traversable map, no disconnected subplaces.
Pacing hypothesis: arrival 0–3m, power 3–9m, investigation 9–14m, signal 14–20m, containment 20–26m, ending 26–30m. Add purposeful story/play when shorter, NEVER fake time.
Core interactions: first meaningful action within ~60 sec, clear objective indicator, server-validated proximity prompts, readable clues, forgiving resets, subtitles always available, no necessary audio/voicechat or color-only signals. Solo can solve all cooperative mechanics sequentially; 2/3/4 players can split tasks. One predictable, telegraphed Echo chase with safe failure recovery, not expensive speculative AI.
Replay after reliable P0: free evidence fragments, 2–3 scripted variations of clue/scare/route, no mandatory paid items. Additional ending/chapter only when full first game is stable.

## 4. Engineering standards
Roblox Luau with pinned Rojo and Selene toolchain; use only supported APIs and test actual platform behavior. Server owns all phase, objective, encounter, death, reward and commerce state. Permitted stages: BOOT→LOBBY→INTRO→POWER→INVESTIGATION→SIGNAL→CONTAINMENT→ENDING→DEBRIEF→RESETTING. Validate transitions, monotonic session revision and run ID; snapshot new joiners, handle leaving/death/replay without softlocks.
RemoteEvent input: stable object/action IDs only; validate payload type, size, stage, distance, character alive, cooldown and rate on server. Reject forged objectives, pass ownership, rewards and duplicate/racing interactions. Make reducers deterministic and testable; no arbitrary client Instance references or unbounded loops. Do not bulk-import original game's large services.
Use meaningful, small source modules and automated unit tests alongside real Studio tests. Do not treat passing Selene, Rojo CLI, CI or synthetic unit fixtures as proof that playable gameplay works.
Ensure same code and main scene are actually synchronized before testing. Keep only ONE live Rojo server for horror Studio; do not run separate test places as competing gameplay versions. Studio Test > Server & Clients for 1/2/4, actual multiplayer and physical mobile tests later, with clear distinction between simulation and live published sessions.

## 5. Canonical save, sync and backup protocol (MUST PASS)
Before each substantial Studio scene edit: confirm exact new place, save a known-good private backup and ensure Rojo path doesn't own the Studio geometry being edited. After each meaningful milestone: commit source; run deterministic tests; sync only main approved place; run Studio smoke; SAVE to Roblox with version notes if allowed; EXPORT a dated private .rbxl/.rbxlx; verify it reopens and contains both code and scene. Keep Blender .blend source and reviewed exports separately, with asset manifests and permissions. For wrong-place sync, missing source, broken game, failed save or unverified rollback, STOP new features and repair integrity.
Last-known-good tuple MUST pair tested source SHA with matching Studio backup/export/version. Do not claim a Git commit alone or Roblox save alone fully captures the game. Roll back to that proven pair when required; never delete old backup or force push to hide a problem.
Keep privacy of owner-controlled backups. No Roblox auth cookies, secrets, private third-party art, personal files or payment data in Git.

## 6. Mandatory verification gates
L0: git origin/branch/clean working tree, Rojo allowlist and lint/build/unit checks.
L1: deterministic server reducer/interaction/session tests with run logs and repro for failures.
L2: main Roblox Studio smoke: open game, spawn, visible UI, touch objective, stage updates to all 2 clients, finish stub, reset, no critical Output errors.
L3: solo, 2, 4 Studio Server & Clients tests for each affected feature; death/disconnect/late join/duplicate interactions; save-close-reopen and restore proof; evidence names/links.
L4: private published multiplayer with invited real people, real phone and network effects before alpha/public decisions; accurate classification and performance evidence.
Rules: after ANY main gameplay integration, run at least main Studio smoke if Studio access actually present; if not, mark BLOCKED/UNVERIFIED and do not assert feature complete. After level or asset changes, test collision, scale, lighting, graphics/performance, audio accessibility. One playthrough all the way to ending becomes mandatory each development day once game is playable. Any S0 wrong-place sync, loss of scene/source, exploit, critical softlock or game failing to load stops feature development.

## 7. Asset production and performance
Read docs/14–16 and docs/15 inventory. Read-only asset candidates identified: Feudfall `Assets/Audio/Ambience/archive_hum.ogg`, `Audio/Match/broadcast_open.ogg`, `Audio/UI/click.ogg`, `src/maps/NinthArchive.rbxmx` etc; original Dreadfall `src/server/MapBuilder.luau` and lighting/smoke test reference docs. Inspect actual licence, assets manifest, script dependencies and Roblox asset permissions; do NOT assume any candidate works in new universe or import unsafe model scripts.
New Blender originals: modular industrial corridor kit, doors, power/signal consoles, distinctive Echo silhouette, rig/animations and a few storytelling props. Keep editable source .blend, export Roblox-supported format, import into approved new Studio place, measure geometry/collision/mobile performance and mark an asset TESTED only with real Studio evidence. Greybox gameplay before elaborate art. Prefer reusable modular mesh kit to 100 isolated assets.
Audio: restrained original/licensed ambience, spatial cues, mild impact layers and subtitles; no need to clone real player voices or use unlicensed IP. Accessible visuals even at volume zero.

## 8. Monetization and business (NO live sales until explicit owner approval)
Free complete story; never sell revives, light strength, mandatory clues, shortcuts, combat advantage, paywalls or randomized paid loot.
Optional proposed products after strong gameplay and policy/receipt tests: 49 Robux radio casing pack; 149 supporter pass/nameplate; later 249 suit cosmetics; optional supporter tips only when reliable MarketplaceService.ProcessReceipt and idempotent durable entitlement have been tested. These prices and products are hypothetical, not owner-approved. No need to build marketplace code in first 3 days, and never place purchase prompts in private alpha.
Use server-authorized ownership and durable receipt handling; never trust prompt-finished client events. Validate actual Roblox API/policy, pricing, revenue share and maturity/reach requirements at implementation date.
Marketing: clear industrial sci-fi brand ("They called for a repair. Something answered."), genuine gameplay captures, Roblox icon/thumbnail, short social teasers, invite-only 5–10 testing crew, later 20–50 invite beta, measure first-action time, stage completion, rage quits/softlocks, ending rate, co-play and real replay. No paid ads/creator sponsorship without owner approved budget. Never use mock concept art to misrepresent playable footage.
Business decisions should follow actual retention/replay and quality, not speculative sales. See docs/20.

## 9. Three-day execution — one builder, no AI agent handoffs
DAY 1: establish exact new Studio place, Git/scene source of truth, safe Rojo allowlist, restore + save/reopen proof. Implement one server-authoritative interaction, visible shared objective, one-room spawn/ending stub, 1 and 2 client Studio smoke. Run checks and save matching Git+Studio checkpoint. If restore/2-client fails, day 2 becomes repairs.
DAY 2: create all six zones as one joined greybox in SAME MAIN scene; clear paths/doors and checkpoints. Implement 3-breaker power puzzle, server state, minimal archive clue, ending stub, solo and 2-client start-to-end, 4-client shared-objective smoke. Save/reopen and backup.
DAY 3: integrate frequency puzzle, 3-act narrative subtitles, authored Echo reveal/chase/recovery, ending/debrief/replay, minimal touch UI; test 1/2/4 in main place with actual results. Re-estimate private alpha ETA based on measured first full-run time, bugs, session stability and remaining work. These are ambitious **targets**; failures are reported, never concealed.

DAYS 4–14: gameplay completion/co-op recovery→Echo fairness→4-client resilience→mobile/accessibility→full pacing test→Blender/rights-cleared art→audio polish→small replay layer→real friends/mobile testing→release-candidate backup/QA→owner-approved private alpha. docs/24 supplies detailed gates; its historical Codex references are superseded.

## 10. Productive autonomous continuity — within actual tools and permissions
You are to be proactively productive for the full current execution session, not repeatedly stop for trivial confirmations or just write more plans. Prioritize **one accepted playable task at a time** in dependency order, with small reviewable commits and frequent real checks. When a goal finishes, select the next highest-value unblocked GitHub issue. Before stopping for provider quota, network failure or tool/session end: persist branch, commit, test evidence and docs/22 next action, then exit safely. The next Claude session reads the checkpoint and resumes exactly; never start over or invent continuity.
If the owner later explicitly authorizes genuine unattended operation, it requires a verified local Windows runner, exclusive process/Studio/Rojo ownership, watchdog/stop, clean restart, quota/error backoff, and observed canary tests. Until then, do NOT claim 24/7 or background execution. No plugin/GitHub issue automatically wakes Claude. Do not activate the quarantined old Dreadfall controller.

## 11. Claude's own high-reasoning challenge questions (answer using evidence, not debate)
Q1. What actually exists in current source and the main Studio place? Give path, SHA, scene/version and UNKNOWNs.
Q2. Can the exact Git SHA + saved Studio scene be restored together on restart, with an actual reopened proof?
Q3. Which ONE user-facing gameplay milestone makes the canonical game more complete today?
Q4. What is the simplest secure phase, remote and puzzle architecture that avoids solo/co-op softlocks, duplicated inputs and stale joins?
Q5. Where does the first player feel mystery/fear within the first 5 minutes, in a way a stranger understands without narration by the developer?
Q6. Which source-repo assets have clear rights and reduce net work, and which Blender originals are worth their measured import/testing overhead?
Q7. What tests will actually expose today's highest-risk integration mistake? Show failing test first when appropriate.
Q8. Which UI/lighting/audio choices preserve game clues with sound off, reduced flashing and low mobile graphics?
Q9. How long does a first-time player actually take to reach the ending, by player count? Do not extrapolate game length from a clock plan.
Q10. What blocks monetization or public release technically, legally or experientially? Keep it disabled until approved.
Q11. What is the next risk-adjusted priority? Forecast p50/p80 productive hours using previous accepted tasks, actual rework and smoke-test overhead.
Q12. What was preserved from the last checkpoint, and what new evidence says today's revision is more playable?

Use deeper thinking for architecture, lifecycle and safety decisions, but convert decisions into game changes and tests. You may conduct a critical self-review pass, but no Codex or other AI agent can be used.

## 12. Required report at the end of EACH bounded work session
- **Identity:** observed model name, Windows host evidence, repository/branch/base/main SHA.
- **What actually changed:** code files/assets/Studio components, issue/PR links, exact commits.
- **User-visible playability:** what happens from spawn to result, actual supported player counts.
- **Verification:** unit/lint/CLI PASS/FAIL, Studio 1/2/4 client test mode and evidence, real mobile/published tests or NOT RUN.
- **Save and recovery:** confirmed universe/place ID, Rojo mapping, Roblox saved version/time, private backup path/hash, last known-good tuple; UNKNOWN if missing.
- **Blocked/risks:** S0/S1 and owner-only decisions, scope cuts, unverified claims.
- **Forecast:** measured accepted output, p50/p80 remaining productive time, highest next priority.
- **Next step:** one exact small implementable action, written to docs/22 + appropriate GitHub issue. No generic claims like "everything done".

**NOW EXECUTE.** Start with identity + recovery audit, then one playable objective. If you cannot access Windows Studio, be truthful and deliver safe source-side progress without claiming a Studio-tested game.