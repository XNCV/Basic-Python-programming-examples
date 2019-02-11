size = int(input())
charaters = input()
if(size <= 0):
	print('Invalid value')
elif(size == 1):
	print(charaters[0])
else:
	# The first line
	add = ''
	for i in range(size - 2):
		add = add + charaters[1]
	line = charaters[0] + add + charaters[0]
	print(line)
	# The next line
	add = ''
	for i in range(size - 2):
		add = add + ' '
	line = charaters[3] + add + charaters[4]
	for i in range(size - 2):
		print(line)
	# The final line
	add = ''
	for i in range(size - 2):
		add = add + charaters[2]
	line = charaters[0] + add + charaters[0]
	print(line)
