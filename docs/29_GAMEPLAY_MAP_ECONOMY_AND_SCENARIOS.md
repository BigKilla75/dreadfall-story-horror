> **GENRE IMPLEMENTATION OVERRIDE:** Follow [docs/36](36_GENRE_SELECTION_AND_CORE_LOOP.md): the map is a repeated **risk-and-return arena** with branching safe endings, not an open-world town simulator. Resources, ATM and shop stocks produce quick tradeoffs; they are not a laborious financial economy. First three minutes must be fun, every authored scenario winnable solo, and both safe-home/assistance routes have active player choices. Rewards free and cosmetic only; no real-life advice claims.

# 29 — DETAILED PLAYER SYSTEMS, LEVEL, NPCS, EVENTS, PROGRESSION
All values are **tuning hypotheses** for private testing, not balanced/implemented mechanics.

## Brookmere navigable graph
[HOME] -> [TERRACED LANE] -> [CORNER SHOP + ATM] -> [HIGH STREET] -> [MILL LANE] -> [COMMUNITY HALL]
[HIGH STREET] -> [RAIL FOOTBRIDGE] -> [SCHOOL REST CENTRE]
[HOME] -> [REAR ALLEY] -> [MILL LANE] (safe alternative revealed early)
All core paths readable from landmarks; blocked route has two alternatives, no maze. One small rail crossing prop, bus stop, post box, temporary roadworks and pharmacy facade sell Britain with cheap geometry. Do not copy actual named shops/brands/official livery. Opening home is an interior; shop and hall are interactive interiors; other facades may be exterior only.
A sandbox layout is not a guarantee of geographic accuracy; validate travel time with actual avatar walking speeds and mobile controls.

## Item system and cash
- Backpack: 5 slots default; one equipped torch and one held radio in dedicated slots so beginners cannot accidentally discard their only information channel.
- Core item definitions: bottled water (1), shelf-stable food (1), batteries (1), torch (tool), battery/wind-up radio (tool). One optional blanket/first-aid/medication marker is a story objective, NOT medical advice.
- UI uses icons + words and slot capacity; no stacking bug, duping, accidental loss during death or UI load.
- Cash: fictional pound notes, illustrative start £5–£15; optional functioning ATM with illustrative withdrawal £10–£30 if available and account conditions; choose "attempt ATM" but never mandatory. Some scenarios ATM fails immediately. Shops sometimes accept cash, sometimes only barter/help; store stock realistically finite and can be exhausted by team, not globally exploited across random servers.
- Pricing examples purely play balance: water £2, tin meal £3, cells £4; all scenario-scaled and labelled game values, NOT actual price predictions. No conversion between in-game £ and Robux. Cash is not a persistent paid currency.
- Individual bag plus consent-based give/drop action; no theft by other human players, PvP or currency gifting. NPC looters may steal only one common non-key quest item with predictable recovery path. Essential radio/mission item remains recoverable/free.
- No hunger/thirst depletion in first 20 minutes. A preparation score (missing food/water/warmth/info) shapes the ending, reflecting preparedness not physiological death from 30 minutes without food.

## Broadcast and player choice
At scripted checkpoints, the server marks one approved bulletin. Players have radio menu "Latest update" and accessible paper notices at community locations. Radio consumes one battery unit only as an optional immersive mechanic; **never** permanently gate required info. Low battery -> wind-up action / public loudspeaker / shelter notice fallback.
Radio causes *state* changes: road closed/open, hub door activation, enemy patrol change, environmental hazards enabled, next task hint.
A player may go home and remain indoors; objective hint recommends evidence-based decision, not "always head outside."

## NPC and enemy AI P0
- Civilian helpers: one static shopkeeper and one volunteer; dialogue selects from authored tree. Friendly helper path demonstrates community resilience.
- Looter threat states IDLE -> OBSERVE -> APPROACH -> THREATEN -> TAKE_ONE_NONCRITICAL_ITEM -> RETREAT -> COOLDOWN; can switch to short CHASE (bounded path and time, not lethal). State transitions and loot actions server owned.
- Warning signs: footsteps, clothing silhouette, lantern sweep, NPC barks with subtitles. Player has escape/shortcuts/hiding. Can shove to open space but no bloody melee or guns. NPC never camps spawn/hub; safe zones and invulnerability after respawn.
- If stolen, recover dropped bag at marked location OR earn replacement by helping volunteer; no unrecoverable softlock. Looter cannot remove the only radio or final item.
- Gang: pre-scripted distant group at one junction (not smart AI swarm); blocks route/creates tension, not farmable combat.
- Threat budget: fewer than 2 simultaneous active pursuers in 4-player P0. Pathing fallback to patrol, safe abort on invalid paths, avoid overusing expensive PathfindingService loops.

## Co-op scaling
Solo: one player can pick up all essentials, use alt safe routes, complete radio tasks and finish.
2 players: can split between shop and rear alley, but each player's objectives are clear; shared team state catches up.
4 players: more carrying options/choices; NPC attention may be tuned without increasing required items or HP grind. Total team minimum preparations do not scale linearly with party size.
Join-in-progress: sync latest broadcast, current scenario, remaining supplies, hub state, and nearest safe spawn. Disconnect/death does not strand quest items. If all leave, session ends cleanly. Repeat runs create clean fresh state, not retained props from previous round.

## Two curated launch scenario cards
CARD A / "STAY PUT": home is intact, shop partially available, national bulletin suggests indoor preparedness; local high-street theft makes travel unwise. Winning path HOME SAFE. Optional hub visit for help, but not mandatory. Replay changes first accessible resource and one blocked street.
CARD B / "ASSISTANCE ROUTE": household needs additional help in fiction, community hall confirms it can assist, railway road partially blocked and ATM has failed. Winning path HALL HELP or HOME WITH SUPPORT depending choices. Only local verified fictional announcement opens hub; alternative rear lane prevents softlock.
Future CARD C / "CENTRE TRANSFER": a specific small area becomes unsafe and rest centre opens at school; do not publish until independent QA and accurate wording review.

## Round result and free progression
Record run outcome, scenario, preparedness checklist, whether every human team member reached a safe conclusion, assists, optional neighbour-help action and replay seed. Cosmetic recognition: free "Wind-up Witness", "Good Neighbour", "Brookmere Prepared" badges/collectibles (platform badge costs/limits reviewed separately). No ranking of players by harming NPCs. Replay button returns same party to new seed (or gracefully handles missing players). Free narrative journal provides reasons to replay. Persistent rewards only after safe DataStore implementation; for P0 session-only result is acceptable.

## UX/atmosphere
British road signs, council notices, bus stop, corner shop shutter sounds, damp pavement, streetlights failing in a cascade, distant dogs/police sirens and subtle battery radio crackle. No direct copying of actual broadcaster idents, real high street trademarks or headlines. Subtle disaster rather than horror monster. Players' flashlights must not blind players or wash out mobile UI.
Readability: large objective text, minimap optional, landmark arrows not waypoint spam, text equivalent for all audio, high-contrast and colour-blind safe inventory cues.
