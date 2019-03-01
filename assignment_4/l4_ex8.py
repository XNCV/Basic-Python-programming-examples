def rotx(message, rot=13):
	# Create the string for the output
	string_out = ''
	for char in message:
		dif = ord(char) + rot
		# A is 65th letter in ascii, Z is 90
		if char >= 'A' and char <= 'Z':
			# Range(a, b) = {a, ..., b - 1}
			if dif in range(65, 91):
				string_out = string_out + chr(dif)
			else:
				string_out = string_out + chr(65 + (dif - 91))
		# a is 97th letter in ascii, z is 122th
		elif char >= 'a' and char <= 'z':
			if dif in range(97, 123):
				string_out = string_out + chr(dif)
			else:
				string_out = string_out + chr(97 + (dif - 123))
		# The special letter is not changed
		else:
			string_out = string_out + char
	return string_out


print(rotx("Toan is a great cook!"))
