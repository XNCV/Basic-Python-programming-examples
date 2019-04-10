# parameter:
# 	- list_of_list
#   - input_choice
# return:
# 	- list_of_list update
import display as dis
def process(list_of_list, input_choice, nameplayer):
    if(nameplayer == 'B'):
        name_defent = 'W'
    elif(nameplayer == 'W'):
        name_defent = 'B'
    # 0: left;  1: right; 2: up;  3: down;
    # 4: left-up; 5: right-down; 6: left-down; 7: right-up
    for i in range(8):
        list_trans = [[], []]
        r = input_choice[0]
        c = input_choice[1]
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
                elif(list_of_list[r][c] == '.'): # or list_of_list[r][c] == name_defent):
                    list_trans = [[], []]
                    break
            else:
                list_trans = [[], []]
                break
        for i in range(len(list_trans[0])):
            list_of_list[list_trans[0][i]][list_trans[1][i]] = nameplayer
    return list_of_list

# list_of_list = [['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', 'W', 'B', '.', '.', '.'],
#                 ['.', '.', '.', 'B', 'B', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.'],
#                 ['.', '.', '.', '.', '.', '.', '.', '.']]
# dis.display(process(list_of_list, [5, 3],'W'))
