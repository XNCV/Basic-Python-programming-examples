# Initializing all started variables
colums = "a b c d e f g h".split()
rows = "1 2 3 4 5 6 7 8".split()

points = {'W': 0, 'B': 0}
posDic = {'W': ["d4", "e5"], 'B': ["d5", "e4"]}


validChoices = [""]
# reverseDic: {"pos of the valid move": [pos of those quan be reversed]}
#   each choice will be a key in a dic, its value is list of
#   positions to be reversed
reverseDic = {}

board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'W', 'B', '.', '.', '.'],
         ['.', '.', '.', 'B', 'W', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]
