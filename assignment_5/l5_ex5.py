# I think that I really meet the trouble with recursion
# I dont know how to think logically

def integer_partition(n):
	if n == 1:
		return {(1,)}
	else:
		list_set = {(n,)}
		for i in range(1, n//2 + 1):
			par = integer_partition(n - i)
			if type(par) is set:
				for element in par:
					hey_you = (i,) + element
					hey_you = tuple(sorted(hey_you))
					list_set.add(hey_you)
			else:
				list_set = {tuple(sorted((i,) + par))}
		return list_set


print(integer_partition(4))
