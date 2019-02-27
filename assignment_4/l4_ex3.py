def apple_pen(first_ingredient, second_ingredient):
	# Though I try to listen this song, I dont really what target this problem want to get
	# but the solution may be written as follow:
	if first_ingredient == 'pen' and (second_ingredient == 'apple' or second_ingredient == 'pineapple' or second_ingredient == 'pen'):
		head_string = 'I have a %s, I have a %s \\n' % (first_ingredient, second_ingredient)
		if second_ingredient == 'pen':
			end_string = 'Uh! Long pen!'
		else:
			end_string = 'Uh! %s-%s!' % (second_ingredient.capitalize(), first_ingredient.capitalize())
		return head_string + end_string
	else:
		raise ValueError('It is not in the lyrics')


print(apple_pen('apple', 'pen'))
