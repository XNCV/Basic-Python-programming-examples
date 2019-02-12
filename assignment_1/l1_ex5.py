size = int(input('What pyramid size do you want?\n'))
if size % 2 == 0:
	size = size - 1
for i in range(size//2 + 1):
	print((size//2 - i)*' ' + (2*(i + 1) - 1)*'#')
