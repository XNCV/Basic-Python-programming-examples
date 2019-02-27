def right_triangle_errors(a, b, c):
	# Check edges
	if (type(a) is int) and (type(b) is int) and (type(c) is int) and a > 0 and b > 0 and c > 0:
		# Check that is this a right triagle
		if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
			return True
		else:
			return False
	else:
		# If you wanna show the Error, you need use raise
		raise ValueError('Incorrect value')


print(right_triangle_errors(17, -5, 5))
