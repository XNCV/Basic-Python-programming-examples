def generate_table(s):
	# Create the list of words in order
	list_of_words = s.split()
	# Create the set of the keys
	set_of_keys = set(list_of_words)
	# Create the output dictionary
	dic_out = {}
	for key in set_of_keys:
		dic_out[key] = {}
		for i in range(len(list_of_words)):
			# If the word equals to key and the value (i + 1) is fewer than the length of the list
			# of word (use this to ignor the last word of the sentence)
			if list_of_words[i] == key and (i+1) < len(list_of_words):
				# If the next word havent appeared yet, its value would have equaled to 1
				# vice versa, the one need plus 1
				if list_of_words[i+1] not in dic_out[key].keys():
					dic_out[key][list_of_words[i+1]] = 1
				else:
					dic_out[key][list_of_words[i+1]] = dic_out[key][list_of_words[i+1]] + 1
	return dic_out


print(generate_table('i am daniel i am french i like jiu-jitsu'))
