hori = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]


board[3][4] = 'B'
board[3][3] = 'W'
board[4][4] = 'W'
board[4][3] = 'B'


directions = [
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1],
        [-1, 0],
        [-1, 1]
        ]


#  Rind valid place.
def find_valid_place():
    global player_one_valid_place
    global player_two_valid_place

    player_one_valid_place = []
    player_two_valid_place = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "B":
                move = [row, col]
                player = "B"
                movable = valid_moves(move, player)
                for i in movable:
                    if i not in player_one_valid_place:
                        player_one_valid_place.append(i)
                # Return player_one_valid_place.
            elif board[row][col] == "W":
                move = [row, col]
                player = "W"
                movable = valid_moves(move, player)
                for i in movable:
                    if i not in player_two_valid_place:
                        player_two_valid_place.append(i)
                # Return player_two_valid_place.


# Return array location.
def return_location(move, player):
    if len(move) != 2:
        print('{}: Invalid choice\
\nValid choices: {}'.format(move, ' '.join(sorted(valid_choices(player)))))
        return False
    col = 'a b c d e f g h'.split()
    row = '1 2 3 4 5 6 7 8'.split()
    if move[0] in col and move[1] in row:
        y = hori[move[0]]
        x = int(move[1]) - 1
        return [x, y]
    else:
        print('{}: Invalid choice\
\nValid choices: {}'.format(move, ' '.join(sorted(valid_choices(player)))))
        return False


# Create the board.
def new_board():
    find_valid_place()

    print(' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    count_line = 0
    for vertical in range(1, 9):
        print(vertical, ' '.join(board[count_line]))
        count_line += 1


# Check if move inside the board.
def nam_trong(x, y):
    return x in range(8) and y in range(8)


# Check if the move is in valid place or not.
def player_move(move, player):
    x = move[0]
    y = move[1]
    if player == "B":
        valid_move_array = player_one_valid_place
    else:
        valid_move_array = player_two_valid_place

    # if x,y in valid_move_array: play and find valid place again for W

    if [x, y] in valid_move_array:
        board[x][y] = player
        eat(move, player)
        find_valid_place()
        return True
    else:
        hori_keys = list(sorted(hori.keys()))
        move[1] = hori_keys[move[1]]
        stupid_m = '{}{}'.format(move[1], move[0] + 1)
        print('{}: Invalid choice\
\nValid choices: {}'.format(stupid_m, ' '.join(sorted(valid_choices(player)))))
        return False


# Which to flip.
def eat(move, player):
    x = move[0]
    y = move[1]
    if player == 'B':
        other_place = 'W'
    else:
        other_place = 'B'

    eatable = []
    for dong, cot in directions:
        frow = x + dong
        fcol = y + cot
        # print("eatable", eatable)
        if nam_trong(frow, fcol) and board[frow][fcol] == other_place:
            eatable.append([frow, fcol])
            frow = frow + dong
            fcol = fcol + cot
            while nam_trong(frow, fcol) and board[frow][fcol] == other_place:
                eatable.append([frow, fcol])
                frow = frow + dong
                fcol = fcol + cot
        if nam_trong(frow, fcol) and board[frow][fcol] == player:
            for i in eatable:
                x_x = i[0]
                y_y = i[1]
                board[x_x][y_y] = player
        else:
            eatable = []
            pass


# Validate moves.
def valid_moves(move, player):
    x = move[0]
    y = move[1]
    if player == 'B':
        other_place = 'W'
    else:
        other_place = 'B'

    movable = []
    for dong, cot in directions:
        frow = x + dong
        fcol = y + cot
        if nam_trong(frow, fcol) and board[frow][fcol] == other_place:
            frow = frow + dong
            fcol = fcol + cot
            while nam_trong(frow, fcol) and board[frow][fcol] == other_place:
                frow = frow + dong
                fcol = fcol + cot
            if nam_trong(frow, fcol) and board[frow][fcol] == '.':
                movable.append([frow, fcol])
            else:
                pass
    return movable


# Return the coordinates[1,1] to [2, b].
def valid_choices(player):
    hori_keys = list(sorted(hori.keys()))

    b_choice = []
    w_choice = []

    if player == 'B':
        for arg in player_one_valid_place:
            arg[1] = hori_keys[arg[1]]
            b_choice.append('{}{}'.format(arg[1], arg[0] + 1))
            arg[1] = hori[arg[1]]
        return b_choice
    else:
        for arg in player_two_valid_place:
            arg[1] = hori_keys[arg[1]]
            w_choice.append('{}{}'.format(arg[1], arg[0] + 1))
            arg[1] = hori[arg[1]]
        return w_choice


# Play game.
def play_game():
    player = 'B'
    play = True
    B = ""
    W = ""
    while play:
        if player == 'B':
            # Player B's turn.
            new_board()
            if len(player_one_valid_place) == 0:
                print('Player B cannot play.')
                player = 'W'
                B = "die"
            else:
                print("Valid choice\
s:", ' '.join(sorted(valid_choices(player))))
                bmove = input('Player B: ')
                bmove_location = return_location(bmove, player)
                # if move is legit , move on. else, stay 'B'
                if return_location(bmove, player) is True:
                    if player_move(bmove_location, player) is True:
                        player = 'W'
                else:
                    pass

        else:
            # Player W's  turn.
            new_board()
            if len(player_two_valid_place) == 0:
                print('Player W cannot play.')
                player = 'B'
                W = "die"
            else:
                print("Valid choice\
s:", ' '.join(sorted(valid_choices(player))))
                wmove = input('Player W: ')
                wmove_location = return_location(wmove, player)
                # if move is legit , move on. else, stay 'B'
                while wmove_location is False:
                    wmove = input('Player W: ')
                    wmove_location = return_location(wmove, player)
                else:
                    finish_move = player_move(wmove_location, player)
                    while finish_move is False:
                        wmove = input('Player W: ')
                        wmove_location = return_location(wmove, player)
                    else:
                        player = 'B'

        # Out of move.
        if B == "die" and W == "die":
            play = False
    # Print score and aWnnounce the winner.
    score_b = []
    score_w = []
    for k in board:
        for j in k:
            if j == 'B':
                score_b.append(j)
            if j == 'W':
                score_w.append(j)
    print('End of the game.\
 W: {}, B: {}'.format(str(len(score_w)), str(len(score_b))))
    if len(score_w) > len(score_b):
        print('W wins.')
    elif len(score_w) == len(score_b):
        print('Draw.')
    else:
        print('B wins.')


play_game()
