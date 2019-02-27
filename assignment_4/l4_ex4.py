def french_rap(csv):
	try:
		# Read file IO
		file = open(csv, 'r')
		string_content = file.read()
		file.close()
		# Split the lines
		string_content = string_content.split('\n')
		string_content.remove('')
		# Create the dictionary
		dictionary = {}
		for pair in string_content:
			lis = pair.split(',')
			if lis[1] not in dictionary.keys():
				dictionary[lis[1]] = [lis[0]]
			else:
				dictionary[lis[1]].append(lis[0])
		return dictionary
	except FileNotFoundError:
		raise FileNotFoundError('File does not exist')


print(french_rap('test_ex4.csv'))
