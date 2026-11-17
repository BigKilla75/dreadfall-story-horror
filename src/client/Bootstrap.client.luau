--!strict
-- PLACEHOLDER ONLY: no inventory, HUD, blackout visuals, radio or gameplay implemented.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
print("[OperationBlackSky] Client scaffold loaded:", Config.WorkingTitle)
