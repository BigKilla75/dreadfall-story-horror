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
