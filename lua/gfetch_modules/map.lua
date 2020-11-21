local lst = {}
lst["gm_construct"] = "Construct"
lst["gm_flatgrass"] = "Flatgrass"
lst["gm_bigcity"] = "Big City"
lst["rp_downtown"] = "Downtown"
lst["rp_downtown_v2"] = "Downtown V2"
lst["rp_downtown_tits"] = "Downtown Tits"
lst["rp_downtown_tits_v2"] = "Downtown Tits V2"
lst["ttt_clue_se"] = "Clue"
lst["ttt_clue"] = "Clue"
lst["ph_clue_se"] = "Clue"
lst["gm_lair"] = "Lair"

local function mapf(m)
	return lst[m].."  ("..m..")" or m
end


local map = GFetch:AddModule("Map","map")
map:SetDescription("Current Map")
map:SetFunction(function()
	return mapf((game.GetMap() or "null"):lower())
end ) 
