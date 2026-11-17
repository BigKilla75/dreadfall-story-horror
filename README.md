# OPERATION BLACK SKY — UK Blackout Survival (Roblox)

> **GENRE DECISION 17 NOV 2026:** The real UK blackout is the factual **SETTING**, not a requirement to make a slow simulator. Current gameplay genre: **round-based cooperative survival / extraction-lite thriller** (1–4 players, solo possible). Prioritise an exciting 60-second hook, meaningful supply/info/safety decisions, a full replayable round, and a safe home OR assistance-hub ending. See [docs/36 — definitive genre and replay loop](docs/36_GENRE_SELECTION_AND_CORE_LOOP.md). Not PvP, full simulation, or a linear Echo horror game.

**ACTIVE GAME — 17 November 2026:** OPERATION BLACK SKY, a 1–4-player fictional UK national blackout survival thriller. **STATUS: design plus minimal source scaffold ONLY. No verified Roblox Studio gameplay, map, tested multiplayer, asset imports or live purchases.**

A compact fictional British town. The lights fail. Gather water, food, cash where available, torch, batteries and radio. Hear original fictional emergency broadcasts; avoid occasional opportunistic looters; decide whether it is safer to stay indoors or travel to a confirmed community assistance point. 18–25-minute target first night, curated scenario replay. The original SIGNAL LOST story is superseded but preserved in Git history and older docs. Do not imply this game predicts an actual UK blackout.

> **Fictional Roblox entertainment. Not affiliated with the UK government or BBC; broadcasts are not real alerts or real-life instructions.**

## ACTIVE documents — READ THESE, not the old story-horror plan
- [27 — Complete product/game bible](docs/27_OPERATION_BLACK_SKY_MASTER_PLAN.md)
- [28 — Official UK research, realistic radio, fictional distinction](docs/28_REALISM_RESEARCH_AND_RADIO.md)
- [29 — British neighbourhood, cash, items, looters, scenarios](docs/29_GAMEPLAY_MAP_ECONOMY_AND_SCENARIOS.md)
- [30 — Secure Roblox server architecture and Studio rules](docs/30_TECH_ARCHITECTURE_AND_SECURITY.md)
- [31 — 7 active-day private alpha / 14-day beta and issues](docs/31_BUILD_ROADMAP_AND_ISSUES.md)
- [32 — Cosmetic monetisation and viral discovery plan](docs/32_MONETIZATION_AND_GROWTH.md)
- [33 — End-to-end QA and private/public release criteria](docs/33_QA_ACCEPTANCE_AND_RELEASE.md)
- [34 — **Claude Opus complete development master prompt**](docs/34_CLAUDE_BLACK_SKY_MASTER_PROMPT.md)
- [35 — Non-destructive pivot, approvals and archive](docs/35_PIVOT_DECISIONS_AND_ARCHIVE.md)
- [22 — Current verified/unknown state](docs/22_CURRENT_STATE.md)
- [26 — Sole-Claude session/recovery protocol](docs/26_CLAUDE_SOLO_OPERATIONS.md); [CLAUDE.md](CLAUDE.md); [AGENTS.md](AGENTS.md)

## Exact boundaries
Destination: BigKilla75/dreadfall-story-horror (historical slug retained). Original PvPvE Dreadfall BigKilla75/roblox-game is postponed and READ ONLY. Feudfall BigKilla75/revengers READ ONLY; Academy is separate. Do not edit, publish or sync to their places. Rights-cleared one-way asset imports require provenance and public-repo privacy review.
**Claude Opus / Claude Code is sole AI development agent; Codex is excluded.** Seven active productive days is a private ALPHA hypothesis, not launch guarantee. No public release, payments, real broadcaster audio or logo, paid ads or autonomous runner without owner approval.

## Tooling and immutable safety lock
- Current code is only src/server/Bootstrap.server.luau, src/client/Bootstrap.client.luau and src/shared/Config.luau placeholders. No claimed new survival systems.
- Pinned Rojo 7.7.1 + Selene 0.32.0 and Python scripts/dev.py doctor|build|serve; CI checks source only, **not Studio game**.
- default.project.json has **servePlaceIds: []** to BLOCK live sync until a specifically verified NEW stand-alone Roblox place is created and owner-approved. NEVER bypass and NEVER sync original Dreadfall or Feudfall Roblox place.
- Recovery needs exact Git SHA + correct scene save/version + private independent .rbxlx backup/checksum and Studio close/reopen test. Studio 1/2/4 clients and real mobile tests required.
- Robux products and launch promotions NOT authorised. LivePurchasesEnabled is false. Repo was PUBLIC at 17 Nov audit, so don't copy private original assets before rights/visibility review.

**Archived material:** docs/00–21 and 23–25 describe SIGNAL LOST/Relay Nine/Echo and outdated Codex scheduling. They are historical, not instructions; generic original asset provenance practices in docs/13–16 remain applicable if consistent with the active documents.
