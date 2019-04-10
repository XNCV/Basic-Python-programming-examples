# parameters:
#    list_of_choices is a list of valid choices
#    nameplayer is 'B' or 'W'
# return:
#    choice_input is correct input
#    print "Invalid choice" if input is fail and require input again


def input_choice(list_of_choices, nameplayer):
    # print valid choices
    list = 'Valid choices:'
    list += " ".join(sorted(list_of_choices))
    print(list)

    # input choice
    choice = input('Player ' + nameplayer + ': ')
    while True:
        if choice not in list_of_choices:
            print("\n%s: Invalid choice\n" % choice)
            print(list)
            choice = input('Player ' + nameplayer + ': ')
        else:
            break

    return choice
