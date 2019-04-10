def find_choice_one_point(row, column, list_of_list, nameplayer):
    if(nameplayer == 'B'):
        name_defent = 'W'
    elif(nameplayer == 'W'):
        name_defent = 'B'
    valid_choice_one = [[], []]
    # 0: left;  1: right; 2: up;  3: down;
    # 4: left-up; 5: right-down; 6: left-down; 7: right-up
    for i in range(8):
        r = row
        c = column
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
            if(list_of_list[r][c] == name_defent):
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
                if(list_of_list[r][c] == nameplayer):
                    break
                elif(list_of_list[r][c] == '.'):
                    valid_choice_one[0].append(r)
                    valid_choice_one[1].append(c)
                    break
            else:
                break
    return valid_choice_one


# return list_of_choices
def find_valid_choices(list_of_list, nameplayer):
    # create coordination of point 'B' and point 'W'
    PB = [[], []]
    PW = [[], []]
    list_of_choices = [[], []]
    a = -1
    for row in list_of_list:
        a += 1
        b = -1
        for column in row:
            b += 1
            if column == 'B':
                PB[0].append(a)
                PB[1].append(b)
            elif column == 'W':
                PW[0].append(a)
                PW[1].append(b)
    if nameplayer == 'B':
        for n in range(len(PB[0])):
            valid_choice_one = find_choice_one_point(PB[0][n], PB[1][n], list_of_list, nameplayer)
            for i in range(len(valid_choice_one[0])):
                list_of_choices[0].append(valid_choice_one[0][i])
                list_of_choices[1].append(valid_choice_one[1][i])
    elif nameplayer == 'W':
        for n in range(len(PW[0])):
            valid_choice_one = find_choice_one_point(PW[0][n], PW[1][n], list_of_list, nameplayer)
            for i in range(len(valid_choice_one[0])):
                list_of_choices[0].append(valid_choice_one[0][i])
                list_of_choices[1].append(valid_choice_one[1][i])
    return list_of_choices

# list_of_list = [['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', 'W', 'B', '.', '.', '.'],
#                 ['.', '.', 'W', 'B', 'B', 'B', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.']]
# print(find_valid_choices(list_of_list, 'W'))
