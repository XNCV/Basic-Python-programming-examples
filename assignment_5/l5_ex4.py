import l5_ex3


def fibonacci_generator():
	n = 0
	while(True):
		yield(l5_ex3.fibonacci(n))
		n = n + 1


fibo_gen = fibonacci_generator()
for i in range(12):
	print(next(fibo_gen))
