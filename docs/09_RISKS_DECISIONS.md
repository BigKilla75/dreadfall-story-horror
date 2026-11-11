# 09 — Risks, unresolved decisions and change control

## Risk register
R1 Seven days too short for polished 30 min + 4 player co-op. Likelihood HIGH / impact HIGH. Mitigation: single reusable map, one enemy, no public matchmaking or live payments, owner-approved cut ladder. Escalate on Day 2 if route isn't traversable.
R2 Co-op state desync / duplicated triggers. HIGH/HIGH. Mitigation: one server state writer, deterministic reducers, idempotent interactions, 1/2/4 Studio tests. Critical blocker.
R3 Roblox Studio publishing is manual and environment-dependent. HIGH/HIGH. Mitigation: owner provides local Studio + Rojo access or supervised interaction, establishes place IDs. Never pretend GitHub source alone is playable.
R4 Roblox discoverability/revenue unknown. HIGH/MEDIUM. Mitigation: focus retention and completion; fair cosmetics after audience validated; no promised income.
R5 Threat/navigation too complex. MEDIUM/HIGH. Mitigation: waypoint/scripted encounter fallback and bounded chase.
R6 Mobile performance and legibility. MEDIUM/HIGH. Mitigation: low-cost lighting, subtitles/UI safe areas, early real device test.
R7 Public repository reveals concept/story/source. CURRENT/HIGH if secrecy desired. Mitigation: owner switches new repo to PRIVATE; do not upload proprietary licensed assets or credentials.
R8 Age-appropriateness and paid offer compliance. MEDIUM/HIGH. Mitigation: mild fear/art, accurate questionnaire, platform policies, no paid random items.
R9 Third-party free-model backdoors/asset theft. MEDIUM/HIGH. Mitigation: audit all inserted scripts, rights provenance list, prefer original assets.
R10 Agent collisions, invented progress. HIGH/HIGH. Mitigation: source ownership, PRs, issue acceptance, exact tests, review and no shared-file parallel edits.
R11 Reconnect/reserved server complexity. HIGH/MEDIUM. Mitigation: private single-place alpha then published controlled testing for true party matchmaking.
R12 Audio-led horror excludes players with sound off. MEDIUM/MEDIUM. Mitigation: subtitles and visual cue equivalents.

## Pending owner decisions (record in issues)
D01 FINAL game title and relationship (if any) to Dreadfall brand; default SIGNAL LOST as standalone working title.
D02 Repo privacy (currently PUBLIC); owner chooses PRIVATE if intended.
D03 Roblox Studio universe/place IDs and who has safe publish permissions.
D04 First-person intensity and visual age/maturity target (validate questionnaire).
D05 Audio/asset rights and whether actor voiceovers are available.
D06 Monetization price/product choice, after real testers confirm value.
D07 Whether first release is invite-only private alpha vs open beta; default invite-only.
D08 Business/account ownership and revenue split (do not assume any agent, contractor, or friend is entitled to revenue).
D09 Target platforms; default PC and real mobile for private alpha, controller stretch.
D10 Approval to reuse any asset from original Dreadfall; default NO cross-project copying.

## Change protocol
Document a proposed scope change with impact on days, risk, testing, and acceptance criteria. Require owner approval for changes affecting repo identity, funding, monetization, promises and the release scope. Mark each item PROPOSED, APPROVED, IMPLEMENTED, TESTED or RELEASED. Never conflate.
