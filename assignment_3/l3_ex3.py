def count_occurrences(string):
	dictionary = string.split()
	count_occurrences_of_word = {}
	while len(dictionary) != 0:
		num = 0
		word_current = dictionary[0]
		# Count the number of the current word appeared
		for word in dictionary:
			if word == word_current:
				num = num + 1
		# The arrays in our dictionary must be a list to use function append
		if num not in count_occurrences_of_word.keys():
			count_occurrences_of_word[num] = []
		# Append the current word with correct key
		count_occurrences_of_word[num].append(word_current)
		# Remove the counted word
		for i in range(num):
			dictionary.remove(word_current)
	# Sort the array alphabetically
	for key in count_occurrences_of_word.keys():
		count_occurrences_of_word[key].sort()
	return count_occurrences_of_word


string = 'daniel mathieu laurie toan toan laurie mathieu mathieu'
print(count_occurrences(string))
