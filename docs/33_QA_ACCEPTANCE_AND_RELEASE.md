# 33 — SECURITY, QUALITY, ACCURACY AND RELEASE CHECKLIST
Every line means PASS with evidence, FAIL, NOT RUN or BLOCKED. Planning or source CI alone cannot pass Studio acceptance.

## Operational / provenance
[ ] Correct source repo and SHA verified; original Dreadfall and Feudfall unchanged.
[ ] Correct NEW standalone Roblox universe and place IDs verified by owner.
[ ] servePlaceIds has zero entries until approval; after approval exactly correct NEW ID; no wrong-place Rojo sync.
[ ] Source files linted, Rojo build succeeds, Python guards pass.
[ ] Studio-authored map saved to correct place/version; shutdown, reopen and independent .rbxlx restoration works; backup SHA256 and path recorded privately.
[ ] Original asset ownership/third-party licence recorded before copying into PUBLIC repository or Roblox experience.
[ ] No passwords, secrets, sessions, cookies or unauthorized personally identifiable logs.

## Game stages
[ ] Solo complete from home to an ending with no scene/cutscene softlock and a clear restart.
[ ] 2-player same exact place sees synchronized radio, items, road states and ending; both may finish.
[ ] 4-player likewise; late join, disconnect, death, death holding radio, repeat join, new round clean state.
[ ] Cash/till/ATM work/fail consistently; unaffordable items not purchased; optional cash never mandatory; supplies never disappear on race.
[ ] Every scenario seed and route has at least one achievable ending, one safe way around blocked streets, predictable broadcast order and NPC state.
[ ] Looter AI bounded pursuit, no spawncamp, no impossible stolen vital item, avoidable without combat or accessibility penalty.
[ ] Radio subtitles and replay journal identical in meaning to audio; fallback mission objective if battery fails.
[ ] Emergency public information is clearly *fictional*, health facts sourced, no fake BBC/government endorsement, no claim that real UK blackout imminent.

## Adversarial security test plan
[ ] Forged remote actions for money/stock/teleport/pickup fail cleanly; rate limited without spam.
[ ] Concurrent purchases cannot overspend or duplicate stock; server authoritative.
[ ] Player drops while transferring an item; state resolves once without duplication or loss.
[ ] Malicious/old broadcast packet cannot open a locked rest centre.
[ ] Analytics derived from server verified actions, not arbitrary client notifications.
[ ] No purchases in alpha; later only durable idempotent server processing of actual Roblox receipts, owner-approved IDs, nonpaying parity.

## Accessibility and performance
[ ] Actual phone has legible subtitles, reachable mobile input and safe UI insets.
[ ] All mandatory tasks can be performed without audio; direction and threat cues visible and captioned.
[ ] Colourblind/high contrast and reduced camera movement/flashing options; no inaccessible quick-time events.
[ ] Profile memory, frame rate, input latency and Roblox networking on a representative real mobile device; optimize based on recorded results.
[ ] Safe replay, failed script recovery, phone rotation/OS UI interruptions and language fallback.

## Alpha exit
Minimum: no S0 (data loss, wrong place, purchases, security exploit) or S1 (hard progression blocker, restart broken, solo impossible, severe mobile unplayable); at least 2 complete runs at 1, 2 and 4 player counts across required scenario seeds; single source+scene last-known-good tuple. 5–10 human outside testers record first-run success/friction and honest average time. Owner approves private publish. No broad launch claims from private tests.
Beta exit: 20–50 consented players, content maturity questionnaire completed accurately, original art and license checks, outcomes/events consistent, clear public fictional disclaimer, monetisation reviewed separately. Public distribution requires new explicit owner approval.

## Reporting template
UTC, observed branch + HEAD, changed paths, issue ID, Studio place/universe IDs or UNKNOWN, approved Rojo state, tools tested with exact outputs/exit status, 1/2/4 actual runs PASS/FAIL/NOT RUN, mobile result, scene save/version and backup checksum, S0/S1 bugs, blocked approvals and ONE next action.
