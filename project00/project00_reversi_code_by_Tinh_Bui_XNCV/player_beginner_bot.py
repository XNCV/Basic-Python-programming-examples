def one_point(row, column, list_of_list, nameplayer):
    if(nameplayer == 'B'):
        name_defent = 'W'
    elif(nameplayer == 'W'):
        name_defent = 'B'
    # 0: left;  1: right; 2: up;  3: down;
    # 4: left-up; 5: right-down; 6: left-down; 7: right-up
    for i in range(8):
        list_trans = [[], []]
        r = row
        c = column
        list_trans[0].append(r)
        list_trans[1].append(c)
        control = 0
        if i == 0:
            c = c - 1
        elif i == 1:
            c = c + 1
        elif i == 2:
            r = r - 1
        elif i == 3:
            r = r + 1
        elif i == 4:
            r = r - 1
            c = c -1
        elif i == 5:
            r = r + 1
            c = c +1
        elif i == 6:
            r = r + 1
            c = c -1
        elif i == 7:
            r = r - 1
            c = c + 1
        if(r > -1 and c > -1 and r < 8 and c < 8):
            # dis.display(list_of_list)
            # print(r, c)
            if(list_of_list[r][c] == name_defent):
                list_trans[0].append(r)
                list_trans[1].append(c)
                control = 1
        while(control == 1):
            if i == 0:
                c = c - 1
            elif i == 1:
                c = c + 1
            elif i == 2:
                r = r - 1
            elif i == 3:
                r = r + 1
            elif i == 4:
                r = r - 1
                c = c -1
            elif i == 5:
                r = r + 1
                c = c +1
            elif i == 6:
                r = r + 1
                c = c -1
            elif i == 7:
                r = r - 1
                c = c + 1
            if(r > -1 and c > -1 and r < 8 and c < 8):
                list_trans[0].append(r)
                list_trans[1].append(c)
                if(list_of_list[r][c] == nameplayer):
                    break
                elif(list_of_list[r][c] == '.'): # or list_of_list[r][c] == name_defent):    list_of_point = []
                    list_trans = [[], []]
                    break
            else:
                list_trans = [[], []]
                break
    return (len(list_trans[0]))
# return the best choice
def player_beginner_bot(list_of_list, list_of_choices, nameplayer):
    list_of_point = []
    correct_input = []
    for i in range(len(list_of_choices[0])):
        number = one_point(list_of_choices[0][i], list_of_choices[1][i], list_of_list, nameplayer)
        list_of_point.append(number)
    max_p = max(list_of_point)
    for i in range(len(list_of_point)):
        if max_p == list_of_point[i]:
            correct_input.append(list_of_choices[0][i])
            correct_input.append(list_of_choices[1][i])
            break
    string = chr(correct_input[1] + 97) + str(correct_input[0] + 1)
    print('player bot choise: ' + string)
    return correct_input
