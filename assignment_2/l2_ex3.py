def right_triangle(a, b, c):
	if a**2 == (b**2 + c**2) or b**2 == (a**2 + c**2) or c**2 == (a**2 + b**2):
		return('True')
	else:
		return('False')


print(right_triangle(17, 15, 8))
