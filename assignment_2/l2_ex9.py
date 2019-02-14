def basic_grep(text, string):
	handled_string = ''
	# Remove the special character $ and ^ in string
	for character in string:
		if character != '$' and character != '^':
			handled_string = handled_string + character
	list_of_text = []
	character = ''
	# Create the list of the lines in the text
	for i in text:
		if i == '\n':
			list_of_text.append(character)
			character = ''
		else:
			character = character + i
	# Because there is not '\n' in the end of text, we
	# add the final line to list by using for... else...
	else:
		list_of_text.append(character)
	list_out = []
	# Find the lines have the string handled
	for element in list_of_text:
		if handled_string in element:
			list_out.append(element)
	return list_out


print(basic_grep("Hellow\nPotato\nMellow", "ow$"))
