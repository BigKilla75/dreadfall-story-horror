--!strict
-- PLACEHOLDER ONLY: no survival game, enemy AI, server radio or Studio map implemented.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
print("[OperationBlackSky] Server scaffold loaded; version", Config.SessionVersion)
