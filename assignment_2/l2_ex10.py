def html_parser(html):
	string_out = ''
	# If the variable control = True, print the character
	# else no print
	control = False
	for i in html:
		if i == '>':
			control = True
			# Move to next loop to avoid printing the character >
			continue
		elif i == '<':
			control = False
		if control:
			string_out = string_out + i
	return string_out


print(html_parser("<html><head><title>Page Title</title></head><body><p>My first <i>paragraph</i>.</p></body></html>"))
