def loads(s):
	# Create the list of the elements, the elements contain the keys, 
	# the contents of the keys and special elements (:\\n, \\n, :)
	# Change the elements :\\n firstly to avoid changing when replace \\n
	s = s.replace(':\\n', ' :: ')
	# Replace \\n by itself and two white space before and after it
	s = s.replace('\\n', ' \\n ')
	# Recreate the elements :\\n
	s = s.replace('::', ':\\n')
	# Replace the elements : by simalar way with the elements \\n
	s = s.replace(': ', ' : ')
	# The created white spaces are used for splitting to create the list
	s = s.split()

	# However, the elements liked "Tinh dep trai" need to be contained 
	# in only one element of the list. We create the list s_new to meet this need
	s_new = []
	# The speacial elements will interleave the normal elements (keys and contents)
	# The variable num will plus 1 when the loop pass a normal element
	num = 0
	for i in range(len(s)):
		# The special elements are the flag to add the elements passed to 
		# the new list and the variable num counts the elements to need to be
		# contained in only one element of this one.
		if(s[i] == ':' or s[i] == ':\\n' or s[i] == '\\n') and num > 1:
			string = s[i-num]
			for j in range(num-1, 0, -1):
				string = string + ' ' + s[i-j]
			s_new.append(string)
			num = 0
			s_new.append(s[i])
		elif(s[i] == ':' or s[i] == ':\\n' or s[i] == '\\n'):
			num = 0
			s_new.append(s[i-1])
			s_new.append(s[i])
		else:
			num = num + 1
	# The last element doesnt have any flats to be added. So we need add it.
	string = s[-num]
	for j in range(num-1, 0, -1):
		string = string + ' ' + s[-j]
	s_new.append(string)
	
	# The idea is create the dictionary in order from inside to outside
	# The variable dic is used for creating the new layer contained the old
	# layers dic_old
	dic = {}
	dic_old = {}
	control = False
	for i in range(-1, -len(s_new)-1, -1):
		# Create the new layer if the condition is true
		if control:
			dic_old = dic
			control = False
			dic = {}
		# The element : is the flag to create one pair (key and contain)
		if s_new[i] == ':':
			dic_old[s_new[i-1]] = s_new[i+1]
		# The element :\\n is the flag to create the new layer
		elif s_new[i] == ':\\n':
			control = True
			dic[s_new[i-1]] = dic_old
	return dic_old
	

string = 'nest:\\n  ted:\\n    dict: ionary'
print(loads(string))
