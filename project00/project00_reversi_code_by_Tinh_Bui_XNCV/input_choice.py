# parameters:
#    list_of_choices is a list of valid choices
#    nameplayer is 'B' or 'W'
# return:
#    choice_input is correct input  by list[1] = row, list[2] = column
#    print "Invalid choice" if input is fail and require input again
def input_choice(list_of_choices_1, nameplayer):
    list_of_choices_2 = []
    for i in range(len(list_of_choices_1[0])):
        string = chr(list_of_choices_1[1][i] + 97) + str(list_of_choices_1[0][i] + 1)
        list_of_choices_2.append(string)
    list_of_choices_2 = set(list_of_choices_2)
    list_of_choices = []
    for i in list_of_choices_2:
        list_of_choices.append(i)
    list_of_choices = sorted(list_of_choices)
    # print valid choices
    list_s = 'Valid choices: '
    for choice in list_of_choices:
        list_s = list_s + choice + ' '
    print(list_s)
    # input choice
    # string = 'Player ' + nameplayer + ':'
    choice_input = input('Player ' + nameplayer + ': ')
    # check choice_input
    control = 0
    while(control == 0):
        noti = ''
        for choice in list_of_choices:
            if choice == choice_input:
                control = 1
                break
        if(control == 0):
            noti = choice_input + ': Invalid choice'
            print(noti)
            print(list_s)
            choice_input = input('Player ' + nameplayer + ': ')
    correct_input = []
    correct_input.append(int(choice_input[1]) - 1)
    correct_input.append(int(ord(choice_input[0]) - 97))
    return correct_input
# print(input_choice(['a2', 'b1', 'c5'], 'B'))
