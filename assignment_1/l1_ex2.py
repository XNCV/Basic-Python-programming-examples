va1 = input('Player 1? ')
va2 = input('Player 2? ')
if((va1 != 'paper' and va1 != 'rock' and va1 != 'scissors') or\
   (va2 != 'paper' and va2 != 'rock' and va2 != 'scissors')):
    print('Error')
else:
    if((va1 == 'scissors' and va2 == 'paper') or (va1 == 'paper' and va2 == 'rock') or (va1 == 'rock' and va2 == 'scissors')):
        print('Player 1 wins.')
    elif(va1 == va2):
        print('Draw')
    else:
        print('Player 2 wins.')