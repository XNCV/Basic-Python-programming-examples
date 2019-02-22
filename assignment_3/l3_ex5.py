def generate_autocomplete(words):
	# Create the set of the keys
	set_of_keys = []
	for word in words:
		key = ''
		for character in word:
			key = key + character
			set_of_keys.append(key)
	# Create the set of the keys with one time appeared
	set_of_keys = set(set_of_keys)
	# Create the autocomplete results
	dic_out = {}
	for key in set_of_keys:
		dic_out[key] = []
		for word in words:
			# If the word begin by key, we will chose this word
			if key == word[0:len(key)]:
				dic_out[key].append(word)
		# Stransfer srom list type to set type
		dic_out[key] = set(dic_out[key])
	return dic_out


print(generate_autocomplete(['a', 'abc', 'abd', 'abd', 'b']))
