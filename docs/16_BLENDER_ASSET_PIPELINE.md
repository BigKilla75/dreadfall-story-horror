> **17 NOV 2026 — OPERATION BLACK SKY:** Technical safety, source-preservation and rights-checking instructions remain relevant where consistent with the [current Black Sky master plan](27_OPERATION_BLACK_SKY_MASTER_PLAN.md). SIGNAL LOST-specific environment, story, old assets and Codex workflows below are HISTORICAL; no asset listed is automatically approved/imported into this game. See [Claude's active prompt](34_CLAUDE_BLACK_SKY_MASTER_PROMPT.md).

# 16 — Blender original asset pipeline (approved 15 Nov 2026)

## Policy
Claude Opus is the sole development agent and may create new, original 3D meshes, rigs, props, modular kits and animations using Blender for this standalone horror game. The preferred strategy is a mix of rights-cleared one-way copies from Dreadfall/Feudfall and purpose-built Blender originals. Neither original game may be changed. Blender must be available on the actual Windows host or another authorized workstation; no claim of installation, automation or successful export is implied.

## Priority order
1. Modular sci-fi horror kit: corridor/wall/floor/ceiling pieces, corners, door frames, vents, cables, pipe clusters and control room shells.
2. Gameplay props: radio transmitter, signal tuner, fuse/power box, generators, doors, switches, warning displays and objective evidence.
3. Signature antagonist: original silhouette, simple Roblox-compatible rig and a small tested animation set. Avoid time-consuming high-poly sculpting before the playable vertical slice.
4. Atmosphere: debris, broken machinery, monitors, signage, unique set dressing. Prefer decals/lighting to excessive geometry.
5. Optional cosmetics only after alpha gameplay and performance are verified.

## Reproducible workflow
- Audit reusable assets first; log whether each new mesh is REUSED, ADAPTED COPY or ORIGINAL.
- Build Blender source in a dedicated destination-only directory such as `assets/blender/source/`; exports under `assets/blender/exports/`. Do not overwrite existing files. Prefer meaningful names, consistent scales, pivots/origins and modular dimensions.
- Use Blender collections for zones and export units consistently. Apply transforms and check normals, UVs and materials. Keep collision meshes simple; use Roblox Studio collision settings deliberately.
- Export suitable meshes as FBX or glTF as supported by the currently installed Roblox Studio importer. For rigs/animations, verify bone structure and import results on the actual target place. Roblox materials/lighting may need Studio recreation; do not assume Blender shader graphs transfer.
- Avoid embedded executable scripts, unknown downloaded textures, copyright-restricted models, and direct links to original Dreadfall/Feudfall Roblox asset IDs without permission in the new universe.
- Import into the NEW standalone Roblox Studio place only, inspect materials, scale, collision, network replication and streaming. Preserve pre-import Studio backup. Use MeshParts/Models in a consistent asset namespace; Rojo scripts must remain separate.
- Optimize for PC and mobile: low/medium geometry, texture budgets, mesh reuse, bounded draw calls, LOD where warranted, simple collision. Measure Studio performance instead of inventing polygon budgets.
- Record source .blend file, exported asset, target Studio model/asset ID, author, dependencies, license, optimization observations, and Studio evidence in a Blender-specific asset ledger before marking TESTED.
- Never commit sensitive files or licensed third-party textures without redistribution permission. Consider Git LFS for large .blend/.fbx binaries only after verifying repository storage limits and owner approval.
- Do not block first two-player vertical slice on art polish. Greybox first, then swap in modular Blender meshes incrementally.

## Completion gate
An asset is only COMPLETE when the original Blender file is retained, export is validated, import is verified in the correct new Roblox place, gameplay collision/scale/materials work, and at least one performance check is recorded. Automated source CI does not prove any of this.

## Asset ledger (Claude to populate)
| Name | Category | Source (.blend or approved reuse) | Export | Roblox destination | Rights | Import/test evidence | Status |
|---|---|---|---|---|---|---|---|
| Not yet audited | — | — | — | — | — | — | NOT STARTED |
