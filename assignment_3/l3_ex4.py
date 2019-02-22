def bdmi(dic):
	# Create the sets of actors
	sets_of_actors = []
	for key in dic.keys():
		for actor in dic[key]:
			sets_of_actors.append(actor)
	sets_of_actors = set(sets_of_actors)
	# Find the movies with each actor
	dic_out = {}
	for actor in sets_of_actors:
		dic_out[actor] = []
		for key in dic.keys():
			if actor in dic[key]:
				dic_out[actor].append(key)
	return dic_out


print(bdmi({'The Godfather': ['Marlon Brando', 'Al Pacino'], 'Scarface': ['Al Pacino', 'Michelle Pfeiffer']}))
