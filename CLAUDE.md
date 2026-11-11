# Instructions for Claude Code / Opus — this repository ONLY

## Mission
Deliver a polished, playable **private alpha** of a 1–4-player, 25–35-minute cooperative Roblox sci-fi story-horror game, within an owner-targeted seven-day sprint starting 11 Nov 2026. The first game experience is provisionally called SIGNAL LOST. Preserve design flexibility and be honest about progress. This is a new project, NOT the pre-existing PvPvE Dreadfall.

## Hard guardrails
- Work only in BigKilla75/dreadfall-story-horror. **Never change** BigKilla75/roblox-game, BigKilla75/revengers or any Academy project.
- Never assume a system works, an asset exists, a Roblox Studio test passed, or the place was published unless evidence exists. Mark unknowns UNKNOWN.
- Do not copy other Roblox games' maps, scripts, names, sounds or paid assets without rights and approval. No use of unverified Toolbox free models with scripts.
- Protect credentials and Roblox authentication; do not commit secrets, cookies, tokens or real-world personal data.
- Do not silently change story canon, monetization, scope, privacy or account settings. Create a proposal/issue when outside scope.
- Owner approval required for public release, game pass/developer product creation, prices, spending Robux, ads, off-platform accounts, and significant asset imports.
- Respect Roblox policies and protect minors; avoid paid random rewards and pay-to-win mechanics.
- If an external dependency, plugin or API is unavailable, report the blocker and implement a safe fallback. No fictional screenshots, metrics, live links or test results.

## Start-of-work routine
1. Read README.md and all docs under docs/, especially 00, 05, 06, 07, 10, 11.
2. Check git status, branch, newest commits and open issues/PRs. Verify repository identity and owner. Confirm that existing changes are not overwritten.
3. Write a brief plan and identify touched paths. Choose the earliest unfinished P0 issue. Prefer 1–3 focused commits per issue.
4. Create a feature branch, e.g. feature/p0-session-state. Include tests or clear manual reproduction criteria.
5. Run whatever tooling is ACTUALLY installed. Record exact commands and results; do not claim Roblox Studio playtests were run if they were not.
6. Open a PR with summary, changed files, risks, screenshots/video if captured, test matrix and any required human Studio action.
7. Mark issue done only against acceptance criteria after owner or reviewer verification.

## Authority / design precedence
Owner's latest explicit instructions > this repo's current approved decisions > docs/00_VISION_SCOPE.md and docs/06_ROADMAP_7_DAYS.md > issue-specific acceptance criteria > this document. Proposed features are not automatically approved or implemented. If files conflict, surface the conflict rather than choosing silently.

## Build philosophy
- Keep one small interconnected facility with modular rooms and lighting variants. Prioritize pacing, clarity and sound over polygon count.
- One threat, heavily directed encounters, forgiving resets, deterministic server-side state. No big procedural world, no combat or expensive open-world AI in alpha.
- Make solo possible: all cooperative mechanics have sequential solo paths; more players enable parallel solutions, not mandatory player-count locks.
- Co-op is a real feature: all players share stage state and key events, interactions synchronize, late arrivals and disconnects do not softlock.
- Avoid blocking cutscenes longer than needed; allow subtitles, camera accessibility, volume controls, photosensitivity options and mobile interaction UI.
- Use original licensed audio and visual assets, no actual personal player voice capture.

## Source ownership between agents
Claude owns runtime module integration: SessionService, ObjectiveService, InteractionService, ThreatDirector, NarrativeDirector and Studio implementation. Codex independently reviews security, tests, code clarity, data definitions, receipts and performance; Codex may implement one clearly assigned module at a time on separate PRs. Do not both edit a shared file concurrently. Use GitHub issues as the handoff ledger.

## Prioritized work
P0: Studio place binding, co-op state machine, stage progression, object interactions, map greybox, two puzzles, one scripted threat, ending, 1/2/4 player tests, PC/mobile checks.
P1: Sound design, 2–3 pretested variants, evidence journal, settings, badges.
P2: Paid cosmetics / catalog / creator products after receipt and eligibility audit, account owners create IDs.
P3: Additional endings, complex AI, persistence beyond basics, public matchmaking and live ops.

## Stop conditions
If the 30-minute target cannot meet reliability, cut encounter count and decorative rooms first; do not fake length with idle timers. If true 4-player progression is broken, do not release a co-op alpha. If purchases cannot be verified end-to-end, disable purchases entirely. Any zero-day critical issue blocks public release.

## Required status report, once each work session
- Verified present (commit SHA, branch, files, tested environment)
- Done (PR/commit references)
- Testing evidence (commands / observed Studio sessions; distinguish automated vs manual)
- Broken/unknown
- Next smallest issue with owner action, if any

Do not say 'fully automated' merely because code was produced. Blender/Studio modelling, publishing, physical device testing and marketing still need a connected execution environment and/or the owner.

## Stable environment requirement (11 Nov 2026)
Before editing or syncing, read docs/13_STUDIO_ENVIRONMENT.md. Rojo 7.7.1 is pinned via rokit.toml. Always run python scripts/dev.py doctor and the unittest suite, then python scripts/dev.py build. Live sync ONLY using python scripts/dev.py serve --place-id APPROVED_NEW_PLACE_ID after the owner verifies the new standalone Roblox place and adds its numeric place ID to servePlaceIds. Do not bypass the empty initial allowlist, run raw Rojo serve/upload, auto-publish or use original Roblox places. A successful GitHub Action build does not count as a Roblox Studio playtest.

## Existing Windows toolchain (owner-reported)
Owner reports Windows + Rojo + Selene installed. Do not waste sprint time reinstalling. Read docs/13_STUDIO_ENVIRONMENT.md and run `rojo --version`, `selene --version`, `selene src`, Python unit tests and safe build locally. Exact pinned versions are in rokit.toml; if mismatch, report rather than blindly changing the machine. Start P0-01 after verifying correct NEW Roblox place. Report actual Studio tests separately from lint/CLI builds.
