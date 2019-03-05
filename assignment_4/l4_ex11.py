import os

def ls(term_width):
	# Get the direct path
	directory_of_path = os.getcwd()
	# Create the list of the files in this path
	list_files = os.listdir(directory_of_path)
	list_files.sort()
	len_num_file = len(list_files)
	# Create the list of the length name
	list_len = []
	for name in list_files:
		list_len.append(len(name))
	string = ''
	# One column
	if max(list_len) > term_width:
		for i in range(len_num_file):
			if list_len[i] > term_width:
				string = string + list_files[i][0:term_width] + '\n'
				string = string + list_files[i][term_width:] + '\n'
			else:
				string = string + list_files[i]
	else:
		# Find the accomondate number of the column and the row
		for i in range(1, len_num_file+1):
			if len_num_file % i == 0:
				num_column = len_num_file // i
			else:
				num_column = (len_num_file//i) + 1
			lis_of_lis_column = []
			lis_len_max = []
			for j in range(num_column):
				lis_len_each_column = []
				for k in range(i):
					if (j*i + k) < len_num_file:
						lis_len_each_column.append(list_len[j*i + k])
				else:
					lis_len_max.append(max(lis_len_each_column))
				lis_of_lis_column.append(lis_len_each_column)
			# If the number of the columns is comfortable, break
			if sum(lis_len_max) + (num_column-1) < term_width:
				num_row = i
				break
		string = ''
		# Create the string for output
		for i in range(num_row):
			line = ''
			for j in range(num_column):
				if j < (num_column - 1) and (j*num_row + i) < len_num_file:
					line = line + list_files[j*num_row + i] + ' '*(lis_len_max[j] - len(list_files[j*num_row + i]) + 1)
				elif j == (num_column - 1) and (j*num_row + i) < len_num_file:
					line = line + list_files[j*num_row + i]
			else:
				line = line + '\n'
			string = string + line
	return string


print(ls(50))
