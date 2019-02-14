def print_tab(array):
	array_sort = array
	array_sort.sort(key=len)
	if len(array_sort) > 0:
		num_column = len(array_sort[len(array_sort) - 1])
		if num_column > 0:
			list_of_len = []
			for i in range(num_column):
				size = 0
				for j in range(len(array)):
					if i < len(array[j]):
						if len(array[j][i]) > size:
							size = len(array[j][i])
				list_of_len.append(size)
			size_column = (sum(list_of_len) + num_column*3 + 1)
			string_out = ''
			for i in range(len(array)*2 + 1):
				if i % 2 == 0:
					string_out = string_out + size_column*'+' + '\n'
				else:
					line = ''
					for j in range(len(array[i//2])):
						line = line + '+ ' + array[i//2][j] + (list_of_len[j] - len(array[i//2][j]) + 1)*' '
					if len(line) < (size_column - 1):
						line = line + (size_column - len(line) - 1)*' '
					string_out = string_out + line + '+' + '\n'
		else:
			string_out = (len(array)*2 + 1)*'++\n'
	else:
		string_out = '++\n++'
	return string_out


print(print_tab([["this"], ["~~", "is", "~~"], ["ah!", "oh!", "kind", "", "eh !"], ["1", "2", "3", "of"], ["...", "...", "...", "...", "fun !"]]))
# print(print_tab([]))
# print(print_tab([[], []]))
