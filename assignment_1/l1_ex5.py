size = int(input('What pyramid size do you want?\n'))
if (size % 2) == 0:
    size = size - 1
num_of_line = int(size / 2) + 1
for i in range(num_of_line):
    num_of_space = int(size / 2) - i
    num_of_symbol = size - num_of_space * 2
    # print space
    for space in range(num_of_space):
        print(' ', end='')
    for symbol in range(num_of_symbol):
        print('#', end='')
    print('')
