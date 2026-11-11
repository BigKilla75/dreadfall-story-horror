# 04 — Revenue strategy, pricing hypotheses and player trust

**Status:** proposal only. NO live Robux sale implemented, approved, or tested. Owner creates game passes/developer products after Roblox experience publish. All pricing here is experimental and requires owner decision.

## Core ethics and business model
Free access to the whole 30-minute narrative, clues, endings and co-op. Sell clearly named, guaranteed cosmetics and voluntary support only. No paid revives, energy timers, mandatory flashlights, "buy clue" gates, random paid crates, story endings, unfair brightness, speed or stealth advantages. All major shop actions outside chase/critical story scenes. No false scarcity/discounts. Never claim money is guaranteed.

## Proposed first catalog (Robux price hypotheses, not promises)
- Radio Casing Pack (49): 3 purely cosmetic radio skins; does not alter sound clues or gameplay.
- Supporter Pass (149): lobby nameplate, decorative badge, supporter credits, cosmetic flashlight exterior; identical light output for all users.
- Crew Appearance Pack (249): 3 non-advantage suit appearances; visibility silhouette rules still equal.
- Tip Jar developer products (25 / 75 / 200): pure voluntary support; repeat purchases grant only gratitude message and receipt history, no gameplay advantage.
Start with **one 49 Robux cosmetic and one 149 Robux supporter pass** after quality/policy validation. Don't launch a large shop or subscription for one chapter. Free earned cosmetics prevent a pay-only identity economy. Prices and net proceeds depend on regional pricing and Roblox terms.

## Transaction implementation contract
- Pass: one-time entitlement checked with platform purchase APIs; server grants cosmetic after validated ownership. Cache conservatively and handle lookup failure.
- Developer product: **MarketplaceService.ProcessReceipt** on SERVER; verify allowed product ID/user/receipt. Make grant idempotent, save receipt ledger and reward atomically or acknowledge only after safe durable grant. Prompt completion events are not proof of payment.
- For repeated tips, never accidentally double-issue rewards after retry. If purely a tip, record successful receipt safely and show thank-you, without a fake delivered digital item.
- No client-authoritative currency/entitlement grants. No secrets in repository.
- Never test actual payments using live Robux without clear owner approval and a test plan. Manual product IDs configured only after creation; leave placeholders until then.
- Check Roblox PolicyService where applicable. Avoid all paid random items; if future designs use them, rigorous restrictions and odds disclosure apply.
- No subscription, paid access, paid private server or ads in alpha; reconsider only if users return repeatedly and monthly value exists.

## Creator Rewards and retention
Roblox's Creator Rewards can include Daily Engagement rewards under specific conditions. This is not a guarantee per visit: the documented example is 5 Robux for an eligible active spender's 10+ minute daily play when the experience is among their first three that day. Do not fabricate sessions, encourage alts or pad waiting time. Evaluate organic retention, recommendations and legitimate new users; read official current documentation before making forecasts.

## Revenue model (illustrative, not forecasts)
Earned Robux from passes ≈ unique visitors x buyer conversion x average spend per paying visitor x applicable creator share. Developer products may be repeated, so separate unique buyer count from purchase count. Track **net earned Robux**, not headline Robux sales, and account for regional pricing/refunds/platform terms. Net cash availability depends on DevEx eligibility and rules. No assertion of expected profit without visits, conversion, platform share and marketing costs.

## Conversion funnel
Join -> first objective -> first scare -> Act 2 -> ending -> debrief -> optional cosmetic storefront visit -> product view -> purchase prompt -> confirmed receipt -> cosmetic visible -> player satisfaction/return. Do not show shop on initial spawn or during fear encounter. Measure purchase conversion and refunds alongside negative reviews and churn; eliminate items that harm trust.

## Monetization milestones
P0: catalog mockups only, all products disabled, no real IDs.
P1: free cosmetics and profile saving.
P2: first two passes after end-to-end entitlement / mobile / account testing.
P3: tips and price experiments after the cosmetic store is stable.
Any live monetization needs manual product setup and owner approval.

## Sources
https://create.roblox.com/docs/production/monetization
https://create.roblox.com/docs/production/monetization/passes
https://create.roblox.com/docs/production/monetization/developer-products
https://create.roblox.com/docs/production/monetization/paid-random-items
https://create.roblox.com/docs/creator-rewards
