# Dreadfall Story Horror — standalone Roblox project

**Working in-game title:** SIGNAL LOST (not final branding or canonical Dreadfall lore).
**Repository:** BigKilla75/dreadfall-story-horror.
**Status (11 Nov 2026):** PREPRODUCTION SPECIFICATION + MINIMAL CODE SCAFFOLD. No gameplay, map, assets, automated tests or Roblox publish verified yet.

This is a wholly separate experience/repository from the original Roblox PvPvE Dreadfall (BigKilla75/roblox-game), Feudfall (BigKilla75/revengers), and Academy. Do not edit or import anything from them without a deliberate, rights-checked plan and approval. The first seven-day target is a **private playable alpha**, not a commercial release.

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

AI-agent instructions: [CLAUDE.md](CLAUDE.md) for Claude Code and [AGENTS.md](AGENTS.md) for Codex.

## First milestone: private alpha
Accept only if 1, 2, and 4 players can complete all three acts in a playable Roblox place without softlocks; everyone can interact, recover after death/disconnect as specified; there is a complete ending; and PC + at least one real mobile playtest have passed. No claim of success from code generation alone.

## Source and tooling
Rojo v7 project definition: default.project.json. Shared configuration: src/shared/Config.luau. Client/server scripts are **placeholder bootstraps**, not a game. Open the separate Roblox Studio place, connect Rojo only after confirming place/universe identity, construct the 3D scene in Studio, and test manually. Do not publish or monetise without the owner's approval. Never commit API keys, sessions, cookies or purchased third-party assets without licenses.

## Autonomous workflow
Owner maintains access/approves publishing and Robux products. Claude Opus leads gameplay implementation. Codex handles narrowly scoped reviews, validation, tests and isolated modules on separate branches. ChatGPT coordinates plan, review and GitHub issue acceptance. See CLAUDE.md and AGENTS.md for duties and reporting.

**Repo visibility:** was PUBLIC when checked on 11 Nov 2026. Owner should choose Private in GitHub settings if source/story should stay confidential. The connected GitHub integration cannot change repository visibility.
