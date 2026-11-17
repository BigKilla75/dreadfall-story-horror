# 28 — UK EVIDENCE, REALISM RULES, EMERGENCY RADIO AND STORY SAFETY
As of 17 Nov 2026. Source links below are primary/public and should be rechecked before writing any public-facing "realistic" claim. Fictional simulation only. No imminent-blackout claim.

## Evidence hierarchy
A. VERIFIED UK PUBLIC MATERIAL
- UK 2025 National Risk Register, "Failure of the National Electricity Transmission System" pp90–91: a rare extreme impact scenario; possible communications, fuel, water and critical-service impacts; variable gradual restoration and a hypothetical recovery up to seven days for electricity, longer for some critical services. This is a planning scenario, NOT a forecast. https://www.gov.uk/government/publications/national-risk-register-2025 and https://assets.publishing.service.gov.uk/media/67b5f85732b2aab18314bbe4/National_Risk_Register_2025.pdf
- Four Chief Medical Officers' contingency radio scripts published 16 Dec 2025: water and sanitation, food/nutrition, heat/cold; their advice is from independent health advisers and is explicitly NOT government policy. https://www.gov.uk/government/publications/public-health-advice-from-uk-cmos-during-a-national-power-outage
- A published cold-weather script identifies BBC Radio 2 and Radio 4 as potential emergency broadcast channels in this very unlikely scenario. This is an outlined contingency, not a guarantee or permission to copy BBC sound/branding: https://www.gov.uk/government/publications/public-health-advice-from-uk-cmos-during-a-national-power-outage/keeping-warm-or-cool-in-extreme-weather-scripts-for-broadcast-media
- UK Be Ready power-cut guide: torch and batteries, some cash in case payment systems/ATMs fail, battery/wind-up radio, food safety and communications; many services may or may not fail depending on location and backup power. https://beready.campaign.gov.uk/be-informed-about-hazards/power-cuts/
- Household general preparation guide: non-perishable food, water, hygiene, warmth, cash, radios. This is background reference, never literal coercive survival advice in-game. https://beready.campaign.gov.uk/be-ready-for-emergencies/
- UK mobile Emergency Alerts use 4G/5G masts without need for mobile data/Wi-Fi; working mast/compatible devices required. Alerts cannot be guaranteed after a blackout. https://www.gov.uk/alerts/how-alerts-work
- UK grid disruptions: 105 reaches local distribution network operator in GB where telecommunications remain operational. https://weather.metoffice.gov.uk/warnings-and-advice/seasonal-advice/your-home/what-to-do-in-a-power-cut
B. AUTHORISED FICTION FOR GAMEPLAY
- Brookmere, specific blackout date, cause unknown, ATM availability, looter numbers, closed roads, exact safe centre opening/closure, local responders and broadcasts. In a short outage, widespread immediate social collapse is NOT a justified factual assertion. Characters help one another; an occasional criminal group exploiting a dark shop is drama, not a demographic prediction.
- Clock compresses many fictional hours into 18–25 minutes. Convey acceleration through UI and shifts in lighting without treating it as an official schedule.
C. UNVERIFIED / PROHIBITED AS FACT
- That an "Operation Black Sky" will be triggered on a particular date, a current secret government operation, specific BBC words that "will" air, a deliberate cyberattack attribution, guaranteed 72-hour radio continuity, universal ATMs failing simultaneously, instant evacuation orders, police withdrawal or universal looting. Never use sensational claims from social media as research authority.

## BBC-adjacent branding and copyright
Never capture/play BBC Radio 2/4 audio, recreate a real BBC sonic ident, use BBC logo/official government crest, mimic recognizable living announcer's voice, impersonate current officials, or quote long scripts in the game without separate rights clearance. A neutral, clearly fictional "BROOKMERE PUBLIC INFORMATION RADIO" is the default. A legal/commercial review is required before any official branding or claims of endorsement. Open Government Licence permissions, where applicable, do not grant BBC logos/audio or third-party rights. Do not reproduce entire protected texts; write original paraphrased information with attribution in a credits/research panel.
A prominently accessible intro or menu note must say: "A fictional Roblox survival experience inspired by public UK emergency-preparedness guidance. Not affiliated with the BBC or UK government. Not real-time emergency information."

## Broadcast design contract
- Source is in a single server-side, versioned, reviewable table with fields: id, scenario_id, trigger, fictional_station, fictional_local_time, priority, plain-language subtitle, audio_asset_id_optional, event_effect, fallback_text, citation_basis and editorial_status.
- Type categories: NATIONAL_GENERAL (first safety info), HEALTH_ADVICE (food/water/warmth), LOCAL_CENTRE (fictional hub opening), TRAVEL_WARNING (fictional incident), SERVICE_RESTORED (scenario event).
- Server triggers and validates event effects; client requests audio UI only; never allow arbitrary client messages to pose as broadcasts. Stable event IDs; monotonic sequence; late join receives latest event plus transcript.
- All critical audio always has exact-equivalent subtitles, adjustable size, journal replay, and at least one clear visual objective. Audio optional; no player needs to identify a frequency by hearing.
- Separate NATIONAL information from LOCAL invented fictional instructions. No emergency-channel hijacking, live scraping, live BBC relay, AI voice impersonation, or player-authored "official" messages.
- Distinct callout label "FICTIONAL IN-GAME ANNOUNCEMENT". Optional original voice talent; record license/consent and pronunciation.

## Sample original broadcasts — writing examples, not sourced quotations
B001 / 19:42 / NATIONAL_GENERAL: "A widespread interruption to electricity supplies is being investigated. Please stay calm. Where safe, remain indoors and use a battery-powered radio for updates."
B002 / 20:18 / LOCAL_CENTRE: "Brookmere Community Hall is offering local assistance for residents who need support. Access via Mill Lane. Avoid the high street while a police incident is ongoing." [only when opened in that scenario]
B003 / 20:54 / HEALTH_ADVICE: "Check the safety of stored food and keep fridge and freezer doors closed where possible. Further public-health advice will be repeated." [review factual wording against official guidance]
B004 / 21:27 / LOCAL_WARNING: "A reported theft is being dealt with near the station shops. Do not approach those involved. Use a safer route or remain somewhere secure." [fictional]
B005 / 22:10 / LOCAL_OPTION: "The community rest centre at Brookmere School is now open for those specifically directed there. Residents who are safe at home should follow the latest advice." [scenario-dependent]
Do NOT make an NPC radio voice say "BBC Radio 4" as an ident unless rights reviewed; the factual source comparison appears only in research/credits.

## Crisis plausibility rules
- First hours: most civilians are concerned, helping neighbours, looking for information; criminals are exception. Electricity failure alone does not guarantee immediate lawlessness.
- Not every system instantly dies; battery backups and local variations exist. Cash is useful but cannot always be withdrawn. Pay by cash at a till only if staffed/open and stock exists.
- Real-life default depends on official local instructions, individual needs and safety. No universal go-to-shelter objective.
- Medical needs: do not simulate triage or real-life dosing; represent assistance through NPCs without misleading clinical directions.
- Avoid specific attack method, electrical-grid failure instructions or sabotage gameplay. The cause remains unknown; the experience is about public response.
- Welfare and accessibility: no punishment for accessibility settings; distress warnings and volume controls. No exploitative disaster clickbait.

## Review gate
Each line goes through: source/factual basis checked -> licensed/original -> distinct fiction label -> scenario/state event correct -> accessible subtitle -> PC/mobile speaker test -> approval. Log citations and reviewer in a CSV or Markdown ledger; do not label a draft "BBC verified" just because the background topic is genuine.
