def create_dictionary(list_of_list):
    point_B = 0
    point_W = 0
    dictionary = {}
    for list in list_of_list:
        point_B = point_B + list.count('B')
        point_W = point_W + list.count('W')
    dictionary['B'] = point_B
    dictionary['W'] = point_W
    return dictionary

# print(create_dictionary([['.', '.', '.', '.', '.', '.', '.', '.'],
#                          ['.', '.', '.', '.', '.', '.', '.', '.'],
#                          ['.', '.', '.', '.', '.', '.', '.', '.'],
#                          ['.', '.', '.', 'W', 'B', 'B', '.', '.'],
#                          ['.', '.', '.', 'B', 'B', 'W', '.', '.'],
#                          ['.', '.', '.', '.', '.', '.', '.', '.'],
#                          ['.', '.', '.', '.', '.', '.', '.', '.'],
#                          ['.', '.', '.', '.', '.', '.', '.', '.']]))
