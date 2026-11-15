# 19 — Sequential dual-agent development protocol and Windows automation specification
STATUS: PROPOSED; NOT INSTALLED, APPROVED FOR UNATTENDED ACTIVATION, OR VERIFIED ON WINDOWS. Updated owner intent 15 Nov 2026 supersedes the earlier Claude-only restriction only for planning and for controlled Codex contribution AFTER safe handoffs are proven. Until then Claude remains the only writer.

## North star: exactly one game
One repo BigKilla75/dreadfall-story-horror; ONE canonical MAIN Roblox place and universe; ONE integration worktree and Rojo server; one currently ACTIVE implementation task and ONE active agent process on PC. Separate agent worktrees/branches may be stored, but they are NOT separate games. Original Dreadfall and Feudfall repositories may only be read for rights-cleared copy candidates; their original places/commits/settings never change.

## Why the previous workflow failed / evidence boundaries
Original Dreadfall has docs/NEW_ACCOUNT_HANDOFF.md, docs/AGENT_COLLABORATION.md, docs/masterplan/09_BOOTSTRAP_RECOVERY_AND_HANDSHAKE.md and tools/studio-smoke/, tools/session-smoke/. Useful: repository bootstrap, current SHA readback, issue/PR exchanges, isolated branches, last known-good source, and distinction between simulated and real playtests. REJECT: old Dreadfall game canon, concurrent worker dispatch, its protected original Studio path, agent file ownership assumptions and any instruction to enable its quarantined #27/#28 controller. A GitHub issue comment does NOT notify/wake either agent. Same GitHub account posting does NOT identify a particular AI. Local runner must actually deliver and await readback.
No old autonomous controller has been audited or activated for this standalone horror game.

## Three protected workspaces (example names, verify actual Windows host)
- Integration: C:\Projects\signal-lost-main on clean main. ONLY this worktree starts Rojo and syncs approved MAIN Studio place; no feature edits here.
- Claude feature tree: C:\Projects\signal-lost-claude on claude/<issue>-<slug>.
- Codex feature tree: C:\Projects\signal-lost-codex on codex/<issue>-<slug>.
Agent worktrees have separate branches and do not run live Rojo; the workstation never runs both agent processes simultaneously. Local worktree path is an example, not a verified real folder. Run git remote -v and git worktree list each session.

## Controller modes and activation policy
Manual mode (allowed now): operator starts Claude, waits for clean handoff and full process exit, starts Codex, waits for handoff/exit, starts Claude integration. Single Studio operator (Claude) alone syncs and saves. No new daemon needed.
Automatic mode (future, ONLY after independent safety audit, host trial and owner activation): single local Windows supervisor with a real exclusive OS file lock/mutex, persistent append-only event log, durable atomic state checkpoint, official provider launch adapters, dedicated process group per shift and clean-stop semantics. Never start a second controller while any other development runner is active.
No cloud scheduler, agent plugin, GitHub issue label or ChatGPT answer itself starts sessions. Host off, lost network, unavailable provider/usage quotas or missing Roblox GUI => checkpoint, safe pause. No fabricated constant-running claim.

## State machine (new controller PROPOSAL only; do not copy incompatible old Dreadfall enums)
IDLE → PRECHECK → CLAUDE_BUILD → CHECKPOINT_CLAUDE → CODEX_REVIEW_FIX → CHECKPOINT_CODEX → CLAUDE_INTEGRATE → STUDIO_TEST → PERSISTENCE_VERIFY → VERIFIED → PRECHECK.
Exception states: QUOTA_PAUSE, AUTH_BLOCKED, DIRTY_WORKTREE_BLOCKED, STUDIO_TARGET_BLOCKED, TEST_FAILED, OWNER_REQUIRED, RECOVERING, STOPPED.
Every transition MUST be stored durably with generation number and SHA before the next provider is launched. Never infer agent completion from elapsed time alone.

## 60/30 + integration cadence
- Claude target 60 productive minutes: implement ONE issue slice, run unit/static checks, commit/push branch and produce a machine-readable handoff; then exit. At boundary, finish or safely suspend atomic action; no forced kill during save/publish.
- Codex target 30 productive minutes: read EXACT Claude head and latest handoff, independently review and implement only a bounded regression/security/performance improvement on codex branch; tests, push, handoff, exit. If no safe scope to edit, review only.
- Claude integration 10–25 minutes variable: fetch Codex branch, check full diff/tests, merge only verified isolated changes, run real Studio smoke on MAIN, save/backup and update LAST_KNOWN_GOOD. Any failure pauses feature growth and starts repair.
- If Studio testing/Blender export cannot be safely finished at 60 minutes, extend to checkpoint or explicitly pause before transferring. More frequent tiny handoffs may reduce net throughput; after Day 2 compare empirical overhead before keeping fixed cadence.
- No live Studio edits by Codex; no two Studio connections; no independent place files used as alternate authoring source.

## Mandatory handoff record (machine-parseable fields and human explanation)
A handoff requires a durable commit or explicit dirty-state block. Include:
AGENT; MODEL_AS_CONFIGURED (observed label/version, not invented); UTC; CYCLE_ID; ISSUE; MAIN_SHA; BASE_SHA; HEAD_SHA; BRANCH; WORKTREE; DIRTY_STATUS; FILES_TOUCHED; FILES_OWNED/RELEASED; STUDIO_PLACE_ID; STUDIO_SAVE_LOCATION + CHECKSUM + saved UTC; ROJO_PORT/PROCESS_OWNER; BUILT_FEATURE; TEST_COMMANDS + EXIT_CODES; STUDIO_PLAYER_COUNT/TEST_METHOD + evidence; BUGS_BLOCKING; BLOCKERS/QUOTA; ACKNOWLEDGED_PRIOR_HANDOFF_ID; NEXT_EXACT_TASK; QUESTION_IF_OWNER_REQUIRED.
Store durable source information in docs/22_CURRENT_STATE.md (short current snapshot), GitHub issue comment and PR. Have each agent ACK the previous handoff with its base SHA and action before modifying anything. GitHub messages are storage, not delivery; supervisor passes them explicitly into agent startup prompt.

## Required host-side safeguards (not claims of implemented code)
1. Atomic exclusive controller lock at OS level; no time-only/stale PID lock reuse. If PID disappears, verify process group exit, git status, Studio state and previous save before recovery. Do not silently steal lock.
2. Process census ensures no existing Claude/Codex session or duplicate Rojo listener is writing this game; no supervisor takeover of original Dreadfall/Feudfall processes.
3. Verify repository origin, canonical branch SHA, clean integration tree and active issue before an agent starts. If wrong repo / dirty uncommitted work / SHA mismatch, BLOCK.
4. Prevent Codex from modifying integration worktree or syncing Studio; keep credentials isolated and tool permissions minimal. Source-project repos require read-only credentials / commands where feasible.
5. On agent exit verify the exact output branch SHA; never apply unpushed changes from another worktree. Resolve base conflicts before merge, do not force push to main. Issue status and file claims MUST correspond to actual locks, not just labels.
6. Failure policy: save source and Studio if safe, attach logs, STOP the next shift. Do not skip failing smoke or mark known-good prematurely. No automatic public publish, monetization, spending, asset ownership changes or content rating changes.
7. Quota policy: gracefully pause, store exact provider error class, back off using documented reset time, do NOT farm alternate identities or create uncontrolled retry loops. Provider availability must be checked from real local output.
8. Owner emergency stop must cancel future dispatch; allow current safe checkpoint or immediate safe process stop if necessary. Monitor daily, retain log quotas and machine resource limits.
9. Before unattended mode: demonstrate a dry-run (dummy agents), then 3 actual *manually observed* safe sequential cycles, forced quota/network failure, simulated crash recovery, stale handoff rejection, dirty workspace rejection, and Studio save/reopen test. Record results. Only then request owner activation.

## Test pyramid and status semantics
L0: Git repo/config, JSON, lint, Rojo build; not Studio gameplay.
L1: deterministic Luau unit tests: phase transition, authorized puzzle actions, idempotency, validation.
L2: automated Studio smoke in SAME main place via StudioTestService plugin if installed and validated; no assumption it is configured. Simulated 1/2/4 clients, start, spawn, interact, stage advance, reset, failure cases. Source test alone does not count.
L3: manual Studio scene inspection / save-close-reopen / 1,2,4 client co-op traversal; record exact branch SHA, place ID, backup and actual outcome.
L4: controlled published private server + real device, friends, mobile and network latency, and commerce only after owner signoff.
Severity: S0 data loss, wrong-target sync, broken join, softlock, exploit, no rollback => immediate stop; S1 main chapter cannot finish, broken co-op => block alpha; S2 accessibility/perf risk => fix before public; S3 visual polish => defer.
Every handoff must run L0/L1 relevant checks; every integration at least L2 or a documented manual L3 fallback; each day L3 including restart/save; no night of accumulating unintegrated PRs.

## ONE known-good unit
A releasable gameplay checkpoint is a tuple:
(Git main SHA, exact Roblox universe+place ID, Studio save/version + local export checksum, Rojo configuration revision, relevant test evidence, asset manifest revision, UTC).
A Git tag alone cannot restore a Studio-only map. A Studio backup alone cannot restore file-backed scripts. Keep both, prove reopen. Store backups PRIVATE off repo unless rights/storage policy supports binary versioning. Never delete older known-good until newer one is verified.

## Conflicts and failure recovery
If both agents touched same file on different branches, Codex change remains unmerged pending Claude diff-based integration; no silent auto-merge. If Studio scene and Rojo mapping disagree, stop sync, compare and restore known-good; never guess which side wins. If previous handoff is absent, unknown or unacknowledged, next shift performs only audit/readback and no implementation. If 60/30 rhythm creates >20% overhead in first two days, switch to 90–120 minute Claude blocks and bounded Codex audits at coherent milestones; the shared-game guarantee matters more than the clock.

## Final statement
This file describes a proposed safe orchestrator, NOT an active automation. A running Windows controller with actual provider adapters and Studio access must be implemented, tested and expressly activated on the PC before claiming constant autonomous development.