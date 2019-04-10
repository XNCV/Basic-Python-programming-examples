""
# Function 1: Find all valid choice of a player
#         dictionary: posDic = {'W': [""], 'B': [""]}
#         dictionary: reverseDic = {"move": [positions be reversed]}
#     parameter:
#         string: which player to be found posible moves 'W' or 'B'
#     return:
#         list: list of all posible move [""]
#         Update the reverseDic

""
# Function 2: Update posDic + Upate_board
#        dictionary: posDic = {"move": [positions be reversed]}
#        dictionary: reverseDic = {}
#     parameter
#         String: player
#         String: choice: the choiced move
#     return:
#         None: Update the posDic, board

""
# Funtion 3: Update points
#     parameter:
#         dictionary: points {"W": num, "B": num}
#         dictionary: posDics
#     return:
#         None: update points dicitionary

""

# Function 4: Return a list contain valid move at the end (called listValid)
#         dictionary: posDic = {'W': [""], 'B': [""]}
#         dictionary: reverseDic = {"move": [positions be reversed]}
#     parameter:
#         string: posPlayer: position of current player
#         string: posOppo: position of adjacent Opponent
#         string: Who is current Player 'W' or 'B'
#         string: Who is Opponent 'W' or 'B'
#     return:
#         list: list[len(list) - 1] will be the valid move, list[:-1] will be
#               the pos to be reversed

""
# Function 5: Update reverseDic
#        dictionary: reverseDic = {"move": [positions be reversed]}
#     parameter:
#         list: listValid: list contains valid move at the end
#     return:
#         None: Update reverseDic with key is the list[len(list) - 1],
#               value is list[:-1]

""
# Function 6: update board
#         dictionary: posDic
#         list: board
#     parameter:
#         None
#     return:
#         None: Update the board by posDic
