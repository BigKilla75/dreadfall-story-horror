# 05 — Technical architecture, Roblox platform and Git workflow

## Foundations
Roblox Studio experience authored as its own new universe/place, bound to this repository only. Luau scripts in Rojo project v7 layout. No evidence of a bound Roblox place yet. The code scaffold in src/ is not running gameplay. Owner or Claude with a local Studio environment must create place geometry, models, animation and UI, then synchronize and publish after testing.

## Source layout (target)
- default.project.json — Rojo mapping.
- src/shared/Config.luau — shared nonsecret constants, versioned settings.
- src/shared/Protocol.luau — typed remote contract and enums (to implement).
- src/server/Bootstrap.server.luau — create/start services (placeholder).
- src/server/Services/SessionService.luau — phases, 1–4 player state, transitions.
- src/server/Services/ObjectiveService.luau — server-owned objectives/puzzles.
- src/server/Services/InteractionService.luau — validated proximity requests, rate limit.
- src/server/Services/ThreatDirector.luau — deterministic encounter triggers.
- src/server/Services/NarrativeDirector.luau — timeline, cues and subtitles.
- src/server/Services/ProfileService.luau — later: completion/entitlements storage.
- src/server/Services/PurchaseService.luau — later: receipt processing.
- src/client/Bootstrap.client.luau — UI/effects bindings (placeholder).
- src/client/Controllers/TaskUI, PromptUI, FearFX, SettingsUI — implement.
- assets/ — only owned/licensed reusable assets, documented with attribution.
- tests/ — pure Luau unit tests and Studio integration test cases.

Directory names above are planned; do not mark missing modules as implemented.

## Networking contract
Client -> Server RemoteEvent: RequestInteract({objectId:string, action:string}). No arbitrary Instance or path trusted from client. Server validates known IDs in registry, eligible act/state, player alive, distance, LOS where applicable, cooldown and spam rates. Returns explicit success/failure to that player.
Server -> Clients: StageChanged({stage, revision}), ObjectiveChanged({objectiveId,status,revision}), CueTriggered({cueId, serverTimestamp, sequence}), PlayerStateChanged({playerId, status}). Single writer for server session state. Every event has a monotonic session revision/sequence. Client may request snapshot on join; clients cannot advance acts or claim badges.
No RemoteFunctions for long-running or yielding operations. Do not send massive payloads or asset instances dynamically. Never accept player-provided achievement or product ownership.

## Deterministic state
SessionService only writes canonical phase and objective flags. All stages have allowed transition table; a stage transition is idempotent, validated and logged. Event cue playback can be local but outcome is server-owned. Unique runId (server generated) scopes metrics/rewards and guards resets. Pause/timeout gracefully when players temporarily absent. Lock/serialize critical puzzle completion to prevent two players issuing double transitions.

## Account storage
P0: only in-memory state, no promise that clues persist beyond a session; ending still accessible. P1/P2: one versioned profile record per user with cleared chapters, evidence bitmask, cosmetics owned, accessibility preferences if appropriate, receipt ledger. Use DataStoreService with UpdateAsync, pcall, bounded retries/backoff, cached session state, save on exit/BindToClose; avoid writing for every interaction. Do not promise 100% persistence under platform outages. Consider session locking strategy if persistent ownership is introduced. Keep purchase and entitlement writes durable and idempotent.

## Teleports, server parties
P0: one place, max four, safe joining/late join rules. For public release, evaluate a two-place lobby/chapter system with reserved server and TeleportService:ReserveServer/TeleportAsync using Roblox's current recommended APIs; verify server reservation, reconnect and teleport failure. Do not implement custom global matchmaking in week one.
Do not rely on reserved-server teleports being fully testable inside ordinary Studio alone; perform published controlled tests.

## Security threats
Client forging interact distances, stage flags, rewards, kill events; repeated ProximityPrompt triggers; remote flood; client-supplied character instances; duplicate datastore writes/receipts; fake badge completions; plugin asset backdoors. Server checks each critical operation, caps payloads and uses allowlists. All new Toolbox content requires source audit, not just favorable ratings.

## Tooling and delivery
Rojo v7 with plugin: map file-backed scripts into Studio; verify target universe/place before live sync to avoid corrupting another project. Optional StyLua formatter, Selene/luau-analyze lint and TestEZ tests only when tool availability and version proven. No destructive scripts, force pushes or blind package upgrades.
Claude develops a feature branch. Codex reviews on another branch or PR, test first. Main is kept stable, PR template used, manual Studio evidence attached. Pin dependencies if introduced and scan licenses.
Studio testing: Server & Clients 1/2/4; device emulator and REAL phone; network simulator; remote spam and disconnect tests. Review performance with MicroProfiler, reduce expensive rendering effects on phone. Never claim build success based solely on Rojo sync.

## Observability
Server errors and stage transitions include runId, phase, objectiveId and sanitized reason, not personal chat data. Instrument server-side funnels after publishing: join, first interaction, act entry, encounter fail, chapter finish, replay, cosmetic view and confirmed purchase. Keep logs privacy-respecting, don't transmit chat or voices externally.

## Helpful official sources
https://create.roblox.com/docs/scripting/security/client-server-boundary
https://create.roblox.com/docs/cloud-services/data-stores/best-practices
https://create.roblox.com/docs/studio/testing-modes
https://create.roblox.com/docs/projects/teleport-private-servers
https://rojo.space/docs/v7/project-format/
