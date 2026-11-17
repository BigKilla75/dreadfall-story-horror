> **ARCHIVED — 17 NOV 2026:** Retired SIGNAL LOST story/workflow/monetisation only. **NOT ACTIVE.** Current game is OPERATION BLACK SKY; do not implement the Echo, Relay Nine, sci-fi puzzles or Codex tasks. Follow [README](../README.md), [Black Sky bible](27_OPERATION_BLACK_SKY_MASTER_PLAN.md) and [Claude's current prompt](34_CLAUDE_BLACK_SKY_MASTER_PROMPT.md). Original text retained below as history.

# 20 — Monetization, growth, marketing, publishing and live-ops blueprint
STATUS: Owner-requested commercial plan, not price or spend approval. Do NOT enable purchases, paid advertising or public access before explicit owner authorization and verified Roblox requirements. All figures below are proposed hypotheses, not revenue forecasts.

## 1. Core positioning
Brand working title SIGNAL LOST; logline "They called for a repair. Something answered." Position as FREE, 1–4 player, ~30-minute shared sci-fi horror, first complete chapter, one deceptive dispatcher, authored scares, optional evidence. Do not claim replay variants, multiple endings, mobile readiness or 30-minute measured duration until implemented and tested.
Differentiation: cooperative engineering interactions, contradictory AI dispatch narration, short complete session and player-driven curiosity. Inspiration: social dread/mystery audiences of DOORS, Pressure and short story-based Roblox horror; never copy assets, story, logos, UI or mechanics blindly.

## 2. Revenue architecture — free-first
Core chapter and every puzzle and ending FREE. Do not monetize fear, missed clues, darkness, recovery, clues, health, stamina, checkpoint or respawn. No paid randomized items, fake scarcity, intrusive interstitial sales, forced wait timers or pay-to-win.
Private alpha: NO sale prompts, zero live product IDs, no financial dependencies.
After retention/quality gate:
- Pass A: Cosmetic Radio Pack, proposed 49 Robux, 3 radio casing finishes with no acoustics/signal differences.
- Pass B: Supporter Pass, proposed 149 Robux, lobby nameplate, credits tag and purely cosmetic flashlight shell, equal gameplay brightness.
- Pass C LATER: Crew Suit Cosmetics, proposed 249 Robux, 3 noncompetitive looks if mobile rig/performance succeeds.
- Optional voluntary tip developer products 25/75/200 Robux only after ProcessReceipt ledger idempotency audit; avoid early complexity.
- Free unlock path: first-clear patch, all-evidence tag, no-failure cosmetic. Cosmetics worn in lobby or non-distracting gameplay; silhouettes remain legible.
- No subscription for a single 30-minute chapter. No paid private servers or paid access at launch; social group entry must stay easy. Revisit only if a repeat audience wants clearly ongoing value.

## 3. Technical purchase gates
Passes: owner creates products under the new game's own universe; server verifies ownership, safely retries and applies only cosmetic entitlement. Confirm Roblox regional pricing and displayed price; do not hardcode price assumptions.
Repeat developer products: MarketplaceService.ProcessReceipt on server, validate UserId/ProductId/PurchaseId, persist granted receipts via atomic UpdateAsync or equivalent idempotent datastore strategy. Return NotProcessedYet if safe durable grant is not possible. Never grant on client purchase-prompt finished events. Test duplicate receipts, server restart, disconnections and datastore failures in approved environment.
Owner must approve real IDs, prices, checkout copy, public catalog listing and transaction tests. Document refunds/support handling and no false purchase promises.

## 4. Business model and illustrative math
Roblox docs describe standard creator earnings as 70% for passes, though exact sale terms, price optimization, platform policies and regional factors must be checked for real items. Hypothesis: 10,000 legitimate visits, 1% buyer conversion, 99 Robux average pass spend => 100 purchases, 9,900 gross Robux and approximately 6,930 earned Robux at 70% BEFORE any costs. This is an arithmetic example only, NOT an expectation or DevEx cash; repeat products/fees vary. Actual money depends on reached audience, session quality, repurchases, eligibility, source and operational costs.
Track net earned Robux, purchaser conversion, ARPPU, complaint rate, return/retention, refund risk and creator marketing spend. DevEx currently requires at least 30,000 earned Robux plus other eligibility criteria; reaching that threshold does not guarantee cash-out approval. Roblox Creator Rewards (replaced older engagement-based payouts) may supplement earnings from genuinely eligible engagement; never farm sessions or promise a per-player payout.

## 5. Analytics event design (no fake or identifying records)
SERVER event schema common: eventName, runId, objectiveId, phase, contentVersion, scenarioSeed, partySize, deviceCategory (when safely known), event sequence and failureCode. Do not upload personal data, chat or player voice. Event names:
run_started; first_interaction; stage_completed(power/investigation/signal/containment); puzzle_failed; player_downed; player_respawned; disconnect_during_stage; ending_reached; replay_started; run_abandoned; shop_opened; offer_viewed; purchase_confirmed.
Instrument funnel: join→first_action→power→signal→chase→ending→replay; stratify 1 vs 2/3/4, mobile vs PC and new vs repeat. Use Roblox Analytics funnel or approved event services as supported. P0 can log local safe counters; do not build heavy live analytics before chapter works.

## 6. Experiment targets (project thresholds, NOT industry facts)
- First meaningful interact <=60 seconds for >=90% of alpha testers.
- >=70% of 5–10 first testers reach midpoint without human instructions.
- >=60% complete whole chapter on first valid run.
- 0 reproducible S0/S1 progression softlocks across release gate tests.
- >=20% self-report intent to replay/share; measure actual replay later.
- Real phone UI + no-sound completion proven.
After traffic, monitor Roblox first-play bounce rate, play-through rate, play days, time per user, co-play days, D1/D7 retention, payer conversion and acquisition by source. User sentiment and bug reports trump headline spend.
Roblox says discovery weighs PTR, bounce, play days and playtime and other metrics; optimize the first experience before marketing. Ads will not repair bad retention.

## 7. Creative and launch packaging
Icon: one clear silhouetted figure/radio mast, red signal bar on dark industrial background; must read at small size. Original logo mark, no misleading brand associations.
Thumbnail A: 2–3 co-op crew at actual lit communications door; B: actual control console + hint of Echo. Real representative in-game screenshots/videos are mandatory for launch images; concept renders are internal only, not passed off as real gameplay. Roblox 2026 video thumbnail rules restrict external overlays, spoken VO, nonrepresentative content and ad text; review Creator Hub rules at export time.
Description draft (after playtest confirms claims): "Your crew has one job: restore an abandoned relay. The voice on the radio knows too much. Investigate, solve cooperative puzzles and survive the transmission. Play solo or with up to three friends." Modify if any claim unverified.
Short-form video storyboards: (1) crew receives impossible message, cut to frozen monitor; (2) two friends align waveforms as silhouette appears; (3) ending tease without spoiler. Capture from real play build; captions on social platforms, no paid creator endorsements without disclosure and owner approval.

## 8. Audience and marketing sequence
PRE-ALPHA (days 1–7): no ad spend; create truthful teaser art privately, capture actual in-Studio clip once playable; recruit 5–10 opt-in friendly testers, ask what confused or scared them.
ALPHA VALIDATION (days 8–14 or once proven): 1/2/4 co-op and mobile tests, 3 short real gameplay clips, simple Roblox icon/title, survey and bug triage. No fixed public launch date.
CLOSED BETA (later): 20–50 opt-in testers across time zones; measure entry, midpoint, chapter completion, replay intent, device and group experience. Resolve top 3 dropoffs.
PUBLIC LAUNCH ONLY AFTER gates: publish accurate metadata; queue short genuine gameplay clips on creator-owned channels, announce to existing relevant communities without spam; approach small Roblox horror content creators with preview access and no undisclosed paid endorsements. User's spending approval required for sponsorships/ads.
POST-LAUNCH: hotfix urgent defects, review metrics weekly, add 1 tested authored variant/evidence beat before major chapter expansion; avoid feature proliferation. 2–4-week lightweight content cadence is a target, not promise.

## 9. Marketing experiments (no spend without owner approval)
- Organic A/B hypothesis: icon emphasizes "crew" versus "signal mystery"; track Roblox impression→play-through, not just clicks.
- Hook A/B: first transmission at 30 sec vs 45 sec; track first interaction, bounce, completion.
- Social hook: 10–20-second teaser emphasizing actual teammate reaction, no fabricated players.
- Beta question: "What moment would you show a friend?" Use direct qualitative answers to guide trailers and new content.
- PAID ADS only if conversion, retention and technical error thresholds have passed; cap initial spend at 0 by default, require budget and stop-loss from owner. Never use paid traffic to mask S1 bugs.

## 10. Publishing, maturity and reach checkpoints — verify in Creator Dashboard
As of Roblox's current Creator Hub documentation reviewed 15 Nov 2026, publishing/reach has distinct audience paths, age checks, content rating requirements and possible fee/subscription requirements for all-ages reach. Do not assume an experience automatically reaches every Roblox user. For age-checked 16+ release verify account standing/age check; reaching Kids/Select may require 2FA, additional eligibility/review, age content classification and possibly a publishing fee depending on subscription/eligibility. This is not a recommendation to pay the optional fee.
Use a truthful questionnaire; horror fear/intensity affects classification. Check current requirements before launch. Do not share credentials, upload restricted personal details or silently switch visibility/public access.

## 11. Revenue risk and operational costs
Costs to track: Blender asset creation hours, licensed audio/texture expenses (default 0 without approval), provider plan/runtime usage, optional ads, any release fee, device testing time, moderation and post-launch support. Never promise revenue in a 14-day development window. Defer monetization if product value, technical reliability or policy compliance is not ready.

## 12. Primary current sources
- Roblox monetization: https://create.roblox.com/docs/get-started/monetization
- Passes: https://create.roblox.com/docs/production/monetization/passes
- Developer products: https://create.roblox.com/docs/production/monetization/developer-products
- Creator Rewards: https://create.roblox.com/docs/creator-rewards
- Analytics: https://create.roblox.com/docs/production/analytics
- Discovery FAQ: https://create.roblox.com/docs/discovery-faq
- Publishing/reach: https://create.roblox.com/docs/production/publishing/publish-games-and-places
- Video thumbnails: https://create.roblox.com/docs/production/publishing/thumbnails
- Co-op Studio tests: https://create.roblox.com/docs/studio/testing-modes
- Partially managed Rojo: https://create.roblox.com/docs/projects/rojo
