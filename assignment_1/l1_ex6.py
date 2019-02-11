while True:
	string = input('repl> ')
	n = len(string)
	if string == 'quit':
		break
	elif n == 6:
		print('My length is 6')
	elif string[0] == 'a' or string[0] == 'e' or string[0] == 'i' or string[0] == 'o' or string[0] == 'u':
		for i in range(4):
			print(string[1:4])
	elif string == 'ls' or string == 'cat' or string == 'rev' or string == 'pwd':
		print('I know the command ', string)
	elif string[0] == '0' and string[n-1] != '9':
		for i in range(n):
			if string[i] >= '0' and string[i] <= '9':
				print(string[i])
	# else:
	# 	pass
