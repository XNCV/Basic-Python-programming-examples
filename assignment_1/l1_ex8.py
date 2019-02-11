number = int(input('Let\'s print the prime numbers up to? '))
for i in range(2, number):
	# If you are a perfectionist, you need use function sqrt()
	# for the variable 'limit' and import the library 'math'
	limit = i // 2 + 1
	for n in range(2, limit, 1):
		if (i % n) == 0:
			break
	else:
		print(i)
