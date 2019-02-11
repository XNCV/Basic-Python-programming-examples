money = int(input('What\'s the bill ? '))
if money == 0:
	print('Oh, it was free !')
elif money < 0:
	print('Well, it\'s you who owes me money then.')
else:
	# To have as few banknotes and coins as possible,
	# You need devide your money to the value descending in order
	num2000 = money // 2000
	if num2000 > 0:
		print(str(num2000) + ' 2000 banknote')
	excess = money - num2000*2000
	if excess > 0:
		num1000 = excess // 1000
		if num1000 > 0:
			print(str(num1000) + ' 1000 banknote')
		excess = excess - num1000*1000
		if excess > 0:
			num100 = excess // 100
			if num100 > 0:
				print(str(num100) + ' 100 coin')
			excess = excess - num100*100
			if excess > 0:
				num50 = excess // 50
				if num50 > 0:
					print(str(num50) + ' 50 coin')
				excess = excess - num50*50
				if excess > 0:
					print(str(excess) + ' 1 coin')
