# 02 — Gameplay loop and 1–4-player co-op design

## Core loop
Join safe lobby -> choose start / wait for friends -> story objective -> explore -> read clue -> interact/puzzle -> survive one pressure beat -> regroup -> checkpoint -> act advance -> ending -> debrief/replay. No combat, crafting, loot economy or paid resurrection.

## Session model
- One authoritative SessionController per Roblox server. Maximum players set to 4 in Studio experience settings; enforce server-side.
- State enum: BOOT, LOBBY, INTRO, POWER, INVESTIGATION, SIGNAL, CONTAINMENT, ENDING, DEBRIEF, RESETTING. Explicit permitted transitions, once only; guard invalid/out-of-order interactions.
- Alpha: single Roblox place, private/friend playtests. Owner chooses whether host/manual start or automatic start after short countdown. No public party/matchmaking promise until lobby/reserved-server flow is implemented and proven.
- Once a run starts: late join enters spectator/safe waiting area then joins at next act checkpoint; don't teleport directly into a chase. If no checkpoint remains, show 'Next run' wait option. If private test setup disallows late join, document it and test.
- Solo must work. Never require a second account or voice chat to progress.
- Shared objective flag per session; evidence and optional rewards credited per player from verified server interactions. Player departures don't invalidate already completed tasks.
- If all players leave, session ends; if one remains, objectives remain solvable. If host leaves, no host-dependent destruction.

## Interaction spec
- Each interactable has stable ID, stage eligibility, distance/line-of-sight bound, cooldown and server authorization.
- UI shows "Interact" prompt and icon/touch target, with controller alternative.
- For repeated inputs, server handles idempotency. Advance stage only once, even with all four players pressing at the same time.
- Doors: server authoritative locked/open state, anti-spam, collision and safe respawn after transition. Maintain clear route.
- Puzzles: persistence in memory for the current run, resets on full run restart, not on one player's death.
- Clues: optional personal journal and team-shared progress; no unsynced required clue pickup.

## Fear systems
- Shared threat state is server authoritative, with client visual/audio effects per-player for atmosphere.
- Threat state: DORMANT, SIGNALING, REVEALED, PURSUIT, COOLDOWN. Give warning before danger and a guaranteed recoverable route.
- Light/audio changes triggered through network events with timestamps/sequence IDs; repeated events safe to receive twice. Never rely solely on the client to set objective completion.
- Sound attenuation, spatial audio, clear mixes, sliders, optional camera shake on/off and reduced flashing. Critical cues also have subtitle/visual indicators.

## Fail / recovery
- Prefer short incapacitation (downed/respawn at act checkpoint) over permanent elimination. If all players fail, restart only the immediate encounter or act, not 30 minutes.
- On death: temporary spectator camera restricted to safe teammates or checkpoint, then respawn in a safe zone. Dead player cannot solve puzzles remotely.
- If solo dies in scripted chase, reset chase with a hint. Limit frustration; allow 'story mode' accessibility toggle to slow threat without reducing chapter access.
- On network disconnect: the team continues; a reconnecting player joins at safe checkpoint if platform/game session permits. Do not promise guaranteed reconnect to a particular Roblox server until verified.

## Fairness, accessibility and device targets
- Default first-person with optional reduced camera motion/FOV comfort if supported; no hard enforcement of motion-sickness-inducing effects.
- PC keyboard/mouse and touch baseline. Controller in next phase unless acceptance test proves it now.
- Text-only fallback for every audio cue, color+symbol puzzle coding, subtitles default on and readable, brightness/volume controls, menu safe areas, respawn logic.
- Support low graphics by reducing effects (not clues or interaction visibility).

## Co-op tension design
Players receive the SAME canonical objectives but may see different harmless environmental anomalies. Do not fabricate actual teammate messages or voices. Work together on paired consoles / scanning while keeping solo sequential route.
Players can revive/regroup and discuss. Use location-based collaboration, not mechanics that punish strangers for failing timed voice coordination.

## Reward
Per-run debrief shows whether team completed, clues found, progress record, and earned free badge/cosmetic (after persistence implemented). No score penalties for leaving due to disconnect. Prevent duplicated rewards server-side.
