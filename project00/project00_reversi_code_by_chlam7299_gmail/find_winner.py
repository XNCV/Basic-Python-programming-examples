import variables as V
#   dictionary: posDic
# parameters:
#    None
# return:
#    print point and name of winner


def find_winner():
    point_B = len(V.posDic["B"])
    point_W = len(V.posDic["W"])
    print("\n==== End of the game ====")
    print("W: %s, B: %s" % (point_W, point_B))
    if point_B > point_W:
        print('B wins!')
    elif point_B == point_W:
        print('Draws')
    else:
        print('W wins!')


# print(find_winner({'B': 3, 'W': 4}))
