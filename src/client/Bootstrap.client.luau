--!strict
-- PLACEHOLDER: does not implement HUD, atmosphere, input or co-op.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
print("[SignalLost] Client bootstrap scaffold loaded:", Config.WorkingTitle)
