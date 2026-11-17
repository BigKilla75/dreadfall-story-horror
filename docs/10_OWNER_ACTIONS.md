> **ARCHIVED — 17 NOV 2026:** This is the retired SIGNAL LOST creative/gameplay plan. **DO NOT IMPLEMENT IT.** Current game is OPERATION BLACK SKY. Follow [README](../README.md), [Black Sky master plan](27_OPERATION_BLACK_SKY_MASTER_PLAN.md), and [Claude's active prompt](34_CLAUDE_BLACK_SKY_MASTER_PROMPT.md). Kept intact below for provenance and rollback; all Echo/Relay Nine/Codex tasks superseded.

> **SUPERSEDED WORKFLOW — OWNER OVERRIDE, 15 NOVEMBER 2026:** Claude Opus / Claude Code is the **ONLY** development agent for SIGNAL LOST. Codex and all multi-agent/rotating schedules are CANCELLED. Preserve the gameplay objectives and acceptance gates below but reassign ALL implementation, testing and review to Claude. Do not start/dispatch Codex, a two-agent supervisor or the quarantined original Dreadfall controller. For current instructions read [CLAUDE.md](../CLAUDE.md), [docs/25_CLAUDE_MASTER_PROMPT.md](25_CLAUDE_MASTER_PROMPT.md) and [docs/26_CLAUDE_SOLO_OPERATIONS.md](26_CLAUDE_SOLO_OPERATIONS.md). Old text is retained only to preserve history. 

# 10 — Owner actions required for real autonomous development

## Now (minimum human actions)
1. **GitHub privacy:** this repository was verified PUBLIC on 11 Nov 2026. If your concept/source should be private, GitHub -> repository Settings -> General -> Danger Zone -> Change repository visibility -> Private. The ChatGPT GitHub tool cannot perform this action.
2. **Roblox Studio:** create a completely new Roblox experience/place, independent of original Dreadfall and Feudfall, with a temporary private-test access mode. Save a working local copy/backup. Determine universe and place IDs; these identifiers may be committed only after verifying the correct new project, but never commit API keys/session cookies.
3. **Claude execution:** give Claude Code access to this repo AND a functioning Roblox Studio + Rojo environment (local machine or supervised remote executor); GitHub access alone cannot construct/publish a Roblox place. Allow Claude to open PRs; don't let any agent blindly sync to an unknown place ID.
4. **Test helpers:** schedule 2–4 friends and at least one mobile device for short playtests; a single local scripted test cannot substitute for actual network/device validation.
5. **Assets:** approve only owned, licensed original or appropriately licensed reusable meshes, audio and animations. Keep provenance.

## Optional inputs for better quality
- 1 or 2 visual mood references (not copied scenes), preferred realism/stylization and jump-scare intensity.
- Budget for licensed sound, animations or studio assets. Zero-cost default if unapproved.
- A 20–30 minute time slot daily for creative decisions and Studio publish/testing.
- Decide final brand and preferred private/public launch date once gated testing is complete.
- Consent before monetization offers, purchase testing, any ad spend or social account actions.

## Owner does NOT need to do
- Write Luau code; agents can prepare scripts.
- Create all design documentation; already versioned here.
- Share password, Roblox cookies or personal access tokens in ChatGPT/issue text.
- Give assistants blanket administration permissions over original game repositories.

## Agent execution reality
A GitHub commit is not a Roblox game. Agents can autonomously work when an active agent environment has local source, Studio integration, appropriate permissions and a work queue. They cannot truthfully claim a deployed game, completed player tests, created marketplace passes or continuous background work without those connected tools and evidence.

## Publishing process once alpha passes
Owner opens the intended new Roblox place, reviews Studio assets/sync target, confirms game privacy, runs team tests, publishes private test build, completes Roblox maturity questionnaire and invites testers. Record screenshot/test result and released version. Real Robux offers remain disabled until a separate monetization approval and receipts QA.

## Safe local environment setup
See docs/13_STUDIO_ENVIRONMENT.md for the exact Rojo/Rokit/Studio installation and daily commands. Live sync starts **locked** through servePlaceIds: [] until a NEW independently verified place ID is provided. Never use the original Dreadfall or Feudfall place IDs. The optional Codespaces container runs CLI builds but cannot execute Roblox Studio GUI. GitHub Actions verifies source, not Roblox game functionality.

## Owner decisions already granted (15 Nov 2026)
- HISTORICAL (superseded later on 15 Nov): Claude Opus was sole developer. Owner subsequently requested sequential Opus/Codex coding turns with Claude exclusive Studio integration. Codex only works after safe committed handoff; unattended controller activation remains separate owner-gated action. See docs/19.
- Original Dreadfall development is postponed due to complications. Do not modify its source or Studio place; Feudfall also stays untouched.
- Claude may reuse suitable rights-cleared assets from both source projects through **one-way copying** into the horror project. No per-asset reapproval needed when rights and provenance are clear; do not import uncertain third-party licenses or untrusted scripts.
- Existing Windows Studio/Rojo/Selene installation is owner-reported. Do not reinstall blindly.
