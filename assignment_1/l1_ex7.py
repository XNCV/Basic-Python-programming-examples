result = int(input('What is the result? '))
print('OK, let\'s begin\n')
# The variable 'control' is used for condition LOSE
control = True
for i in range(11):
	num = 10 - i
	if(num >= 0):
		string = 'Your guess? ('
		if(num == 5):
			string = string + 'Half way done) '
		elif(num == 0):
			string = string + 'Last guess) '
		else:
			string = string + str(num) + ' left) '
		print(string, end='')
		number = int(input())
		diff = result - number
		if(diff > 50):
			print('It\'s way more')
		elif(diff <= 50 and diff > 0):
			print('It\'s more')
		elif(diff == 0):
			print('Congrats !')
			control = False
			break
		elif(diff < 0 and diff >= -50):
			print('It\'s less')
		else:
			print('It\'s way less')
if control:
	print('You lose :(')
