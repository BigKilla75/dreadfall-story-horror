# 22 — CURRENT_STATE / single-game handoff ledger
Recorded 15 Nov 2026 by ChatGPT from connected GitHub. Update after EACH safely completed agent turn. This file is current planning snapshot, not proof of Windows/local Studio state.

## Verified GitHub state at plan creation
- Repository: BigKilla75/dreadfall-story-horror (PUBLIC when checked 15 Nov 2026), default main.
- Original Dreadfall: BigKilla75/roblox-game PRIVATE / postponed; Feudfall BigKilla75/revengers PRIVATE / asset reuse read-only.
- At this snapshot, original 13 horror issues were OPEN; no gameplay or map implementation was verified in the horror repository beyond placeholder bootstraps.
- Repo contains pinned Rojo/Selene and a source-only CI workflow; earlier run 43078139200 passed on commit 6af5a9e. That does NOT prove Studio tests.
- A NEW dedicated Roblox place/universe ID, real local Studio synchronization, physical mobile tests, Blender imports, multiplayer playthrough and an active Windows-side alternating controller remain UNKNOWN/UNVERIFIED.
- Documentation is updated by subsequent plan commits; always verify exact main SHA live before task dispatch, never copy a stale hash as expected head.

## Owner-approved policy
ONE MAIN Roblox Studio place and one GitHub repo. Preserved original source projects. One-way rights-cleared reusable assets; new original Blender assets. STRICT sequential model turns; Claude sole Studio integration owner; Codex bounded code/review turn ONLY after clean handoff. Studio recoverability and playability before polish. No purchases, paid ads or public launch without approval.

## Planned first active issue
GitHub issue #1: approve and verify dedicated place, Rojo allowlist, Studio scene save/reopen and source restore. Then #2 minimal co-op state, #4 interaction + breaker; add tiny vertical slice ending before building more features.

## Last-known-good artifact tuple
GIT_MAIN_SHA: NONE_VERIFIED_FOR_STUDIO
STUDIO_UNIVERSE_ID: UNKNOWN
STUDIO_PLACE_ID: UNKNOWN
STUDIO_VERSION_NOTES_ID: UNKNOWN
PRIVATE_RBXL_BACKUP: UNKNOWN
BACKUP_CHECKSUM: UNKNOWN
SOURCE_CI: PASS on earlier snapshot (not current HEAD)
STUDIO_1_CLIENT: NOT RUN/UNVERIFIED
STUDIO_2_CLIENT: NOT RUN/UNVERIFIED
STUDIO_4_CLIENT: NOT RUN/UNVERIFIED
REAL_MOBILE: NOT RUN/UNVERIFIED
CONTROLLER_STATE: NOT IMPLEMENTED/NOT ACTIVATED
ACTIVE_AGENT: NONE VERIFIED
ACTIVE_ISSUE: #1 PLANNED, NOT CLAIMED
CYCLE_ID: NONE
ACKNOWLEDGED_PREVIOUS_HANDOFF: NONE

## Handoff update template
UTC:
AGENT / OBSERVED_MODEL:
CYCLE_ID / ISSUE:
MAIN_SHA / BASE_SHA / FEATURE_SHA:
LOCAL_PC_AND_WORKTREE_VERIFIED:
LOCK_OWNER / OTHER_AGENT_EXIT_CONFIRMED:
FILES_CLAIMED / RELEASED:
IMPLEMENTED_USER_FACING_BEHAVIOUR:
L0/L1 TESTS and logs:
L2/L3 STUDIO TESTS + player count/place ID:
L4 REAL DEVICE/PUBLISHED MODE:
SCENE_SAVE + RESTORE TEST:
KNOWN_GOOD_TUPLE:
BROKEN/UNKNOWN:
PR/ISSUE LINKS:
NEXT ONE ACTION:
RESPONSE NEEDED / BY WHOM:
