def merge_dict(dictionaries):
	# Create the list of the keys
	list_of_keys = []
	for dic in dictionaries:
		for key in dic.keys():
			if key not in list_of_keys:
				list_of_keys.append(key)
	list_of_keys.sort()
	# Create the merged dictionary
	dictionary = {}
	for key in list_of_keys:
		dictionary[key] = []
		for dic in dictionaries:
			# Check the key in each dictionary
			if key in dic.keys():
				dictionary[key].append(dic[key])
	return dictionary


print(merge_dict([{'a': 1, 'b': 2, 'c': 1, 'd': 2},
	{'e': 1, 'f': 2, 'b': 1, 'g': 2}, {'h': 1, 'i': 2, 'd': 1, 'b': 2}]))
