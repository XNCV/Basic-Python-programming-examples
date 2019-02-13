def order_words(array):
	if len(array) == 0:
		return [[]]
	else:
		array_out = []
		array_current = []
		array = sorted(array, key=len)
		while(len(array) != 0):
			if len(array) > 0:
				for element in array:
					if len(element) == len(array[0]):
						array_current.append(element)
					else:
						break
				for element in array_current:
					array.remove(element)
			array_current.sort()
			array_out.append(array_current)
			array_current = []
	return array_out


print(order_words(['aa', 'laurie', 'daniel', 'toto', 'tata', 'aA', 'AA', 'Aa']))