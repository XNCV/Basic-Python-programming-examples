# parameters:
#    dictionary point of B and W
# return:
#    print point and name of winner
def find_winner(dictionary):
    point_B = str(dictionary['B'])
    point_W = str(dictionary['W'])
    print('End of the game. W: ' + point_W + ', B: ' + point_B)
    if point_B > point_W:
        print('B wins')
    elif point_B == point_W:
        print('=')
    else:
        print('W wins')
# print(find_winner({'B': 3, 'W': 4}))
