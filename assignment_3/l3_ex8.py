def find_diff(d1, d2):
	# Create the list of the keys (the value of each must equal to "b")
	list_of_d1 = []
	list_of_d2 = []
	for key in d1.keys():
		if d1[key] == "b":
			list_of_d1.append(key)
		else:
			for key_in in d1[key].keys():
				list_of_d1.append(key + ':' + key_in)
	# The same with d2
	for key in d2.keys():
		if d2[key] == "b":
			list_of_d2.append(key)
		else:
			for key_in in d2[key].keys():
				list_of_d2.append(key + ':' + key_in)
	# Use sets minus sets to attract the difference between two list of the keys
	set_of_difference = (set(list_of_d1) - set(list_of_d2))
	# Print the result to meet the need
	for key_diff in set_of_difference:
		print('Key ' + key_diff + ' not in d2')


find_diff({'to': "b", 'ti': "b", 'tu': "b", 'te': {'tre': "b"}}, {'to': "b", 'tu': "b", 'te': "b"})
