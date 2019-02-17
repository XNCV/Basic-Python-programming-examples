def sed(command, s):
	string1 = ''
	string2 = ''
	control = 0
	for i in command:
		if i == '/':
			control = control + 1
			continue
		if control == 1:
			string1 = string1 + i
		elif control == 2:
			string2 = string2 + i
	string_out = s
	if command[0] == 's':
		string_out = string_out.replace(string1, string2)

	elif command[0] == 'y':
		for i in range(len(string1)):
			string_out = string_out.replace(string1[i], string2[i])
		# for i in s:
		# 	character = i
		# 	for j in range(len(string1)):
		# 		if character == string1[j]:
		# 			character = string2[j]
		# 	string_out = string_out + character
	return string_out

print(sed('y/aeo/430/', 'hello mr wayne'))
print(sed('s/morning/evening/g', 'Good morning'))
