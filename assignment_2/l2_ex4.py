def compact(parameter):
	n = 0
	for string in parameter:
		if string == None:
			parameter.pop(n)
		n = n + 1
	return(parameter)


print(compact(["toto", "mathieu", None, "Laurie", "DaNiEl", None, "Toan"]))