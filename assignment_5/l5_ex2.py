# Easy task
def factorial(n):
	if n == 0:
		return 1
	else:
		result = 1
		for i in range(1, n + 1):
			result = result * i
		return result


print(factorial(10))
