# Structure to functions command
# V0.2
# Created by dakonblackrose & StealthyExpert

from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
from pymclevel import TAG_Float
from pymclevel import TAG_Int
from pymclevel import TAG_List
from pymclevel import TAG_Double
from pymclevel import TAG_Long
import inspect
import random
import math
import os, tempfile
import pyperclip
import io
import os
import json
import shutil
import sys
from itertools import izip_longest

script_path = os.path.dirname(__file__)

#Java Ids 1.12 to Java 1.12 Function.
names = {
	"0": "air",
	"1": "stone",
	"2": "grass",
	"3": "dirt",
	"4": "cobblestone",
	"5": "planks",
	"6": "sapling",
	"7": "bedrock",
	"8": "flowing_water",
	"9": "water",
	"10": "flowing_lava",
	"11": "lava",
	"12": "sand",
	"13": "gravel",
	"14": "gold_ore",
	"15": "iron_ore",
	"16": "coal_ore",
	"17": "log",
	"18": "leaves",
	"19": "sponge",
	"20": "glass",
	"21": "lapis_ore",
	"22": "lapis_block",
	"23": "dispenser",
	"24": "sandstone",
	"25": "noteblock",
	"26": "bed",
	"27": "golden_rail",
	"28": "detector_rail",
	"29": "sticky_piston",
	"30": "web",
	"31": "tallgrass",
	"32": "deadbush",
	"33": "piston",
	"34": "piston_head",
	"35": "wool",
	"36": "piston_extension",
	"37": "yellow_flower",
	"38": "red_flower",
	"39": "brown_mushroom",
	"40": "red_mushroom",
	"41": "gold_block",
	"42": "iron_block",
	"43": "double_stone_slab",
	"44": "stone_slab",
	"45": "brick_block",
	"46": "tnt",
	"47": "bookshelf",
	"48": "mossy_cobblestone",
	"49": "obsidian",
	"50": "torch",
	"51": "fire",
	"52": "mob_spawner",
	"53": "oak_stairs",
	"54": "chest",
	"55": "redstone_wire",
	"56": "diamond_ore",
	"57": "diamond_block",
	"58": "crafting_table",
	"59": "wheat",
	"60": "farmland",
	"61": "furnace",
	"62": "lit_furnace",
	"63": "standing_sign",
	"64": "wooden_door",
	"65": "ladder",
	"66": "rail",
	"67": "stone_stairs",
	"68": "wall_sign",
	"69": "lever",
	"70": "stone_pressure_plate",
	"71": "iron_door",
	"72": "wooden_pressure_plate",
	"73": "redstone_ore",
	"74": "lit_redstone_ore",
	"75": "unlit_redstone_torch",
	"76": "redstone_torch",
	"77": "stone_button",
	"78": "snow_layer",
	"79": "ice",
	"80": "snow",
	"81": "cactus",
	"82": "clay",
	"83": "reeds",
	"84": "jukebox",
	"85": "fence",
	"86": "pumpkin",
	"87": "netherrack",
	"88": "soul_sand",
	"89": "glowstone",
	"90": "portal",
	"91": "lit_pumpkin",
	"92": "cake",
	"93": "unpowered_repeater",
	"94": "powered_repeater",
	"95": "stained_glass",
	"96": "trapdoor",
	"97": "monster_egg",
	"98": "stonebrick",
	"99": "brown_mushroom_block",
	"100": "red_mushroom_block",
	"101": "iron_bars",
	"102": "glass_pane",
	"103": "melon_block",
	"104": "pumpkin_stem",
	"105": "melon_stem",
	"106": "vine",
	"107": "fence_gate",
	"108": "brick_stairs",
	"109": "stone_brick_stairs",
	"110": "mycelium",
	"111": "waterlily",
	"112": "nether_brick",
	"113": "nether_brick_fence",
	"114": "nether_brick_stairs",
	"115": "nether_wart",
	"116": "enchanting_table",
	"117": "brewing_stand",
	"118": "cauldron",
	"119": "end_portal",
	"120": "end_portal_frame",
	"121": "end_stone",
	"122": "dragon_egg",
	"123": "redstone_lamp",
	"124": "lit_redstone_lamp",
	"125": "double_wooden_slab",
	"126": "wooden_slab",
	"127": "cocoa",
	"128": "sandstone_stairs",
	"129": "emerald_ore",
	"130": "ender_chest",
	"131": "tripwire_hook",
	"132": "tripwire",
	"133": "emerald_block",
	"134": "spruce_stairs",
	"135": "birch_stairs",
	"136": "jungle_stairs",
	"137": "command_block",
	"138": "beacon",
	"139": "cobblestone_wall",
	"140": "flower_pot",
	"141": "carrots",
	"142": "potatoes",
	"143": "wooden_button",
	"144": "skull",
	"145": "anvil",
	"146": "trapped_chest",
	"147": "light_weighted_pressure_plate",
	"148": "heavy_weighted_pressure_plate",
	"149": "unpowered_comparator",
	"150": "powered_comparator",
	"151": "daylight_detector",
	"152": "redstone_block",
	"153": "quartz_ore",
	"154": "hopper",
	"155": "quartz_block",
	"156": "quartz_stairs",
	"157": "activator_rail",
	"158": "dropper",
	"159": "stained_hardened_clay",
	"160": "stained_glass_pane",
	"161": "leaves2",
	"162": "log2",
	"163": "acacia_stairs",
	"164": "dark_oak_stairs",
	"165": "slime",
	"166": "barrier",
	"167": "iron_trapdoor",
	"168": "prismarine",
	"169": "sea_lantern",
	"170": "hay_block",
	"171": "carpet",
	"172": "hardened_clay",
	"173": "coal_block",
	"174": "packed_ice",
	"175": "double_plant",
	"176": "standing_banner",
	"177": "wall_banner",
	"178": "daylight_detector_inverted",
	"179": "red_sandstone",
	"180": "red_sandstone_stairs",
	"181": "stone_slab2",
	"182": "double_stone_slab2",
	"183": "spruce_fence_gate",
	"184": "birch_fence_gate",
	"185": "jungle_fence_gate",
	"186": "dark_oak_fence_gate",
	"187": "acacia_fence_gate",
	"188": "spruce_fence",
	"189": "birch_fence",
	"190": "jungle_fence",
	"191": "dark_oak_fence",
	"192": "acacia_fence",
	"193": "spruce_door",
	"194": "birch_door",
	"195": "jungle_door",
	"196": "acacia_door",
	"197": "dark_oak_door",
	"198": "end_rod",
	"199": "none",
	"200": "chorus_flower",
	"201": "purpur_block",
	"202": "purpur_pillar",
	"203": "purpur_stairs",
	"204": "purpur_double_slab",
	"205": "purpur_slab",
	"206": "end_bricks",
	"208": "grass_path",
	"209": "end_gateway",
	"210": "repeating_command_block",
	"211": "chain_command_block",
	"212": "frosted_ice",
	"213": "magma",
	"214": "nether_wart_block",
	"215": "red_nether_brick",
	"216": "bone_block",
	"217": "structure_void",
	"218": "shulker_box",
	"219": "white_shulker_box",
	"220": "orange_shulker_box",
	"221": "magenta_shulker_box",
	"222": "light_blue_shulker_box",
	"223": "yellow_shulker_box",
	"224": "lime_shulker_box",
	"225": "pink_shulker_box",
	"226": "gray_shulker_box",
	"227": "silver_shulker_box",
	"228": "cyan_shulker_box",
	"229": "purple_shulker_box",
	"230": "blue_shulker_box",
	"231": "brown_shulker_box",
	"232": "green_shulker_box",
	"233": "red_shulker_box",
	"234": "black_shulker_box",
	"235": "white_glazed_terracotta",
	"236": "orange_glazed_terracotta",
	"237": "magenta_glazed_terracotta",
	"238": "light_blue_glazed_terracotta",
	"239": "yellow_glazed_terracotta",
	"240": "lime_glazed_terracotta",
	"241": "pink_glazed_terracotta",
	"242": "gray_glazed_terracotta",
	"243": "silver_glazed_terracotta",
	"244": "cyan_glazed_terracotta",
	"245": "purple_glazed_terracotta",
	"246": "blue_glazed_terracotta",
	"247": "brown_glazed_terracotta",
	"248": "green_glazed_terracotta",
	"249": "red_glazed_terracotta",
	"250": "black_glazed_terracotta",
	"251": "concrete",
	"252": "concrete_powder",
	"255": "structure_block",
}

def remove_file(file_name):
	if file_exist(file_name):
		os.remove(file_name)

def file_exist(file_name):
	return os.path.isfile(file_name)

displayName = "Structure to function v2.0"

def cmdBlockTileEntity(cmd,x=None,y=None,z=None):
	control = TAG_Compound()
	control["Command"] = TAG_String(cmd)
	control["id"] = TAG_String("Control")
	if not x == None:
		control["z"] = TAG_Int(z)
		control["y"] = TAG_Int(y)
		control["x"] = TAG_Int(x)
	 
	return control

def signBlockTileEntity(line,text,x=None,y=None,z=None):
	control = TAG_Compound()
	control["Text" + str(line)] = TAG_String(text)
	control["id"] = TAG_String("Sign")
	if not x == None:
		control["z"] = TAG_Int(z)
		control["y"] = TAG_Int(y)
		control["x"] = TAG_Int(x)
	 
	return control

def idToName(inputid):
	global names

	if str(inputid) in names:
		return names[str(inputid)]

	# Default if not found in the list
	return 'BLOCKNOTFOUND:' + str(inputid)

groupedblocks = ' '
highestCoords = [-9999999, -9999999, -9999999]

def checkAround(x, y, z, level, box):
	checkFor = level.blockAt(x, y, z)
	checkForData = level.blockDataAt(x, y, z)

	# curgrouped should be like so when used: [x1, y1, z1, x2, y2, z2]
	curgrouped = []
	alreadyChoseDir = 'false'

	if level.blockAt(x+1, y, z) == checkFor and level.blockDataAt(x+1, y, z) == checkForData and '&'+str(x+1)+','+str(y)+','+str(z)+'&' not in groupedblocks and alreadyChoseDir == 'false':
		curgrouped = checkLinear(x, y, z, 1, 0, 0, level, box)
		alreadyChoseDir = 'true'
	if level.blockAt(x-1, y, z) == checkFor and level.blockDataAt(x-1, y, z) == checkForData and '&'+str(x-1)+','+str(y)+','+str(z)+'&' not in groupedblocks and alreadyChoseDir == 'false':
		curgrouped = checkLinear(x, y, z, -1, 0, 0, level, box)
		alreadyChoseDir = 'true'
	if level.blockAt(x, y+1, z) == checkFor and level.blockDataAt(x, y+1, z) == checkForData and '&'+str(x)+','+str(y+1)+','+str(z)+'&' not in groupedblocks and alreadyChoseDir == 'false':
		curgrouped = checkLinear(x, y, z, 0, 1, 0, level, box)
		alreadyChoseDir = 'true'
	if level.blockAt(x, y-1, z) == checkFor and level.blockDataAt(x, y-1, z) == checkForData and '&'+str(x)+','+str(y-1)+','+str(z)+'&' not in groupedblocks and alreadyChoseDir == 'false':
		curgrouped = checkLinear(x, y, z, 0, -1, 0, level, box)
		alreadyChoseDir = 'true'
	if level.blockAt(x, y, z+1) == checkFor and level.blockDataAt(x, y, z+1) == checkForData and '&'+str(x)+','+str(y)+','+str(z+1)+'&' not in groupedblocks and alreadyChoseDir == 'false':
		curgrouped = checkLinear(x, y, z, 0, 0, 1, level, box)
		alreadyChoseDir = 'true'
	if level.blockAt(x, y, z-1) == checkFor and level.blockDataAt(x, y, z-1) == checkForData and '&'+str(x)+','+str(y)+','+str(z-1)+'&' not in groupedblocks and alreadyChoseDir == 'false':
		curgrouped = checkLinear(x, y, z, 0, 0, -1, level, box)
		alreadyChoseDir = 'true'

	# At this point, curgrouped should be set like so: [x1, y1, z1, x2, y2, z2] (the same as stated above)
	# This array of coordinates will be checked by in the main function and will
	# decide whether to make a command or not by checking its length.
	return curgrouped

def checkLinear(x, y, z, xdir, ydir, zdir, level, box):
	checkFor = level.blockAt(x, y, z)
	checkForData = level.blockDataAt(x, y, z)

	global groupedblocks
	global highestCoords

	# groupStart and groupEnd are the corners of the group
	groupStart = [x, y, z]
	groupEnd = [x, y, z]

	multfactor = 1
	extending = 'true'

	while extending == 'true':
		if xdir == 1:
			if level.blockAt(x+(xdir*multfactor), y, z) == checkFor and level.blockDataAt(x+(xdir*multfactor), y, z) == checkForData and x+(xdir*multfactor) >= box.minx and x+(xdir*multfactor) < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				groupEnd = [x+(xdir*multfactor), y, z]
				multfactor = multfactor + 1
			else:
				extending = 'false'
		if xdir == -1:
			if level.blockAt(x+(xdir*multfactor), y, z) == checkFor and level.blockDataAt(x+(xdir*multfactor), y, z) == checkForData and x+(xdir*multfactor) >= box.minx and x+(xdir*multfactor) < box.maxx and y >= box.miny and y < box.maxy and z >= box.minz and z < box.maxz:
				groupEnd = [x+(xdir*multfactor), y, z]
				multfactor = multfactor + 1
			else:
				extending = 'false'
		if ydir == 1:
			if level.blockAt(x, y+(ydir*multfactor), z) == checkFor and level.blockDataAt(x, y+(ydir*multfactor), z) == checkForData and x >= box.minx and x < box.maxx and y+(ydir*multfactor) >= box.miny and y+(ydir*multfactor) < box.maxy and z >= box.minz and z < box.maxz:
				groupEnd = [x, y+(ydir*multfactor), z]
				multfactor = multfactor + 1
			else:
				extending = 'false'
		if ydir == -1:
			if level.blockAt(x, y+(ydir*multfactor), z) == checkFor and level.blockDataAt(x, y+(ydir*multfactor), z) == checkForData and x+(xdir*multfactor) >= box.minx and x < box.maxx and y+(ydir*multfactor) >= box.miny and y+(ydir*multfactor) < box.maxy and z >= box.minz and z < box.maxz:
				groupEnd = [x, y+(ydir*multfactor), z]
				multfactor = multfactor + 1
			else:
				extending = 'false'
		if zdir == 1:
			if level.blockAt(x, y, z+(zdir*multfactor)) == checkFor and level.blockDataAt(x, y, z+(zdir*multfactor)) == checkForData and x+(xdir*multfactor) >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z+(zdir*multfactor) >= box.minz and z+(zdir*multfactor) < box.maxz:
				groupEnd = [x, y, z+(zdir*multfactor)]
				multfactor = multfactor + 1
			else:
				extending = 'false'

		if zdir == -1:
			if level.blockAt(x, y, z+(zdir*multfactor)) == checkFor and level.blockDataAt(x, y, z+(zdir*multfactor)) == checkForData and x+(xdir*multfactor) >= box.minx and x < box.maxx and y >= box.miny and y < box.maxy and z+(zdir*multfactor) >= box.minz and z+(zdir*multfactor) < box.maxz:
				groupEnd = [x, y, z+(zdir*multfactor)]
				multfactor = multfactor + 1
			else:
				extending = 'false'

		# Adds the newest block to the groupedblock string to track all of them
		groupedblocks = groupedblocks + '&'+str(groupEnd[0])+','+str(groupEnd[1])+','+str(groupEnd[2])+'&'
		if groupEnd[0] > highestCoords[0]:
			highestCoords[0] = groupEnd[0]
		if groupEnd[1] > highestCoords[1]:
			highestCoords[1] = groupEnd[1]
		if groupEnd[2] > highestCoords[2]:
			highestCoords[2] = groupEnd[2]

	if len(groupStart) == 3 and len(groupEnd) == 3:
		return [groupStart[0], groupStart[1], groupStart[2], groupEnd[0], groupEnd[1], groupEnd[2]]
	else:
		return []

def tagToNBT(entity):

	curNBT = ' '

	for attr, value in entity.iteritems():
		print attr, value

		curNBT += ',' + str(attr) + ':' + str(value)

	curNBT = curNBT.replace(',', ' ', 1)

	return curNBT

def split_file(filepath, lines_per_file=10000):
	lpf = lines_per_file
	path, filename = os.path.split(filepath)
	with open(filepath, 'r') as r:
		name, ext = os.path.splitext(filename)
		try:
			w = open(os.path.join(path, '{}_{}{}'.format(name, 0, ext)), 'w')
			for i, line in enumerate(r):
				if not i % lpf:

					w.close()
					filename = os.path.join(path,'{}_{}{}'.format(name, i, ext))
					w = open(filename, 'w')
				w.write(line)
		finally:
			w.close()

def generateStructure(cmds):
	path = script_path+"/structures/structure.mcfunction"
	with open(path, 'w') as output:
		for line in cmds:
			output.write(line.replace("    ","").replace("  ","\n").replace(" set", "\nset"))
	split_file(path, 10000)

def perform(level, box, options):
	blocks = []
	isFill = []
	posx = []
	posy = []
	posz = []

	depblocks = []
	depisFill = []
	depposx = []
	depposy = []
	depposz = []

	curblock = ' '
	curdamage = ' '
	tryGroup = []

	entitycommands = ' ';

	dependentBlocks = [27, 28, 66, 157, 171, 78, 55, 93, 94, 149, 68, 63, 143, 77]

	global groupedblocks
	global highestCoords

	for y in xrange(box.miny, box.maxy):
		for x in xrange(box.minx, box.maxx):
			for z in xrange(box.minz, box.maxz):
				if level.blockAt(x, y, z) !=0 and level.blockAt(x, y, z) !=1 and '&'+str(x)+','+str(y)+','+str(z)+'&' not in groupedblocks:
					# Optimize by using /fill wherever it can
					tryGroup = checkAround(x, y, z, level, box)
					if len(tryGroup) > 0:
						# Was able to group nearby blocks

						# Adds the name and damage of the block, for example: 'quartz_block 2'
						curblock = idToName(level.blockAt(x, y, z))

						if 'blocknotfound' not in curblock:
							curdamage = str(level.blockDataAt(x, y, z))

							blocks.append('fill '+str(tryGroup[0])+' '+str(tryGroup[1])+' '+str(tryGroup[2])+' '+str(tryGroup[3])+' '+str(tryGroup[4])+' '+str(tryGroup[5])+' ' +curblock + ' ' + curdamage)
							isFill.append('true')
							print 'fill '+str(tryGroup[0])+' '+str(tryGroup[1])+' '+str(tryGroup[2])+' '+str(tryGroup[3])+' '+str(tryGroup[4])+' '+str(tryGroup[5])+' ' +curblock + ' ' + curdamage
							# Keeps the coordinates in parallel arrays
							posx.append(0)
							posy.append(0)
							posz.append(0)
					else:
						# Wasn't able to group nearby blocks

						# Adds the name and damage of the block, for example: 'quartz_block 2'
						curblock = idToName(level.blockAt(x, y, z))

						if 'blocknotfound' not in curblock:
							curdamage = str(level.blockDataAt(x, y, z))

							blocks.append(curblock + ' ' + curdamage)
							isFill.append('false')

							# Keeps the coordinates in parallel arrays
							posx.append(x - box.minx)
							posy.append(y - 3 - box.miny)
							posz.append(z - box.minz)

							groupedblocks = groupedblocks + '&'+str(x)+','+str(y)+','+str(z)+'&'

	initCmdStrings = []
	initCmdStrings.append(' ')
	currentCommand = 0
	armorStandPlaced = 'false'

	for i in range(0, len(depblocks)):
		blocks.append(depblocks[i]);
		isFill.append(depisFill[i]);
		posx.append(depposx[i]);
		posy.append(depposy[i]);
		posz.append(depposz[i]);

	for i in range(0, len(blocks)):
		if isFill[i] == 'false':
			if len(initCmdStrings[currentCommand] + 'setblock '+str(posx[i]+1)+' '+str(posy[i])+' '+str(posz[i])+' '+blocks[i]+' ') + 528 > 32300:
				currentCommand = currentCommand + 1
				initCmdStrings.append(' ')
			initCmdStrings[currentCommand] = initCmdStrings[currentCommand] + 'setblock '+str(posx[i]+1)+' '+str(posy[i])+' '+str(posz[i])+' '+blocks[i]+' '
		else:
			if len(initCmdStrings[currentCommand] + ' '+blocks[i]+' ') + 528 > 32300:
				currentCommand = currentCommand + 1
				initCmdStrings.append(' ')
			initCmdStrings[currentCommand] = initCmdStrings[currentCommand] + ' '+blocks[i]+' '

		if i == len(blocks) - 1:
			initCmdStrings[currentCommand] = initCmdStrings[currentCommand] + ' '

	cmds = []
	# This puts the initCmdStrings each into their own final command.
	# The final commands are all in the cmds[] array
	executeForMult = ' '
	appendEntityCmds = ' '
	for i in range(0, len(initCmdStrings)):
		executeForMult = ' '

		if i == 0:
			appendEntityCmds = entitycommands
		else:
			appendEntityCmds = ' '

		# Regular
		cmds.append(executeForMult + ' ' + initCmdStrings[i] + appendEntityCmds + ' ')
	generateStructure(cmds)
