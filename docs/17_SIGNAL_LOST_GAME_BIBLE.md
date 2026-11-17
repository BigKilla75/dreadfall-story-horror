> **ARCHIVED — 17 NOV 2026:** Retired SIGNAL LOST story/workflow/monetisation only. **NOT ACTIVE.** Current game is OPERATION BLACK SKY; do not implement the Echo, Relay Nine, sci-fi puzzles or Codex tasks. Follow [README](../README.md), [Black Sky bible](27_OPERATION_BLACK_SKY_MASTER_PLAN.md) and [Claude's current prompt](34_CLAUDE_BLACK_SKY_MASTER_PROMPT.md). Original text retained below as history.

# 17 — SIGNAL LOST: integrated game-design bible (owner-requested plan, 15 Nov 2026)

STATUS: PROPOSED DESIGN / NOT IMPLEMENTED. This expands, rather than discards, docs/00–16. The working title, names, prices and marketing dates require owner's final approval. Existing Dreadfall is postponed; it is NOT the source game for this IP. Feudfall and original Dreadfall are READ-ONLY source candidates for licensed/owned asset copying, never dependencies.

## A. Product positioning and constraints
- Tagline: "They called for a repair. Something answered."
- Elevator pitch: a crew of 1–4 enters a silent communications relay, restores systems, uncovers a deceptive dispatcher and must sever an outbound signal before an Echo escapes.
- Player contract: 25–35 minute FIRST clear target; ~20–25 minute experienced replay is fine. One complete, understandable ending; optional secrets; all gameplay free; no PvP, weapons, giant open-world, forced voice chat, loot boxes, paid skips or deep procedural generation.
- Platform first: Windows PC and mobile with physical-device testing; controller after proof. Target accessible mild horror with no explicit gore, no mandatory audio, no excessive flicker. Actual Roblox content classification must be completed before public reach.
- Production target: 14 active-development days for a plausible private alpha with a rigid day-three feasibility gate, not guaranteed public launch or an asserted calendar completion date.
- Non-goals: shared Dreadfall lore, imported Feudfall combat, complex pathfinding, microtransaction economy, custom matchmaking servers and untested high-poly Blender assets.

## B. Player experience, moment-to-moment
1. Open in a quiet, readable drop-off gate. Within 60 seconds interact with emergency beacon; dispatcher speaks/texts "Restore power to open containment".
2. Explore 6 connected zones, observing architectural landmarks and a directional objective display; meet one small puzzle in first five minutes.
3. Every 3–5 purposeful minutes get an escalation: contradictory notice, silhouette, controlled blackout, radio anomaly or directed near-miss. Use spatialized original sound; visuals/subtitles must carry the same critical information.
4. Cooperate by splitting across readable sightlines, not mandatory simultaneity or voice communications. Solo can complete identical objectives sequentially.
5. Encounter a distinct Echo silhouette (not constantly pursuing), survive a fair signaled chase, cut the amplifier and watch a complete resolution.
6. Results screen reports chapter clear, clues, time, free rewards, replay invite and optional cosmetics later. Let players leave without purchase interruptions.

## C. Six-zone facility and navigation contract
A. Arrival Gate — start, intro, safety options, first interact, exit/backtracking.
B. Maintenance Workshop — first fuse, tools, checkpoint, short clue, recovery.
C. Power Gallery — three breakers and visible schematic, blackout preview, first shadow.
D. Relay Archive — incident logs, optional hidden evidence, alternate sightline, wrong-voice clue.
E. Control Room — two frequency stations, three indicators, critical contradictory broadcast.
F. Amplifier Core / Service Tunnel — telegraphed Echo reveal, 45–90-second guided pursuit, final cutoff, ending/debrief.
Graph: A→B→C→D→E→F with D↔C and E↔D optional shortcut when safe; no mandatory labyrinth. Doors convey locked state, accessible hints and clear team reset points. Use one fixed whiteboxed layout for alpha. Any alternate corridor or seed is P1 and must not introduce softlocks.

## D. Narrative beat sheet (provisional dialogue, not final VO)
- 00:00 Arrival: emergency dispatcher identifies Relay Nine as abandoned-but-operational and asks for reactivation.
- 01:00 A player receives the first repair task; lights reveal a crew list with dates that conflict with the recorded emergency.
- 03:00 Fuse found. A shadow retreats behind observation glass once, not a lethal scare.
- 05:00 Power puzzle: breaker order requires reading the schematic, simple solo path.
- 08:00 Power returns; the radio speaks about a crew member who does not exist. First contradiction visible in archive.
- 11:00 Security tape indicates "broadcast quarantine", not "evacuation"; dispatcher supplies a plausible lie.
- 15:00 Signal alignment: two consoles must hold valid settings, three waveform indicators converge.
- 18:00 The first clean signal is not speech but a prediction of an event that happens a few seconds later.
- 21:00 The Echo silhouette forms. Emergency lights and arrows establish escape route; a 45–90-second chase is fair with checkpoints.
- 25:00 Team reaches cutoff; visually readable instruction explains that powering the amplifier helps the Echo.
- 28:00 Sever power, station quiets. Result: evacuation never happened; the signal was asking to be retransmitted.
- 30:00 Final text: "Request received. New crew dispatched." Complete ending, optional sequel hook.
Audio is decorative, never essential; all required instructions have a visible/captioned counterpart. No impersonation of real players or capture of voice.

## E. Puzzle contracts
POWER_01 — 3 breakers, schematic with 3 visually distinct labeled steps; each valid step moves server state forward exactly once. Wrong attempt plays non-punitive glitch and explains next hint after repeated failures. All players see same progress. Objective resolves with server authorization, never client-local state.
SIGNAL_02 — two consoles ~10 m apart; set persistent frequencies/visual waveform shapes. Parallel co-op, sequential solo. 8-second group lock is OPTIONAL and cannot require two players. Every legal setting yields an explicit state update; failure never strands late joiner. Final frequency check performed on server.
CUT_OFF_03 — climactic two-stage cutoff with safe pause/checkpoint; not a brand new complex puzzle. A player can finish alone. Prompt must remain reachable after any chase outcome.
Investigate clue pickups are optional; main progression needs no random object hunting.

## F. Threat design
The Echo uses finite states DORMANT→SIGNALING→REVEALED→PURSUIT→COOLDOWN. Signal for danger with light, distinct audio and subtitles, then short authored motion with defined safe corridors. Server owns encounter state, pursuit bounds, hit logic, retry/cooldown. No instant kills through walls, on spawn or during input lock. If humanoid pathfinding is unreliable, replace with scripted moving silhouette + authored pursuit triggers; preserve narrative payoff.
Solo failure resets only active segment with an additional hint. Team member death respawns safely and never resets team progress. During chase, late joiners wait until a safe checkpoint.

## G. Networking + data architecture
- One universe, one MAIN place for gameplay and test. One canonical Studio scene; no competing place builds. Code tracked in Git, Studio-authored environment in the canonical Roblox place plus verified immutable dated export/backups (partially managed Rojo).
- SessionService server-only single writer with explicit states and increasing runId/revision. Other services request transitions through validated methods. Never allow client to send stage, victory, money, owned pass or raw Instance references.
- Interaction registry uses short IDs; server validates live player, stage, range, action, cooldown, LOS as required, and payload size/types. Reject replayed/forged/flood requests. Snapshot-on-join and sequence-aware client replay avoid divergence.
- Build thin services only as needed: Session, Objective, Interaction, Narrative, Threat; a separate Profile/Commerce service after P0. All services initialized once and independently testable.
- Versioned content config for zone/objective IDs; deterministic seed 1 during P0. DataStore only after safe write/retry/failure handling and clear requirement. Commerce receipt processing must be durable and idempotent.
- Studio and Rojo boundaries: Rojo owns mapped files/scripts; Studio owns authored geometry, terrain, objects and game settings. Explicitly document which instances Rojo is allowed to replace; NEVER blindly overwrite Studio assets.
- No unreviewed remote asset fetching; no external API keys or Roblox auth saved in repo. Separate place ID allowlist must remain active.

## H. Art/audio/Blender production
Visual palette: graphite/oxidized steel, cool blue-white utility lights, red emergency state, pale green waveform highlights; low cost on mobile. Hero identity: Relay Nine tower waveform insignia, broken silhouettes, static.
Reuse audit first: Dreadfall/Feudfall source assets are READ-ONLY; check license and scripts, log in docs/15. Prioritize geometry, material/look-dev, safe audio/animations; do NOT bulk import FPS/cargo/zombie services and do NOT touch original live asset IDs.
Original Blender priority: modular wall/floor/corner/door kit → transmitter + breaker props → Echo silhouette and simple rig → signs, debris. All editable .blend files and exports kept under versioned assets with clear naming. Test Roblox import, pivots, UVs, collision, normals, performance and actual place ID. Keep a simple fallback if an import fails.
Audio priority: air handling hum, plausible breaker clunks, glitch layers, restrained stinger, nonverbal threat cue, UI confirm. Every cue has volume control and optional subtitle/visual equivalent. License/source ledger required.
No speculative high-fidelity claims before actual captured Studio evidence.

## I. UI and accessibility
HUD: next objective (max 1 line + expandable details), team status, interactive prompt with keyboard/touch, subtitle panel and settings accessible at any time. Diegetic signs must remain readable with reduced graphics. First task visible at spawn; first response within 60 seconds target.
Settings: subtitles on by default; volume split if practical, screen-motion reduction, reduced flashing, contrast-safe symbols and adjustable hints. Test with volume=0 and low graphical preset. Mobile touch must support all mandatory interactions; all screen regions respect safe zones.

## J. Replay and progression
P0: replay/reset works reliably, fixed content seed, optional clue counter only if stable. P1: 3 pre-authored variants in clue positions / path opening / scare timing, six evidence records, free radio tags/helmet looks, team-first-clear badges. P2: short optional modifiers after chapter completion. P3: additional ending or chapter ONLY if retention justifies it.
No daily chores, no random paid crates, no repetitive paid boosts.

## K. Definition of done / release ladder
Prototype: a two-client Studio session spawns, interacts, completes one objective, reaches a stub ending; verified screenshots/logs.
Vertical slice: power→investigation→signal→Echo→cutoff is accessible (even greybox), same MAIN place survives save/reopen, has safe retries.
Private alpha: entire coherent story, 1/2/4 Studio tests, published private network test if available, real mobile smoke, no P0 softlocks, saved source+Studio backups, owner-approved invite-only deployment, payments OFF.
Public: age/reach requirements verified with Creator Hub, truthful media, receipts/persistence audit if enabled, valid game settings/permissions, documented rollback, complete owner approval.

See docs/18–21 for 72-hour delivery, agent orchestration, marketing and questions.