> **17 NOV 2026 ACTIVE GAME: OPERATION BLACK SKY.** This generic Claude-only operations/recovery guide remains active, but the old SIGNAL LOST creative master prompt docs/25 has been superseded by docs/34_CLAUDE_BLACK_SKY_MASTER_PROMPT.md. Do not implement old Echo/Relay Nine gameplay. No unattended automation approved.

# 26 — CLAUDE-ONLY EXECUTION, SAFE CONTINUITY, TESTS AND RECOVERY
**CURRENT AUTHORITY as of 15 November 2026.** This replaces the active dual-agent workflow described historically in docs/18, 19, 21, 23, 24. It does NOT delete those earlier planning records. Read docs/25 for the executable master prompt.

## Absolute single-writer rule
- Claude Opus is the sole coding, review, Blender and Roblox Studio development agent for this standalone horror game. NO Codex involvement, no relay jobs, no agent rotations, no alternate AI coding process or branching strategy designed around multiple live writers.
- Maintain one canonical game: a SINGLE new Roblox universe/place and one controlled Rojo integration connection; create feature branches if useful, but those are source branches, NOT competing Roblox games.
- GitHub Actions may run deterministic automated checks and the owner may perform human playtests, neither counts as another coding agent.
- Use a clean main integration checkout for the approved target. Confirm source and place identity before every sync; no two Rojo listeners. Maintain source work on a feature branch or safe sequential local checkout, never simultaneously modify unsaved integration work.
- The original Dreadfall and Feudfall remain READ-ONLY asset/research sources. Never change their repos or experiences.

## One Claude work session
1. RECOVER: read docs/22, GitHub HEAD, open issues, current branch/dirty files and last-known-good Git+Studio tuple. Examine local Studio identity, current Rojo connections and existing save state; never overwrite unknown changes.
2. CHOOSE: highest-severity blocker first; otherwise one small player-facing issue with acceptance and estimated 1–3 productive-hour scope. Break work into testable slices.
3. IMPLEMENT: write Luau/Blender/Studio work in the new project only. Keep reversible, minimal changes. No re-platforming or new speculative infrastructure.
4. VALIDATE: lint, unit tests, Rojo source build; then actual main Studio smoke with 1/2 clients; add 4-client after co-op changes; check Output and visual scene. Use device/mobile testing at required gates, not fake approximations.
5. SAVE: commit/push source; save Studio experience with version note; export dated private place backup; independently reopen restored artifact at least at relevant milestones. Record scene export checksum and corresponding Git SHA.
6. REPORT: update docs/22_CURRENT_STATE.md with SHA, exact player tests, issue, scene save/version, backup checksum, verified/unknown and single next step. Never advance a false pass.
7. CONTINUE: if current session has capacity and no blockers, move to next unblocked issue; otherwise checkpoint and stop cleanly.

## Controller vs normal CLI sessions
Manual Claude sessions with durable checkpoints are available now. A local runner that schedules/restarts Claude can only be considered after: owner authorization; no conflicting existing Dreadfall controller; exact repository/process/Studio locks; power/network/quota/auth safe pause; emergency stop; crash/dirty-state recovery; source+Studio canary and a published audit showing no duplicate executions.
The previous autonomous Dreadfall controller was quarantined. Never copy/activate or repurpose it without owner-approved audit. No truthful claim of unattended 24/7 development before a tested authorized runner operates on Windows. Automation is a future engineering task, not a default in this repository.

## Mandatory integrity and testing gates
A known-good gameplay snapshot is a matching tuple: (Git main SHA, approved universe+place ID, Studio saved version/time, private .rbxlx backup+checksum, Rojo config revision, asset manifest revision, actual 1/2/4 tests and date).
Progress is accepted ONLY when new gameplay works in the SAME main Studio game and the matching source and scene are recoverable. Never claim a source-only CI artifact recreates Studio-only map content.
Smoke: load, spawn, GUI objective, local interact, authoritative stage for second client, safe prompt/retry, output errors, ending stub, replay/reset.
Regression: invalid remote inputs, double-press, late join, disconnect, death/respawn, clue/puzzle solvable solo, scene save/close/reopen, 4-player event sequencing, performance/low settings and phone.
S0: wrong-place sync, data loss, unrecoverable scene, critical exploit, play-blocking fault => stop feature growth and repair.
S1: required story path/co-op failure, missing ending, unhandled session restart => block private alpha.
S2: mobile/readability/performance failure => block public release; assess private test risks.
S3: small cosmetic flaw => defer.

## Reporting and honest forecasting
For each issue record estimate vs actual productive minutes, test time, rework, verified acceptance and remaining p50/p80 hours. Don't measure progress by file count or raw commits.
After day 3, compute a reforecast from actual passing milestones and known defects, not 14-day marketing promise. Keep one prioritized WIP issue at a time. If behind, cut scenario variants, extras and decoration BEFORE core security, reliable saving, co-op synchronization or a free complete ending.

## Owner-only boundaries
Ask owner for separate Roblox place creation/authorization when needed, public/private experience or repository visibility, any real Robux prices/products or spend, policy/rating submissions and public launch, irreversible changes or ambiguous licenses. No advertising, product activation or public publish by default.

## How to handle old documents
Historical docs/19 and docs/21 were written when user wanted dual-agent rotations. Those are retained as an audit trail but NOT instructions to start Codex. Docs/18 and docs/24 contain task content with old Codex rows; reinterpret all reviews, tests and implementation as work for Claude itself. The master prompt docs/25 and THIS file take precedence.
