import variables as V
#  function 6: Update board


def update_board():
    for player in V.posDic:
        for pos in V.posDic[player]:
            col = V.colums.index(pos[0])
            row = V.rows.index(pos[1])
            V.board[row][col] = player

# Function 2: Update posDic + update board


def update_posDic(choice, player):
    opponent = 'W' if player == 'B' else 'B'
    revPos = V.reverseDic[choice]
    # print(V.reverseDic[choice])
    for pos in revPos:
        V.posDic[opponent].remove(pos)
        V.posDic[player].append(pos)
    V.posDic[player].append(choice)
    update_board()
