# 01 — Story, level design, horror direction and 30-minute pacing

All names and narrative beats are **proposals** for owner creative approval, not existing lore.

## Story synopsis
Relay Nine once filtered emergency transmissions from a quarantined district. A call for repair is received after years of silence. The crew enters to restore the station for an evacuation route, but recorded voices repeat events before they occur. The Echo is a signal that can predict/control automated systems and lure crews into completing a relay. The evacuation was a cover: the station's outbound amplifier would broadcast the Echo beyond quarantine. In the ending, the crew intentionally severs the amplifier, but the final console displays one last message: 'Request received. New crew dispatched.' Potential follow-up without making this chapter feel incomplete.

## Map: six reusable interconnected zones
A. Drop-off / sealed gate (introduction, lobby spawn).
B. Maintenance workshop (first fuse, visual onboarding, respawn checkpoint).
C. Power gallery (breaker puzzle, first anomaly).
D. Relay corridor / archive alcove (search, collect evidence, alternate paths).
E. Communications control room (frequency puzzle, subtitles and broadcasts).
F. Amplifier core / service tunnel (pursuit, emergency cutoff, ending).
Keep navigation loops and several sightline bends; use locked access and light/audio transforms to make one small map feel changed rather than building a huge one.

## Timeline target (pacing budgets, not fake delays)
00–03 Arrival: cinematic environment without unskippable camera lock. 'Restore facility power' instruction, tutorial flashlight/interact.
03–09 Power act: retrieve component, route to workshop, two-step breaker puzzle, first light failure, one optional note.
09–14 Investigate: command center opens, abnormal radio warning, search 2 clues and optional journal; players can split and regroup.
14–20 Signal act: tune two consoles and align three relay indicators, environmental contradiction. Solo sequential steps; squads can divide roles. The station mimics an automated dispatcher, not actual player speech.
20–26 Containment act: a false evacuation instruction routes to service tunnel, short telegraphed threat stalking event, one recoverable pursuit and final switch.
26–30 Amplifier resolution: cooperate to sever circuit; clear reveal, visual consequence, final broadcast and results screen.
Median target 25–35 minutes depends on measured first-time playtests; no forced 30-minute clock. If players finish in 15 min, add purposeful exploration/beats, not waiting rooms.

## Two puzzles only, made well
**Power routing:** 3 labeled breakers, one physical schematic, solve in order. Wrong entry causes a creepy sound/reset to last safe step, never random instant death. In solo: complete sequentially. In co-op: one reads schematic, another operates breaker, but both stations accessible to everyone.
**Signal alignment:** dial 2 frequencies using audio-visual waveforms; verify by color/shape for deaf players; two consoles 10 meters apart, optional synchronized 'lock' timing of 8 seconds, but solo can set both with persistent states. Always show a legible fallback hint after repeated failures; do not paywall hints.

## Horror beat table
- Initial corridor: distant metallic tap timed when first player passes, localized for team.
- A non-player silhouette behind glass; gone when players round corner.
- Contradictory dispatcher: 'All personnel accounted for' while security roster clearly shows station empty.
- Lights fail after relay alignment, leaving emergency route guidance.
- The Echo crosses an intersection during a nonfatal first reveal (sets threat expectations).
- One 45–90-second guided escape/avoid sequence, predictable cues and safe cover; no instant unavoidable kills.
- Final quiet after disconnect, then ambiguous transmission in results screen.
No reliance on huge strobe effects, graphic gore or ear-damaging audio.

## Directed enemy constraints
One original licensed silhouette model; server-authoritative trigger/target, simple movement between authored waypoints or short pathfinding, line-of-sight and finite chase boundaries. Threat must not teleport on-screen, cheat through walls, kill during disabled controls, camp the respawn or break solo. If AI fails, use a scripted corridor threat with a clearly telegraphed chase rather than ship broken navigation.

## Writing and presentation
Short lines, readable subtitles (large text, safe-area), one optional log at each act, no excessive exposition. Voiceover optional and only with owned/licensed audio. Important story knowledge always conveyed visually and textually; don't require voice chat or hearing. Skip/fast-forward repeated opening scenes in later runs.

## Post-alpha endings
One ending is required in alpha. After metrics: optional truth ending if 4 evidence fragments are found; alternate route affects payoff but doesn't require Robux. Never fake a multiple-ending claim when only one ending is implemented.
