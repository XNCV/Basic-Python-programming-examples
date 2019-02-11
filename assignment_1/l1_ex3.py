range_number = int(input('Value? '))
for i in range(range_number):
    number = i + 1
    if((number % 9 == 0) and (number % 5 == 0)):
        print('Number')
    elif(number % 5 == 0):
        print('Play')
    elif(number % 9 == 0):
        print('With')
    else:
        print(number)
