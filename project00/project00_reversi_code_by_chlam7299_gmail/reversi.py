import variables as V
from Find_all_choices import findAllValidChoices
from find_winner import find_winner
from display import display
from input_choice import input_choice
from update_posDic import update_posDic

print("======= WELCOME TO REVERSI =======")
while True:
    Bvalid = True
    Wvalid = True
    # for player B
    print("\n==== B's TURN ====")
    choicesB = findAllValidChoices('B')
    if len(choicesB) > 0:
        display(V.board)
        move = input_choice(choicesB, 'B')
        update_posDic(move, 'B')
    else:
        Bvalid = False
        print("Player B cannot play.")

    # for player W
    print("\n==== W's TURN ====")
    choicesW = findAllValidChoices('W')
    if len(choicesW) > 0:
        display(V.board)
        move = input_choice(choicesW, 'W')
        update_posDic(move, 'W')
    else:
        Wvalid = False
        print("Player W cannot play.")

    if not (Wvalid or Bvalid):
        display(V.board)
        find_winner()
        break
