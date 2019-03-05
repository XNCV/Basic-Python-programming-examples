# I dont really known the funtion that transfer 
# the number in the first five examples
def int2base(number, base='0123456789'):
	count_control = False
	for character in base:
		if base.count(character) > 1:
			count_control = True
	if base == '0123456789':
		return str(number)
	elif base == '01':
		return bin(number)[2:]
	# elif base == 'qwertyuiopasdfghjklz':
	# 	pass
	# elif base == '):':
	# 	pass
	elif len(base) < 2:
		raise ValueError('The length of base must be >= 2.')
	elif count_control:
		raise ValueError('The base must be composed of unique characters.')
	elif '-' in base:
		raise ValueError('\'-\' is not a valid character for the base.')


print(int2base(-23, base='0'))
