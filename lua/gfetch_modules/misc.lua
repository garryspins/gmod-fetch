-- Screen Resolution (CLIENT)
local res = GFetch:AddModule("Resolution","res")
res:SetDescription("Screen Resolution")
res:SetState(CLIENT)
res:SetFunction(function()
	return ScrW().."x"..ScrH()
end )

-- Time
local time = GFetch:AddModule("Time","time")
time:SetDescription("Current Time")
time:SetFunction(function()
	return os.date("%I:%M %p")
end )
