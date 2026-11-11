# Codex / secondary agent contract

You are an independent engineering helper for BigKilla75/dreadfall-story-horror, a new Roblox project separate from original Dreadfall, Feudfall and Academy. Read README.md and docs first. Never modify the other repositories.

Preferred mode: highest available **reasoning/high-effort** option. Actual model labels/versions must be confirmed in your account; do not assume 'Sol6.1' or 'Opus 5.5' exist because they were suggested conversationally.

## What to do
- Request/choose one unclaimed GitHub issue with measurable acceptance criteria.
- Own isolated modules or review a PR. Work on a dedicated branch; do not race Claude on the same files.
- Highest-value tasks: Luau type safety, replicated event payload contracts, server authorization/rate limiting, session state machine tests, edge cases with 1/2/4 players, purchase idempotency analysis, performance inspection, documentation checks.
- Prefer small, reviewable PRs, with exact test logs and proof. Don't invent Studio access, places, product IDs or passing tests.
- Use Roblox official docs for APIs; check versions before adding packages.
- Flag exploits and data loss first, then reliability, accessibility, polish.
- Never enable purchases, production deploys or modify repo visibility without explicit owner approval.

## Review checklist
1. All client-originated requests validated for type, range, player state, stage, proximity and rate on SERVER.
2. Shared stage remains consistent through joins/leaves, duplicate inputs, race conditions and player death.
3. No unbounded loops, unnecessary high-frequency remote spam or expensive per-frame logic.
4. No external scripts, unsafe Toolbox models, copied assets or secrets.
5. Mobile and gamepad alternatives for all essential inputs.
6. Safe fallback when DataStore/teleport/network calls fail.
7. Same-player/party rewards cannot be claimed twice; developer product receipts only acknowledged after idempotent grant.
8. Tests have exact execution evidence, not optimistic checkmarks.

## Agent collaboration
Claude integrates runtime and Studio scene. Codex reviews or completes one explicitly assigned isolated issue. Use PR comments and issues for communication; assistants have no magical direct cross-account messaging. Owner resolves product and access decisions. Never auto-merge critical gameplay/purchase logic without review.

## Environment checks
Read docs/13_STUDIO_ENVIRONMENT.md. Use pinned Rojo 7.7.1 through scripts/dev.py; run python -m unittest discover -s tests -v and python scripts/dev.py build before PRs. The initial empty servePlaceIds list is an intentional protection against syncing into the wrong place. You may verify code in Codespaces, but Roblox Studio GUI tests require a Windows/Mac host. Never silently bypass this lock or claim that source CI proves 1–4-player gameplay.

## Selene gate
Run `selene src` (Roblox std, pinned 0.32.0) on each touched Luau module and note exact result; repo CI will also enforce it. Read docs/13_STUDIO_ENVIRONMENT.md for the owner-reported already-installed Windows/Studio/Rojo/Selene environment. No need to reinstall tools if version checks pass.
