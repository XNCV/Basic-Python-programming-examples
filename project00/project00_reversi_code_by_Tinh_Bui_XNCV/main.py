import create_dictionary as cd
import display as dp
import find_valid_choices as fv
import find_winner as fw
import input_choice as ic
import process as pr
import player_beginner_bot as bot

print('Number 1: play with your friend; number 2: play with beginner bot')
mode = input('You choice number: ')
while True:
    if mode != '1' and mode != '2':
        mode = input('You need choice number again: ')
    else:
        break
list_of_list = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'W', 'B', '.', '.', '.'],
                ['.', '.', '.', 'B', 'W', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
dp.display(list_of_list)
if mode == '1':
    while True:
        list_of_choices = fv.find_valid_choices(list_of_list, 'B')
        if(len(list_of_choices[0]) == 0):
            print('Player B cannot play.')
            break
        input_choice = ic.input_choice(list_of_choices, 'B')
        list_of_list = pr.process(list_of_list, input_choice, 'B')  #return new update list_of_list
        dp.display(list_of_list)
        #####
        list_of_choices = fv.find_valid_choices(list_of_list, 'W')
        if(len(list_of_choices[0]) == 0):
            print('Player W cannot play.')
            break
        input_choice = ic.input_choice(list_of_choices, 'W')
        list_of_list = pr.process(list_of_list, input_choice, 'W')
        dp.display(list_of_list)
elif mode == '2':
    while True:
        list_of_choices = fv.find_valid_choices(list_of_list, 'B')
        if(len(list_of_choices[0]) == 0):
            print('Player B cannot play.')
            break
        input_choice = ic.input_choice(list_of_choices, 'B')
        list_of_list = pr.process(list_of_list, input_choice, 'B')  #return new update list_of_list
        dp.display(list_of_list)
        #####
        list_of_choices = fv.find_valid_choices(list_of_list, 'W')
        if(len(list_of_choices[0]) == 0):
            print('Player W cannot play.')
            break
        input_choice = bot.player_beginner_bot(list_of_list, list_of_choices, 'W')
        list_of_list = pr.process(list_of_list, input_choice, 'W')
        dp.display(list_of_list)

dictionary = cd.create_dictionary(list_of_list) # return dictionary = {'B': point_B, 'W': point_W}
fw.find_winner(dictionary)
