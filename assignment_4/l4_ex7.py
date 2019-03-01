# I dont have the function special_sort
# So I created my own function, but it dont meet the need
import sorts

# Create a list
lis = []
while True:
	string_in = input()
	if string_in == '':
		break
	else:
		lis.append(string_in)
# Catch the only exception RuntimeError 
# when the special_sort function raises it
try:
	print(sorts.special_sort(lis))
except RuntimeError:
	print('I catch a RuntimeError')
