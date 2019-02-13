def to_l33t(stringfix):
	string = ''
	for s in stringfix:
		if s == 'a' or s == 'A':
			string += '4'
		elif s == 'e' or s == 'E':
			string += '3'
		elif s == 'i' or s == 'I':
			string += '1'
		elif s == 'o' or s == 'O':
			string += '0'
		elif s == 'u' or s == 'U':
			string += '8'
		else:
			string += s
	return(string)


print(to_l33t("leetspeak, DUDE !"))