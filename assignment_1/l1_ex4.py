size = int(input())
charaters = input()
if(size <= 0):
	print('Invalid value')
elif(size == 1):
	print(charaters[0])
else:
	# The first line
	print(charaters[0] + (size - 2)*charaters[1] + charaters[0])
	# The next lines
	for _ in range(size - 2):
		print(charaters[3] + (size - 2)*' ' + charaters[4])
	# The final line
	print(charaters[0] + (size - 2)*charaters[2] + charaters[0])
