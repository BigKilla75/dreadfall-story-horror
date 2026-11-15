# 15 — Reused asset provenance ledger

**Status:** EMPTY / NOT YET AUDITED. Owner permits suitable rights-cleared Dreadfall and Feudfall asset reuse, but no asset is verified or imported by this document.

| Source project | Original path / Studio model | Source commit / export | Ownership / reuse rights | Destination path | Dependencies / IDs | Status | Studio test evidence |
|---|---|---|---|---|---|---|---|
| (Claude to audit) | — | — | UNKNOWN | — | — | NOT INSPECTED | — |

Status vocabulary: CANDIDATE, RIGHTS-CLEARED, BLOCKED, COPIED, IMPORTED, TESTED. Do not advance a status without evidence.

Source repos must remain read-only. See docs/14_ASSET_REUSE_AND_OWNERSHIP.md.

## Read-only candidates identified by repository inspection, 15 Nov 2026
This is a path-level audit ONLY. No asset copied/imported or Studio playback verified. Even documented CC0 must be verified against original licence and Roblox permissions before use.

| Project | Verified candidate source | Potential role | Rights/technical check | Current status |
|---|---|---|---|---|
| Feudfall | Assets/Audio/Ambience/archive_hum.ogg | Relay Nine archive atmosphere | Source identity in Feudfall manifest; cross-game audio upload or permission | CANDIDATE, NOT IMPORTED |
| Feudfall | Assets/Audio/Match/broadcast_open.ogg; broadcast_urgent.ogg | Station automated radio stingers | Confirm asset origin and CC0 provenance from manifest; Roblox audio permission | CANDIDATE, NOT IMPORTED |
| Feudfall | Assets/Audio/UI/click.ogg; confirm.ogg | Puzzle UI feedback | Confirm Kenney pack entry/CC0 licence and intended audio use | CANDIDATE, NOT IMPORTED |
| Feudfall | Assets/Audio/Abilities/fuse.ogg; sonar.ogg | Relay/power signal effects | Check exact manifest source/licence, sound mix and reuse rights | CANDIDATE, NOT IMPORTED |
| Feudfall | src/maps/NinthArchive.rbxmx | Geometry / archival set pieces | Scan for embedded scripts, review all textures/asset IDs, safe mesh/part import | CANDIDATE, NOT IMPORTED |
| Feudfall | src/maps/AshfallRelay.rbxmx; BrassLantern.rbxmx | Modular environment candidates | Only extract compatible generic pieces; avoid importing full FPS maps | CANDIDATE, NOT IMPORTED |
| Dreadfall | src/server/MapBuilder.luau | Facility construction approach / dimensions / industrial palette | Read-only study; do NOT import entire gameplay services; no copying without isolating dependencies | CANDIDATE, NOT IMPORTED |
| Dreadfall | docs/art/LIGHTING.md | Shadow/lighting tradeoff research | Verify new Studio version and real phone performance; historical settings not current guarantees | RESEARCH ONLY |
| Dreadfall | tools/studio-smoke/ and tools/session-smoke/ | Test-harness design reference | Read-only study; do NOT run controller or duplicate place IDs; create destination-only adapted tools | RESEARCH ONLY |

Feudfall verified catalog paths: Assets/CATALOG.md, Assets/manifest.json, Assets/Licences/Kenney_Sci-Fi-Sounds_CC0.txt, Assets/Licences/Kenney_Interface-Sounds_CC0.txt. Source projects are PRIVATE, while standalone horror repo is currently PUBLIC: never include proprietary source code, media or licensed files in the public destination until rights AND intended visibility are reviewed.
