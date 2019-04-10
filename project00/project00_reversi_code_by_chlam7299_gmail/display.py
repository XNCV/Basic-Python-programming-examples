import variables as V


def display(list_of_list):
    print('  a b c d e f g h')
    n = 0
    for list in list_of_list:
        n += 1
        string = str(n)
        for i in list:
            string = string + ' ' + i
        print(string)
