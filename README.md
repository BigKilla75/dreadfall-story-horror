# Dreadfall Story Horror — standalone Roblox project

**Working in-game title:** SIGNAL LOST (not final branding or canonical Dreadfall lore).
**Repository:** BigKilla75/dreadfall-story-horror.
**Status (11 Nov 2026):** PREPRODUCTION SPECIFICATION + MINIMAL CODE SCAFFOLD. No gameplay, map, assets, automated tests or Roblox publish verified yet.

This is a wholly separate experience/repository from the original Roblox PvPvE Dreadfall (BigKilla75/roblox-game), Feudfall (BigKilla75/revengers), and Academy. Original Dreadfall development is **postponed due to complications**, not cancelled. Owner now explicitly permits **one-way copying of suitable, rights-cleared assets from original Dreadfall and Feudfall into this standalone horror game**; originals remain untouched. Follow [asset reuse policy](docs/14_ASSET_REUSE_AND_OWNERSHIP.md). The first seven-day target is a **private playable alpha**, not a commercial release.

## Product promise
A 1–4-player cooperative sci-fi story horror experience in an abandoned signal station. A first run targets approximately 25–35 minutes, with replay through free evidence collection and small, testable scenario variations. No pay-to-win. Build tension with light, sound and misdirection, not prolonged waiting or spammed jumpscares.

## Documents (read in this order)
1. [Vision and release scope](docs/00_VISION_SCOPE.md)
2. [Story, level and pacing](docs/01_STORY_LEVEL.md)
3. [Gameplay and co-op rules](docs/02_GAMEPLAY_SYSTEMS.md)
4. [Replayability and progression](docs/03_REPLAYABILITY.md)
5. [Monetization and compliance](docs/04_MONETIZATION.md)
6. [Technical architecture](docs/05_TECH_ARCHITECTURE.md)
7. [Seven-day production plan](docs/06_ROADMAP_7_DAYS.md)
8. [QA, security and release gates](docs/07_QA_RELEASE.md)
9. [Analytics, launch and marketing](docs/08_KPI_GROWTH.md)
10. [Risks and decisions](docs/09_RISKS_DECISIONS.md)
11. [Owner setup and blockers](docs/10_OWNER_ACTIONS.md)
12. [Work breakdown](docs/11_BACKLOG.md)
13. [References](docs/12_REFERENCES.md)

Agent instructions: [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md) both enforce the current Claude-only directive. New 15 Nov sequential-turn instructions supersede historical Claude-only language.

## First milestone: private alpha
Accept only if 1, 2, and 4 players can complete all three acts in a playable Roblox place without softlocks; everyone can interact, recover after death/disconnect as specified; there is a complete ending; and PC + at least one real mobile playtest have passed. No claim of success from code generation alone.

## Source and tooling
Rojo v7 project definition: default.project.json. Shared configuration: src/shared/Config.luau. Client/server scripts are **placeholder bootstraps**, not a game. Open the separate Roblox Studio place, connect Rojo only after confirming place/universe identity, construct the 3D scene in Studio, and test manually. Do not publish or monetise without the owner's approval. Never commit API keys, sessions, cookies or purchased third-party assets without licenses.

## CURRENT DEVELOPMENT DIRECTIVE — CLAUDE ONLY (15 November 2026)

**Claude Opus / Claude Code is now the sole development agent. Codex has been removed at the owner's request.** This supersedes all previously proposed Claude/Codex shifts, handoffs, separate worktrees and controller dispatch. The original dual-agent planning files are preserved as history, not active instructions.

**Start here:** [Claude master prompt](docs/25_CLAUDE_MASTER_PROMPT.md) → [Single-agent operations and recovery](docs/26_CLAUDE_SOLO_OPERATIONS.md) → [Current state](docs/22_CURRENT_STATE.md).

The one-game invariant remains: ONE new Roblox universe/place, ONE approved Rojo integration target, source in Git plus independently verified Studio scene saves/backups, 1/2/4-player smoke and regression tests. The original Dreadfall and Feudfall repositories are READ-ONLY asset/research candidates, not alternate games.

- [Comprehensive game bible](docs/17_SIGNAL_LOST_GAME_BIBLE.md)
- [First three active development days](docs/18_FIRST_72_HOURS.md) — old multi-agent rows superseded
- [14-day private-alpha production path](docs/24_DAYS_4_TO_14.md) — Claude owns all tasks
- [Monetization, marketing and launch](docs/20_MONETIZATION_MARKETING_LAUNCH.md)
- [Technical challenges for Claude](docs/25_CLAUDE_MASTER_PROMPT.md#11-claudes-own-high-reasoning-challenge-questions)

**Repo visibility:** was PUBLIC when checked on 15 Nov 2026. Owner should choose Private in GitHub settings if source/story should stay confidential. The connected GitHub integration cannot change repository visibility.

## Stable Studio/toolchain environment (added 11 Nov 2026)
See [docs/13_STUDIO_ENVIRONMENT.md](docs/13_STUDIO_ENVIRONMENT.md) for Windows/Mac Studio setup, pinned Rojo, safety guard, test strategy and optional cloud source-development container.

- rokit.toml pins Rojo 7.7.1; scripts/dev.py doctor|build|serve is the ONLY intended command entrypoint for agents.
- default.project.json deliberately has "servePlaceIds": []: live sync is BLOCKED until the owner creates and verifies a new, standalone Roblox place and approves its numeric place ID. Do not bypass it.
- .github/workflows/validate.yml builds source-only XML and runs configuration tests; it does not publish a place.
- .devcontainer is optional VS Code/Codespaces editing/CLI environment; it cannot run the Studio GUI.
- Start with P0-01 and confirm CI/Studio evidence before treating environment as operational.

**Windows workstation update:** owner reports Roblox Studio, Rojo and Selene already installed. Selene is now pinned/configured and checked in CI. Use the local verification commands in docs/13_STUDIO_ENVIRONMENT.md; actual Studio operation remains unverified until agent runs on the Windows PC.

## Current project direction — 15 November 2026
Original Dreadfall is **on hold because of complications**; its source, assets, place and existing work must be preserved. The standalone horror game is the active focus. Claude Opus is the **only authorized coding/development agent**. Reuse suitable rights-cleared Dreadfall/Feudfall assets via one-way copies with provenance, compatibility checks and independent Studio tests. The seven-day plan is a target requiring a fresh baseline, not a claim of elapsed-day progress.

## Original Blender assets
Claude Opus may create new custom 3D assets in Blender as well as reuse rights-cleared source-project assets. See [Blender asset pipeline](docs/16_BLENDER_ASSET_PIPELINE.md). New assets must be independently stored, optimized and tested in the standalone Roblox place. No Blender meshes have been created or imported by this documentation change.
