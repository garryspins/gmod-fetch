local function arch(ar)
	if ar == "x86" then
		return "x86 (32 Bit)"
	else
		return "x64 (64 Bit)"
	end
end

local opsys = GFetch:AddModule("OS","os")
opsys:SetDescription("Operating System")
opsys:SetFunction(function()
	local text = "Windows"
	if system.IsOSX() then
		text = "Mac OS"
	elseif system.IsLinux() then
		text = "Linux"
	end
	return text.." "..arch(jit.arch)
end ) 
