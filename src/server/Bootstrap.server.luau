--!strict
-- PLACEHOLDER: no runtime game systems or Studio scene are implemented yet.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
print("[SignalLost] Server bootstrap scaffold loaded; version", Config.SessionVersion)
