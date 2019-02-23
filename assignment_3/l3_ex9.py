def find_genealogy(father_d, mother_d, person):
	# Create a genealogy of the person
	genealogy = [person]
	child = [person]
	conti = True
	while(conti):
		# Update the child need consider their parents
		child_new = child
		# The list child will save the parents of the list chid_new
		child = []
		for name in child_new:
			# Find father
			if name in father_d.keys():
				genealogy.append(father_d[name])
				child.append(father_d[name])
			# Find mother
			if name in mother_d.keys():
				genealogy.append(mother_d[name])
				child.append(mother_d[name])
			# If the list chid_new dont have their parents in the list, we will end the process
			if len(child) == 0:
				conti = False
	return genealogy


def are_related(father_d, mother_d, first, second):
	# The first, we create two Genealogies of two people
	# Then, compare them, if have any similarities, they related to each other
	first_genealogy = set(find_genealogy(father_d, mother_d, first))
	second_genealogy = set(find_genealogy(father_d, mother_d, second))
	# If two genealogies have any similarities, we certairn that they related to each other 
	if len(first_genealogy.intersection(second_genealogy)) != 0:
		return True
	else:
		return False


print(are_related({'John': 'Jack', 'Jack': 'Jim'}, {'Jim': 'El'}, 'John', 'El'))
