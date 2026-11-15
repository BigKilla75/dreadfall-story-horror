# AGENTS.md — Codex conditional sequential-turn policy (owner update 15 Nov 2026)

## Mission
The owner now wants Claude Opus and Codex to contribute to ONE standalone horror game in STRICTLY SEQUENTIAL shifts. The earlier Claude-only development period is superseded by this specific instruction for planned Codex involvement. This is **not** permission for simultaneous development or unattended controller activation.

Claude is lead gameplay architect and the ONLY canonical Roblox Studio operator, live Rojo sync operator, integrator and release owner. Codex contributes code/test/security/performance fixes ONLY on a separate branch and ONLY after Claude's complete, acknowledged, clean, pushed handoff and full process exit. Never edit the integration worktree, Studio scene, original Dreadfall or Feudfall projects, or another agent's uncommitted files.

Until handoff safety is locally validated, Codex mode = read-only source audit and concrete improvement proposals. Later bounded implementation is allowed through manual serial shifts, with Claude reviewing and integrating. Autonomous unattended operation remains BLOCKED until an exclusive Windows controller has passed dry-run, crash/quotas, save/reopen, 1/2-client Studio canary and owner activation.

## Every Codex turn
1. Read docs/17–22, current CLAUDE.md, exact main/head, last handoff and GitHub issue/PR evidence.
2. Verify that Claude session has exited and branch state/lock/claimed files are safe. ACK the precise main/branch SHA.
3. Respond to relevant C01–C14 questions in docs/21. Identify highest-risk failure first.
4. If implementation mode is verified, make one bounded change on codex/<issue>-<slug>; never start Rojo serve/Studio or touch uncommitted integration.
5. Run Selene, unit tests, Rojo source build as appropriate; commit/push, document tests and Studio testing NOT PERFORMED.
6. Exit, release claimed files and hand off to Claude for human-readable review, integration and actual Studio smoke.
7. Stop immediately on stale SHA, dirty workspace, conflicting process, missing owner permissions, wrong target or unproven backup.

## Boundaries
- Original Dreadfall postponed; preserve BigKilla75/roblox-game.
- Feudfall preserved; owner permits rights-cleared one-way asset copies from both older projects; scripts/assets must be provenance-checked. See docs/14–16.
- No public game launch, purchases, paid subscriptions, real product creation, ads, new secrets or unsafe third-party assets without owner approval.
- Source tests and CI do not prove Roblox Studio gameplay. GitHub messages do not wake or notify other agents.

## Ready-to-use scoped turn prompt
Use the Codex launch prompt in docs/23_AGENT_START_PROMPTS.md only AFTER an exclusive handoff is verified and Claude has exited.
