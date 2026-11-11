--!strict
-- INITIAL CONFIG SCAFFOLD ONLY. This does not implement any gameplay.
local Config = {
    WorkingTitle = "Signal Lost",
    MaxPlayers = 4,
    TargetRunSeconds = 30 * 60,
    SessionVersion = 1,
    DefaultScenarioSeed = 1,
    LivePurchasesEnabled = false,
    Stages = {
        "BOOT", "LOBBY", "INTRO", "POWER", "INVESTIGATION",
        "SIGNAL", "CONTAINMENT", "ENDING", "DEBRIEF", "RESETTING",
    },
}
return table.freeze(Config)
