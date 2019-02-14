list_number = []
print('Give me a series of numbers and I will give you their median.')
while True:
	number = input()
	if number == '':
		break
	else:
		list_number.append(int(number))
leng = len(list_number)
if leng == 0:
	print('Error, empty dataset')
else:
	if leng % 2 == 1:
		median = list_number[leng//2]
	else:
		median = (list_number[leng//2 - 1] + list_number[leng//2])/2
	print('The median is %.1f' %median)
