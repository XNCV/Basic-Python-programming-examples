# NOT DONE
def numbers_cor_letters(n, list_used):
	if n > 0:
		list_prep = list_used
		for i in range(0, 10):
			print(n)
			list_iteration = list_prep
			if i not in list_used:
				list_iteration.append(i)
				yield from numbers_cor_letters(n-1, list_iteration)
			print(list_prep)
	else:
		print(n)
		yield list_used



def solve_cruptarithm(op1, op2, sum_op):
	list_letters = set(op1).union(set(op2).union(sum_op))
	num_letters = len(list_letters)
	my_list_num = numbers_cor_letters(num_letters, [])
	for lis in my_list_num:
		pass
	return list_letters

# print(solve_cruptarithm("SEND", "MORE", "MONEY"))
my_list_num = numbers_cor_letters(2, [])
for i in my_list_num:
	pass
