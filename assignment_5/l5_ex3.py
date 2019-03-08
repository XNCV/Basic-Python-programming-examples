# I refered the script at
# https://www.techbeamers.com/python-program-fibonacci-sequence-using-recursion/


def fibonacci(n):
	if n <= 1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))


print(fibonacci(4))
