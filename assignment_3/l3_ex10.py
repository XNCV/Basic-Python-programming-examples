def loads(s):
	s = s.replace(':\\n', ' :: ')
	s = s.replace('\\n', ' \\n ')
	s = s.replace('::', ':\\n')
	s = s.replace(': ', ' : ')
	s = s.split()
	# print(s)
	s_new = []
	num = 0
	for i in range(len(s)):
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
	string = s[-num]
	for j in range(num-1, 0, -1):
		string = string + ' ' + s[-j]
	s_new.append(string)
	# print(s_new)
	dic = {}
	dic_old = {}
	control = False
	for i in range(-1, -len(s_new)-1, -1):
		if control:
			dic_old = dic
			control = False
			dic = {}
		if s_new[i] == ':':
			dic_old[s_new[i-1]] = s_new[i+1]
		elif s_new[i] == ':\\n':
			control = True
			dic[s_new[i-1]] = dic_old
	return dic_old
	

string = 'nest:\\n  ted:\\n    dict: ionary'
print(loads(string))
