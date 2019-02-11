number = int(input('How many squares do you need? \n'))
size = (number - 1)*4 + 3
# Print the half top square
for i in range(number*2 - 1):
	if i % 2 == 0:
		line = '# '*(i//2) + (size - (i//2)*4)*'#' + ' #'*(i//2)
		print(line)
	else:
		line = '# '*(i//2 + 1) + (size - (i//2 + 1)*4)*' ' + ' #'*(i//2 + 1)
		print(line)
# Print the center line
linecenter = '# '*(size//2) + '#'
print(linecenter)
# Print the half down square
# because of range(5, 1, -1) -> 5 4 3 2, I used the folowing function
for i in range(number*2 - 2, -1, -1):
	if i % 2 == 0:
		line = '# '*(i//2) + (size - (i//2)*4)*'#' + ' #'*(i//2)
		print(line)
	else:
		line = '# '*(i//2 + 1) + (size - (i//2 + 1)*4)*' ' + ' #'*(i//2 + 1)
		print(line)
