# 30 — CLAUDE IMPLEMENTATION DESIGN: ONE REAL ROBLOX GAME
DESIGN ONLY. Do not claim any module below already exists.

## Current checked repository state before pivot
Minimal src/shared/Config.luau and two client/server bootstrap scripts; Rojo 7.7.1 and Selene 0.32.0 pinned; guarded Python scripts/dev.py; source-only CI. Actual Studio-authored 3D geometry, verified Roblox place ID, game assets and multiplayer run UNKNOWN. No runtime game services currently implemented.

## Current strict invariants
Claude Opus/Claude Code is sole AI implementer/tester. ChatGPT is authorised to coordinate/edit planning and simple configuration by explicit owner request here, not to start Codex or multiple agents. Original Dreadfall BigKilla75/roblox-game and Feudfall BigKilla75/revengers READ ONLY; Academy unrelated. One-way rights-cleared imports possible, after confirming public destination vs private source rights. No modifications to originals.
Exactly ONE separate new Roblox Studio universe/place; default.project.json -> servePlaceIds [] until owner verifies ID; all live sync blocked. One server, canonical place, local backup and rollback discipline. Do not blindly reinstall Rojo/Selene on Windows.

## Suggested high-value module layout (future work)
src/shared/Config.luau — constants and feature gates; never authority for secrets.
src/shared/Definitions.luau — typed item/scenario/broadcast definitions; server validates all.
src/server/SessionService.luau — stage machine, team objectives, lifecycle, reconnect.
src/server/ScenarioService.luau — seeded, curated, constraint-checked scenario cards, not arbitrary probability.
src/server/InventoryService.luau — ownership, item IDs, slots, one-writer transactions.
src/server/ShopService.luau — fictional cash & finite shop stock; atomic transactions.
src/server/RadioService.luau — bulletin timeline and event effects; late-join sync.
src/server/InteractionService.luau — validates distance, cooldown, object identity/state, user reachability.
src/server/ThreatService.luau — one looter FSM with safe pursuit and recoverable theft.
src/server/ResultService.luau — server-calculated endings and free achievements.
src/client/HUDController.luau — current task, resources, warning, accessibility.
src/client/RadioController.luau — transcripts, volume, wind-up, captions.
src/client/InteractionController.luau — desktop/mobile prompt, hold/cancel states.
src/client/AtmosphereController.luau — local audio/light/weather FX without game-state authority.
The names are suggestions; reduce files if premature architecture prevents first playable vertical slice.

## State diagram
BOOT -> HOME_INTRO -> PREPARED -> SUPPLY_OPTION -> LOCAL_UPDATE -> DECISION -> (STAY_HOME | HUB | REST_CENTRE) -> ENDING -> RESULTS -> RESET.
Branch states can be optional; transitions strictly permitted by server objective predicates and versioned stage revision. Log structured checkpoints for debugging, not personal details. Every state has bounded timeout, safe retry and fallback instruction. Reconnect gets authoritative snapshot, never a purely local replay.

## Network surface and security contract
- Client sends Intent(verb, targetId, optionalItemId, requestId). Never accepts client-reported money, item quantities, objective stage, radio scripts, NPC position, damage, or completion.
- Validate input type, schema, allowed verbs, target existence, player/target distance, alive state, stage, object readiness, inventory membership, stock and per-player throttling. Reject NaN/infinity and malformed strings/IDs. Use idempotent request IDs or server-held single-flight for buy/pickup/drop and receipt awarding.
- Server owns cash, item stack, tool ownership, finite stock, enemy state, session score and outcome. No client grant reward.
- Exploit test: remote spam, teleport to shop, free-buy attempts, duplicated pickup, stale broadcast, late join, disconnect while item transfer, death holding radio, simultaneous spend, replay state leak.
- Do not overengineer DataStores in alpha: session-only resources; persist free badges only when tested. Real Robux purchases stay OFF. If later enabled, use server MarketplaceService entitlements and robust ProcessReceipt idempotency and durable completion. Fake "prompt finished" must not count as purchase.
- Never deploy unreviewed Toolbox packages/scripts or external private assets. Network ownership and parts can be abused; anchor/static collision and server constraints as needed.

## Studio and source truth / Rojo
Project root set to "OperationBlackSky" only if guarded Python validation and CI build artifact updated in same atomic change. Name is internal, NOT authorization to sync.
Source commit + Studio saved scene + owner private .rbxlx backup + checksum are ONE release checkpoint. For every major change: prove a marker object survives Studio save/close/reopen and independently recover backup. The Rojo source-only .rbxlx build is NOT the real authored Studio map.
Never put authentic private game assets or proprietary copies in public repo without rights review. Original files remain where they are.
Use one place, one reviewed Rojo mapping; allowlist always empty until verified ID and owner approval. Perform Studio 1,2,4 players, check mobile real device. Never claim CI automatically proves gameplay.

## Performance and accessibility acceptance
PC/mobile target: acceptable responsive controls/legible UI on real low-mid Android; profile frame time, memory, network, latency in actual test. Set performance budgets after measuring target devices (do not fabricate 60fps guarantee). Limit dynamic lights, simultaneous pathfinding, collisions, high-poly props, and texture sizes. Stream environment only if tested.
Subtitles default ON for broadcasts; no mandatory audio; reduced flashing/camera shake; font resizing; safe UI areas; adequate contrast; never require colour discrimination or fine motor reaction impossible on touch. Pause/replay journal must remain functional during degraded audio.

## Testing tools
Python test/dev guard + Selene + Rojo source build are prechecks; actual playable proof requires Studio real game; never re-label an XML artifact as playable. Prefer Studio's Start Server + 1/2/4 Player test, with private place network/multiple devices, logs and screen recordings. CI must stay no-publish, read-only credentials, no production API keys.
