# CLAUDE.md — ONE game, ONE development agent, recoverable Studio project

**AUTHORITATIVE OWNER DECISION 15 NOVEMBER 2026:** This standalone horror game is now built by **Claude Opus/Claude Code ONLY**. Codex is NOT involved. No AI rotations, secondary coding agents or dual-agent handoffs. This overrides every earlier Claude/Codex plan and GitHub issue discussion.

## FIRST: read and follow the full master prompt
[docs/25_CLAUDE_MASTER_PROMPT.md](docs/25_CLAUDE_MASTER_PROMPT.md) contains the **copy/paste execution mandate**. [docs/26_CLAUDE_SOLO_OPERATIONS.md](docs/26_CLAUDE_SOLO_OPERATIONS.md) is the actual safe development procedure. [docs/22_CURRENT_STATE.md](docs/22_CURRENT_STATE.md) is a verified/unknown handoff ledger for sequential Claude sessions, not separate agents.

## Mission
Ship a reliable, complete 1–4-player ~25–35-minute private-alpha story-horror chapter (working title SIGNAL LOST) with one actual canonical Roblox Studio experience, synchronized multiplayer, a full beginning/ending, honest tests, Blender-original assets where worthwhile, and safe save/restore. The 14-active-workday target is a planning hypothesis and must be re-estimated after the first 3 days of actual measured progress. Planning documentation is NOT proof that a playable game exists.

## Non-negotiable
- Work only in `BigKilla75/dreadfall-story-horror`. Original Dreadfall `BigKilla75/roblox-game` is **POSTPONED**, not abandoned; Feudfall `BigKilla75/revengers` also remains unchanged; Academy stays separate. You can inspect/copy rights-cleared assets from the two originals ONE-WAY only, with ownership and compatibility evidence; never edit original repos or Studio places. Check source repo privacy versus public destination before import.
- Do not install/reconfigure the owner's existing Windows/Rojo/Selene environment blindly; verify what's already present. Blender creation is allowed, with actual import/rights/performance checks.
- Exactly ONE new horror Roblox experience/place, one controlled Rojo integration mapping, one primary development path. `servePlaceIds` empty means live sync intentionally LOCKED pending owner-verified new place ID; do not bypass lock. No standalone rival builds.
- Preserve source, Studio scene and original .blend files. A Git commit does not save Studio-built geometry. Commit source, save Studio with version notes, keep a private .rbxl/.rbxlx backup, and prove reopening/restoration before declaring a gameplay milestone.
- Every real gameplay integration requires appropriate source tests plus an actual 1/2-client canonical Studio smoke; test 4 clients on co-op changes and real devices before release. Differentiate VERIFIED, SOURCE-BUILT, STUDIO-TESTED, UNKNOWN, BLOCKED.
- Server owns objectives and rewards; validate client inputs, distances, state, rates, duplicates and join/death/disconnect/replay. No untested scripts from Toolbox.
- No public publish, real Robux purchases, pass/product ID creation/prices, paid ads, private account changes, fees or unattended controller activation without explicit owner permission.
- No independent AI collaborators. Claude performs its own code review and uses deterministic CI and human playtest evidence.
- No fictional studio access, completed Blender model, game progress, CI or model version.
- For daily handoffs/resumption update docs/22 with exact Git SHA, matching Studio save and backup, test logs, blockers and next task.
- Read relevant full game bible [docs/17](docs/17_SIGNAL_LOST_GAME_BIBLE.md), first three days [docs/18](docs/18_FIRST_72_HOURS.md), business [docs/20](docs/20_MONETIZATION_MARKETING_LAUNCH.md), remaining days [docs/24](docs/24_DAYS_4_TO_14.md). Older docs/19/21/23 are **HISTORICAL ONLY**, superseded.

## Immediate work order
1. Verify exact branch/remote, current worktree and Roblox Studio place; identify last known-good source+scene tuple. Protect all existing uncommitted data.
2. Prove scene save/close/reopen + backup and correct Rojo target on NEW horror place.
3. Implement a minimal authoritative objective, two-client synchronization, one short gameplay route and stub ending in the SAME Studio game.
4. Continue through issues by player-facing value and actual verification. Reforecast after day three. No extra planning loops when engineering can proceed safely.

Read docs/25 and EXECUTE the earliest unblocked task now. If Studio is inaccessible, say so and do safe source work without claiming Studio playability.
