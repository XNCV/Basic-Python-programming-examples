def are_ships_destroyed(ships_map, hits_map):
	for i in range(len(ships_map)):
		if(ships_map[i] == 'B' and hits_map[i] != 'X'):
			return False
	else:
		return True

# The script for testing
ships_map = '............\n.....BBB....\n............\nB...........'
hits_map = '............\n......XX....\n............\nX...........'
print(are_ships_destroyed(ships_map, hits_map))
