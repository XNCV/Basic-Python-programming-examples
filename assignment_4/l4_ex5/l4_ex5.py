def concat_files(*names):
	str_out = ''
	# The string for the output is created by adding the strings in file name
	for name in names:
		try:
			file = open(name, 'r')
			str_out = str_out + file.read()
			file.close()
		# If this file doesnt exist, please ignor it
		except FileNotFoundError:
			pass
	try:
		concat_file = open('concatenated_files', 'w')
	except FileNotFoundError:
		# If this file doesnt exist, create it
		concat_file = open('concatenated_files', 'w+')
	concat_file.write(str_out)
	concat_file.close()


concat_files("toto", "tutu", "titi")
