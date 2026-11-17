--!strict
-- OPERATION BLACK SKY: CONFIGURATION ONLY. No actual game mechanics implemented yet.
local Config = {
    WorkingTitle = "Operation Black Sky",
    MaxPlayers = 4,
    TargetRunSeconds = 22 * 60, -- 18-25 min design range, not tested runtime
    SessionVersion = 2,
    DefaultScenarioSeed = 1,
    LivePurchasesEnabled = false,
    Stages = {
        "BOOT", "HOME_INTRO", "PREPARED", "SUPPLY_OPTION", "LOCAL_UPDATE",
        "DECISION", "STAY_HOME", "HUB", "REST_CENTRE", "ENDING", "RESULTS", "RESETTING",
    },
}
return table.freeze(Config)
