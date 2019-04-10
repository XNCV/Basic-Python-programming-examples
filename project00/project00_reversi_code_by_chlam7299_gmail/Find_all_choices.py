import variables as V

# Function 4: Return a list contain valid move at the end (called listValid)


def returnValidMove(posPlayer, posOppo, player, Oppo):
    # colum and row of started position
    col = V.colums.index(posPlayer[0])
    row = V.rows.index(posPlayer[1])
    colDif = V.colums.index(posOppo[0]) - col
    rowDif = V.rows.index(posOppo[1]) - row

    listre = []
    while True:
        col += colDif
        row += rowDif
        if row not in range(0, 8) or col not in range(0, 8):
            listre.clear()
            break
        OppoTmp = V.colums[col] + V.rows[row]
        if OppoTmp in V.posDic[Oppo]:
            listre.append(OppoTmp)
        elif OppoTmp in V.posDic[player]:
            listre.clear()
            break
        else:
            listre.append(OppoTmp)
            break
    return listre


# Function 5: Update reverseDic
def updateRevDic(listValid):
    if len(listValid) == 0:
        return -1
    theMove = listValid[len(listValid) - 1]
    quanToRev = listValid[:-1]
    if V.reverseDic.get(theMove) is None:
        V.reverseDic[theMove] = quanToRev
    else:
        V.reverseDic[theMove].extend(quanToRev)


# Function 1: Find all valid choice of a player
def findAllValidChoices(player):
    V.reverseDic.clear()
    oppo = 'W' if player == 'B' else 'B'
    posibleMoves = []
    # Loop through each player's positions
    for pos in V.posDic[player]:
        col = V.colums.index(pos[0])
        row = V.rows.index(pos[1])
        for j in range(-1, 2):
            for i in range(-1, 2):
                if row + j in range(0, 8) and col + i in range(0, 8):
                    posAdjOppo = V.colums[col + i] + V.rows[row + j]
                    existOppo = posAdjOppo in V.posDic[oppo]
                    listTm = []
                    if existOppo:
                        listTm = returnValidMove(pos, posAdjOppo, player, oppo)
                    updateRevDic(listTm)
    return list(V.reverseDic.keys())


# print(V.reverseDic, findAllValidChoices("B"))
