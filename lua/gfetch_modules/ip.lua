local safemode = true

local ip = GFetch:AddModule("IP Address","ip")
ip:SetDescription("Server IP Address")
ip:SetFunction(function()
	if safemode then
		return "█.█.█.█:██"
	end
	local ipad = game.GetIPAddress()
	if ipad == "0.0.0.0:0" then
		return "Singleplayer"
	end
	return ipad
end )