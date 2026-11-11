# 03 — Replayability and progression

## Thesis
Replay comes from sharing fear with new friends, finding evidence, and small *authored* variations. Never pad the story to artificially inflate minutes; don't demand daily login or buy extra lives.

## Layers
P0: Repeatable complete chapter, debrief and replay button with scene reset. Players can take different roles and paths. End screen lists optional hidden evidence (not every collectible must be implemented in first week).
P1: Three pre-authored scenario seeds. Each seed varies 2–3 clue locations, one corridor's path availability and one early scare timing. **Keep every seed fully testable**; don't generate random mazes. All runs retain fair escape route and identical story clues.
P1: Six optional evidence fragments, three free cosmetic unlocks (e.g., different helmet lights/radio tags), noncompetitive badges for first clear / no team knockdowns / full evidence.
P1: Run history, best completion, personal journal; never show false progression if data persistence unavailable.
P2: Curated modifiers chosen in lobby after first completion (Blackout, Unreliable Broadcast, Silent Echo). Each has documented change, no loot multipliers that degrade free users.
P3: An alternate ending earned via evidence, second chapter, new threat behavior, periodic short bonus transmissions. Avoid daily content promises before a content production pipeline exists.

## Deterministic seeded variant design
Server generates a seed on game start, selected from tested whitelist 1, 2, 3, with transparent per-variant data for relay order, one clue location and safe jump scare schedule. Same seed broadcast to all clients for display only. Server owns actual decisions. In P0 use seed 1 ONLY; release seed 2/3 after QA signoff.

## Objectives and achievements
- First Clearance: reach ending.
- Complete Archive: find all six optional evidence logs (P1).
- The Crew: complete with 3–4 players (P1).
- No Static: finish without chase failure (P1).
- Alternate Route: solve optional environmental hint (P3).
Rewards are in-game cosmetics/titles only, not competitive stats or cashable items.

## Exit/replay experience
At ending allow 20-second optional debrief, team vote to replay, clear scene reset and act 0 restart. Allow players to leave and earn completed rewards; avoid forced purchases after emotional climax. Completion data save must be server-side and resilient to retries.

## Replay acceptance
A second run meaningfully differs by an authored event or optional clue *after P1*. Do not advertise randomized runs until variants are actually implemented and tested.
