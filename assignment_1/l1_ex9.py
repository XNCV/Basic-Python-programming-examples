locomotive1 = ' ______________________>__ '
locomotive2 = '|]||[]_[]_[]|||[]_[]_[]||[|'
locomotive3 = '\==o-o======o-o======o-o==/'
wagon1 = ' _________________________  '
wagon2 = '|]||[]_[]_[]|||[]_[]_[]||[| '
wagon3 = '\==o-o======o-o======o-o==/_'
while True:
	try:
		long_train = int(input('What is the size of your train? '))
		if(long_train < 0):
			print('Don\'t be so negative.')
		elif(long_train == 0):
			pass
		else:
			line1 = (long_train - 1)*wagon1 + locomotive1
			line2 = (long_train - 1)*wagon2 + locomotive2
			line3 = (long_train - 1)*wagon3 + locomotive3
			print(line1)
			print(line2)
			print(line3)
		break
	except:
		print('The size of your train must be an integer.')
