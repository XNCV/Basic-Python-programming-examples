variable_string = ''
# The case: the user enters data
while True:
    string = input()
    variable_string = variable_string + string + '\n'
    if(string == ''):
        break
# The case: using available data
# you need update the value in declared variable variable_string
number = 0
for i in range(len(variable_string)):
    if(variable_string[i] == '\n'):
        number += 1
print(number - 1)
