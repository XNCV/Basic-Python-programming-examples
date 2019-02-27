def itranslate(dic, string):
	# split the string in order to use keys
	string = string.split()
	translated_string = ''
	n = 0
	# The string for output is created by using add string
	for word in string:
		n = n + 1
		if word in dic.keys():
			if n < len(string):
				translated_string = translated_string + dic[word] + ' '
			else:
				translated_string = translated_string + dic[word]
		else:
			# The word isnt included in dictionary
			raise KeyError('Missing word %s' % (word))
			break
	return translated_string


print(itranslate({"pain": "bread", "le": "the", "bon": "good", "est": "is"}, 'le pain est bon'))
