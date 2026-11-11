# 13 — Reproducible Roblox Studio + agent development environment

Status: Repository configuration committed; **not** proof that Roblox Studio is installed, a Roblox universe exists, Rojo has synced, CI passed, or Claude is running. Last design review: 11 Nov 2026.

## Requirements / what the cloud cannot do
- **Roblox Studio requires Windows or macOS**, not Android/Linux. A real Windows/Mac host or remote desktop to one is mandatory for GUI building, full gameplay and device tests.
- Official recommendation: 8 GB RAM and Windows 11/macOS 14+; for 4-client local testing a faster machine and 16 GB+ RAM are sensible planning targets, not official minimums.
- GitHub Codespaces/devcontainers (Linux) are for editing Luau and running Rojo CLI builds; **they cannot run Roblox Studio GUI**. Codespaces may incur billing; do not launch paid resources without owner consent.
- GitHub Action validation is isolated and DOES NOT log into Roblox, publish a universe or prove playability.

## Reproducible toolchain
- Git + VS Code (recommended)
- Roblox Studio: official Windows/Mac installer at https://create.roblox.com/docs/studio/setup
- Python 3.10+ for scripts/dev.py and built-in unittest
- Rokit https://github.com/rojo-rbx/rokit (install per OS; review the install instructions)
- Rojo **7.7.1 pinned** in rokit.toml (server/CLI) + matching major-version Studio plugin
- Optional Rojo VS Code extension and Luau language server (suggested by .vscode/extensions.json)
- No reliance on unexplained third-party Toolbox models, auto-publish plugins, secrets, external services or unreviewed git hooks.

## One-time Windows or Mac setup
1. Install Roblox Studio from the official site, log in to the Roblox owner account, and install Git + VS Code + Python.
2. Clone ONLY https://github.com/BigKilla75/dreadfall-story-horror and open that folder in VS Code. Confirm the Git remote is correct: git remote -v.
3. Install Rokit per official directions, open a new terminal in the repository and run:
   rokit install
   rojo --version
   rojo plugin install
   python scripts/dev.py doctor
4. Rojo should report **7.7.1**. The doctor should report LIVE SYNC LOCKED; this is intentional until the game's dedicated Roblox place exists.
5. In Roblox Studio create a NEW separate experience/place and back it up as an .rbxl or .rbxlx file in a **private owner-controlled location**, not in the repo. Never open/sync the existing PvPvE Dreadfall/Feudfall places.
6. Find the NEW place ID in the Roblox Creator Dashboard and verify its identity twice. Have the owner approve it.
7. Edit default.project.json to set:
   "servePlaceIds": [NEW_PLACE_ID]
   (Use a numeric ID without quotes; commit/review this change. **Do not** add place IDs from other games.)
8. Run:
   python scripts/dev.py serve --place-id NEW_PLACE_ID
9. In the correct Studio place open the Rojo plugin, connect to localhost:34872. Inspect pending changes before sync. Verify paths:
   ReplicatedStorage/Shared/Config
   ServerScriptService/GameServer/Bootstrap
   StarterPlayer/StarterPlayerScripts/GameClient/Bootstrap
10. Save a fresh Studio backup after reviewing the correct sync. Do not enable any automatic publish action.

## Daily routine for Claude / Codex
- git pull --ff-only on the owned branch and inspect git status; if uncommitted work exists, don't overwrite it.
- python -m unittest discover -s tests -v
- python scripts/dev.py doctor
- python scripts/dev.py build
- For local Studio live editing: python scripts/dev.py serve --place-id APPROVED_PLACE_ID (ONLY after explicit ID lock above).
- Test with Studio Server & Clients at 1, 2, and 4 clients, then mobile device/emulator, after implementing gameplay.
- Push feature branch -> PR -> CI -> Codex or independent reviewer -> merge if verified -> Studio place backup before major sync.
- Never use a direct unsafeguarded 'rojo serve' or any 'rojo upload' command as part of automated agent scripts.

## Studio multi-client validation
Test tab -> play mode dropdown -> Server & Clients -> 1 / 2 / 4 clients -> Play/F7. Validate replication, puzzle idempotency, death, late join, disconnect, restart, and performance. Studio can simulate more clients, but these three counts cover the target. Compare with controlled published multiplayer before release; Studio simulation alone is insufficient.

## CI
.github/workflows/validate.yml runs configuration tests and a pinned Rojo XML place build. It never publishes; it has contents:read permission and no tokens/cookies or write-to-Roblox steps. A green workflow means source and build checks passed, NOT that gameplay or Studio tests passed. Confirm the actual workflow result in GitHub Actions; a workflow file commit is not proof that a job ran.

## Troubleshooting
- 'Rojo missing': install Rokit, run rokit install from repo, reopen terminal, check PATH.
- 'Wrong Rojo version': pin must be v7.7.1; don't use system/global newer Rojo for this sprint.
- 'Live sync LOCKED': create/verify new Roblox place and explicitly set servePlaceIds allowlist.
- 'Place ID mismatch': stop and check original project hasn't been opened. NEVER bypass lock.
- 'No Studio plugin': rojo plugin install; restart Studio; inspect Plugins.
- 'Changes invisible': verify correct Rojo project, connected localhost:34872, existing scene backup, Explorer paths and Studio Output; do not run blind replace.
- 'Codespaces launches but no Studio': expected; connect a Windows/Mac Studio host for actual game tests.
- 'Environment doctor passes but game empty': expected; gameplay code and 3D art are not implemented yet.

## Links
https://create.roblox.com/docs/studio/setup
https://create.roblox.com/docs/studio/testing-modes
https://create.roblox.com/docs/projects/external-tools
https://rojo.space/docs/v7/getting-started/installation/
https://rojo.space/docs/v7/project-format/
https://github.com/rojo-rbx/rojo/releases/tag/v7.7.1
https://github.com/rojo-rbx/rokit

## Existing Windows workstation verified by owner report (11 Nov 2026)
The owner reports a Windows PC with Roblox Studio, Rojo and Selene already installed. **This is owner-reported, not remotely verified.** Do not reinstall programs blindly. First run from a local PowerShell terminal in the new repo:
```powershell
git remote -v
git pull --ff-only
rojo --version
selene --version
python -m unittest discover -s tests -v
selene src
python scripts/dev.py doctor
python scripts/dev.py build
```
Expected pinned versions: Rojo 7.7.1 and Selene 0.32.0. Selene's Roblox standard library is selected by `selene.toml` (`std = "roblox"`). If the already installed versions differ, check before changing the PC tooling; the repo's `rokit.toml` documents supported versions. The Rojo live-sync lock remains active until a NEW, approved experience place ID is configured. Never sync into the original Dreadfall or Feudfall places.

Claude: immediately request/verify the local repo checkout, the separate Studio place and tool output; then focus on P0-01 (two-client synchronized interaction), not environment reinstall. Codex: run `selene src` on each isolated PR, report lints, review remotes and test paths. Selene lint alone does not establish runtime success.
