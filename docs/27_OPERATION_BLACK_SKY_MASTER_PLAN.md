> **V2 GENRE CLARIFICATION — 17 NOV 2026:** This game's **UK blackout is the realistic premise, not the genre straightjacket**. The active format is **round-based co-op survival/extraction-lite**, supported by simulation details and light thriller tension. Fun, co-play and repeat sessions outrank literal emergency simulation or linear story; UK factual safety references and fictional labels remain mandatory. The authoritative choice, breakdown and micro-loop are in [docs/36_GENRE_SELECTION_AND_CORE_LOOP.md](36_GENRE_SELECTION_AND_CORE_LOOP.md). If earlier sections demand too much realism/long round/exposition, reduce them to protect the responsive 12–22-minute testable loop.

# OPERATION BLACK SKY — AUTHORITATIVE PRODUCT & PRODUCTION BIBLE
Status: OWNER-DIRECTED DESIGN PIVOT / PLANNED, NOT IMPLEMENTED. Version 1, 17 November 2026.
This document supersedes the SIGNAL LOST creative plan. Original SIGNAL LOST files 00–21 and 23–25 are retained as HISTORY ONLY. Shared asset/Studio integrity constraints stay binding. Read docs/35 for the formal transition.
Repository is still named dreadfall-story-horror; title in-game is OPERATION BLACK SKY. Repository rename and public-release actions are NOT authorized by this document.

## One-sentence promise
A 1–4 player cooperative Roblox survival thriller set in a fictional British town during the first night of a very unlikely, catastrophic UK-wide electricity failure: listen to emergency radio, prepare cash/food/water/light, make grounded decisions, deal with opportunistic criminals and reach safety together. Fiction, not a live public warning or a simulation of a specific future event.

## Product signature
- Player fantasy: "I am living through the first hours of a national emergency with my mates".
- Tone: urgent, credible, humane, tense; ordinary British people mostly behave like people, not instant anarchists. Some theft/disorder is fictional and localised. No zombies, monsters, conspiracy assertions, war, political propaganda, gratuitous gore or shootouts.
- Target device: Roblox mobile and PC from first alpha; console later if tested.
- Session: 18–25 real minutes, with 20–22 minutes target median for a first guided run, representing several *fictional* hours. Never pad time or imply this is a real-time emergency timetable.
- Party: solo through four friends. Every mandatory objective works solo; no paid advantage, voice requirement, or forced sacrifice of teammate.
- Replay: 2 curated, tested event cards first; randomise shop stock, availability of working ATM, safe routes, looter placement, and official assistance options from internally consistent rule sets. 3rd scenario only after QA.
- One canonical, owner-verified NEW Roblox universe/place. Never sync to Dreadfall/Feudfall. This same existing repo pivots; no parallel competing builds.

## The first 60 seconds — unskippable quality bar
0:00 spawn in ordinary terraced home. Lights/TV cut out within 10 seconds; nearby street darkens.
0:10 players retain movement; flashlight and wind-up radio are immediately reachable; subtitles and colour-independent prompts visible.
0:20 original fictional public-service voice reports significant nationwide power disruption, advises remaining calm and finding safe information. NO BBC voice/logo/audio.
0:35 pick up battery/wind-up radio, torch and one supply to complete a guaranteed small success.
0:50 simple clear task: "Check supplies, then decide whether to stay or go." Friends can invite/enter immediately; no lobby queue longer than necessary.
A real new player must understand why they are playing without reading a manual. No 3-minute lore cutscene.

## Primary loops
MACRO: blackout -> assess safety -> hear verified fictional in-game bulletin -> gather essentials (optional purchase where possible) -> choose risk vs preparedness -> receive changed conditions -> remain safe at home / use assistance hub / proceed to opened rest centre -> survive/end -> debrief and replay.
MICRO every 20–60 seconds: observe signal -> pick route -> interact -> assess inventory -> trade/share/help/avoid -> receive legible feedback. No fiddly hunger tick every few seconds.

## Three outcome paths; no universal mandatory evacuation
1. HOME SAFE: heed stay-put order, assemble suitable supplies, check neighbour, secure home and survive the scripted overnight interval. A valid winning path.
2. ASSISTANCE HUB: on receiving a verified local announcement that a fictional community assistance hub is operating, travel safely and obtain support; finish after completion.
3. REST CENTRE: in scenarios where authorities specifically open a rest centre for affected people, reach it through safe routes and complete assistance/check-in. Do NOT depict every school/church as an automatically open government shelter.
Player can change plan when a bulletin changes. Nobody is forced to travel simply because the game has a countdown. Travel may be safer than remaining indoors in specifically authored circumstances, not generically.

## The social hook
Four friends in a dark UK high street debate whether to buy the last water, share a torch, help an older NPC or use the blocked footbridge. Co-op improves convenience and storytelling but the server never requires simultaneous console presses. Encourage natural clips, not scripted griefing.

## First-release map
ONE dense fictional English neighbourhood "Brookmere"; geographically plausible streets, terraced houses, corner shop, supermarket frontage (limited interaction), ATM, bus stop, pharmacy frontage, railway footbridge, small community hub/school hall, and 2–3 connected side lanes. Use signage and distinctive landmarks. No open-world driving, player vehicles, multi-city map, national grid infrastructure, dynamic destruction, hundreds of NPCs or complex train systems.
Use a modular Studio greybox and small safe staged asset imports before original Blender decorative pieces. First level must fit mobile performance and readable navigation at low graphics.

## Game moments and pacing
ACT 1 (0–5 mins): ordinary home blackout; radio comes alive; assemble starter bag; an optional ATM/shop task establishes cash/payment reality.
ACT 2 (5–14): shops and neighbours; limited trading/availability; one looter presence and one safe street blocked; news about assistance; choices matter.
ACT 3 (14–22): scenario-dependent announcement, one high-tension street encounter, backtrack or shelter route, home/shelter ending, clear summary.
Avoid algorithmic AI-made announcements: every bulletin must be authored, fact checked, reviewed, and consistent with world state. Treat each scenario as a tested miniature level.

## MVP vs later
P0 PRIVATE ALPHA: boot->gameplay->ending, 1–4 server state, home+shop+road+hub, torches, inventory 4–6 slots, 3 supplies (water/food/battery), cash 1 optional source, transaction at 1 working till, original fictional radio text/subtitles, 1 looter finite-state enemy with chase/escape, 2 safe outcome paths, 1 authored scenario, UI/mobile, safe save/reopen, test logs. Use no real purchases.
P1 CLOSED BETA: 2nd scenario, secondary rest-centre ending, distinct stock/road roll, one helpful NPC, free badge/journal, party invite optimisation, onboarding rework, optional cosmetic previews.
P2 ONLY AFTER DATA: second night/chapter, more sophisticated civilian interactions, intermittent restoration, cosmetics with owner approval, additional locale.
DEFER: weapons, PvP, driving, procedurally generated town, player trading, escalating gang economy, realistic multi-day biological needs, live news, live radio feed, copyrighted broadcasts, celebrity voices, Robux supplies.

## Production constraints
7 *active productive* development days = proposed PRIVATE ALPHA target, not a verified delivery date or guaranteed scope; day 3 go/no-go; 14 days = aspirational polished private beta if 7-day target survives. If 7-day limits force cuts, keep clear survival loop, one ending, reliable co-op and real Studio saves; cut enemy sophistication, commerce or variants before cutting correctness.
Authority: docs/35 transition > current README/CLAUDE.md/AGENTS.md > docs/27–34 > historical SIGNAL LOST docs. For truth of implemented work, checked source+canonical Studio state+real test results always supersede prose.
