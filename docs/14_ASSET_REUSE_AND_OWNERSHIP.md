# 14 — Approved cross-project asset reuse & exclusive development (owner decision 15 Nov 2026)

## Authority
The owner explicitly authorizes Claude Opus to reuse **any suitable assets from the owner's original Dreadfall and Feudfall projects** in this **standalone horror game**, subject to rights, technical compatibility and safe handling. This is permission to COPY into BigKilla75/dreadfall-story-horror, **not** to modify the original projects. Original Dreadfall is postponed because of complications; it is not cancelled or a donor repository to dismantle.

Source references (owner-associated, inspect and confirm):
- Original Dreadfall: BigKilla75/roblox-game
- Feudfall: BigKilla75/revengers
- Destination only: BigKilla75/dreadfall-story-horror

## Strict read-only source boundary
- Source repositories, Roblox Studio places, published experiences, Git history, branches and asset ownership remain unchanged.
- Claude may READ source files, inspect assets and create local copies in a separate scratch directory, then import adapted copies into this horror repository/place.
- Never push, commit, merge, delete, rename, reconfigure, publish, synchronize Rojo to, or move files out of either source project.
- Do not reuse shared live Roblox assets by editing the originals in place; create independent copies where rights/Roblox asset access permit. No shared source-linked dependencies that could break the originals.
- No use of source credentials, DataStores, player data, economy, gamepasses, purchase IDs, badges, analytics identifiers or original place/universe IDs in the horror project.
- No cross-pollination of canonical story/lore unless the owner separately approves. Visual/code reuse is not an automatic narrative merger.

## Candidate asset categories to audit
- Architecture: walls, modular rooms, doors, corridors, industrial props, terrain dressing, environmental decals.
- Atmosphere: approved original sound, ambient loops, particles, lighting rigs, fog, post-processing presets, visual effects.
- Interaction: inspected door, prompt, puzzle, UI and audio utilities; adapt only if isolated from old project services and server-authoritative.
- Animation: rights-cleared rig animations and non-player effects; verify rig, asset IDs and permission in new universe.
- Character models: only when appropriate to sci-fi horror, licensed and compatible with Roblox policies and target performance.
- Tools/scripts: inspect source and security; never bulk-import old game services, weapon systems, combat, PvP, admin commands, marketplace code, analytics or unknown third-party plugins.

## Rights and safety gate (required for EACH reused asset)
1. Record source project, path/model name, source commit or Studio export identifier and original author/owner if known.
2. Determine whether asset is user-created, properly licensed for reuse in a separate Roblox experience, or third-party restricted. **Do not import** when rights are uncertain; list as BLOCKED and ask owner for evidence/permission.
3. Verify any asset ID is usable in the destination experience and isn't dependent on source universe permissions. If necessary, owner creates an independent asset upload with appropriate rights.
4. Inspect all embedded scripts, ModuleScripts, packages and external dependencies; strip untrusted executable scripts, require safe network boundaries and avoid leaking source project services.
5. Copy to a new path in destination; adapt and test copies only. Prefer small curated imports over bulk migration.
6. Verify memory/render/network cost, mobile compatibility, art direction and absence of unwanted functionality.
7. Log asset provenance and status in docs/15_ASSET_INVENTORY.md, with links to new destination path and any license note.
8. Mark asset IMPORTED only after verifying actual new-place use; mark TESTED only after Studio evidence.

## Preferred reuse strategy
- **First:** inspect existing assets for high-value corridor modules, doors, lighting, radio props, audio and UI that directly accelerate the six-zone horror slice.
- **Second:** prioritize geometry, atmosphere and safe utilities; rebuild or isolate networking and session progression specifically for this new game.
- **Third:** build only missing pieces. Do not import a giant unrelated FPS/PvPvE framework to save a few hours of scripting.
- Asset copying should be done in a new working directory with explicit destination filenames and separate Roblox place IDs. Preserve a pre-import Studio backup.

## Exclusive agent policy
**Claude Opus / Claude Code is the ONLY authorized development agent for this game.** Codex is removed from development, review, implementation and agent handoffs. ChatGPT can coordinate or edit planning docs on explicit owner request; GitHub Actions automated lint/build/test remains allowed. Claude performs its own reviews and uses deterministic automated tests and human playtests for validation.

## Evidence and reporting
Before coding: produce a READ-ONLY inventory of candidate assets and exact source evidence, without modifying source projects. Then copy small verified batches to destination. For each batch report original path/ref, destination, rights/compatibility result, test result and any unresolved license/Roblox ID blocker. No claim that assets are imported merely because the owner approved reuse.

## Blender-original alternative
The owner also approves new, original Blender assets authored by Claude Opus for this game. Use Blender when no suitable rights-cleared asset exists or a signature horror design needs its own look. New assets are not source-project copies; track them separately using docs/16_BLENDER_ASSET_PIPELINE.md. Never modify Dreadfall/Feudfall originals.
