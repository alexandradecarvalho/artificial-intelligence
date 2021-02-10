#1 - Function that, given a list of tuples, returns a tuple with the list of all first elements of the tuples and a list of all the second elements: [(a1,b1),...,(an,bn)] := ([a1,...,an],[b1,...,bn])
def splitting(l):
	l1 = []
	l2 = []
	if l:
		l1 += [l[0][0]]
		l2 += [l[0][1]]
		recursive_ans = splitting(l[1:])
		return (l1 + recursive_ans[0], l2 + recursive_ans[1])
	return (l1,l2)

#2 - Function that, given a list l and an element x, returns a tuple with the list of all elements of l different from x and the number of occurrences of x in l
def popNCount(l, element):
	if l:
		recursive_ans = popNCount(l[1:], element)
		if l[0] == element:
			return ([] + recursive_ans[0], 1 + recursive_ans[1])
		else:
			return ([l[0]] + recursive_ans[0], 0 + recursive_ans[1])
	return ([], 0)

#3 - Function that, given a list, returns a list of tuples with each element of the list and its number of occurrences
def occurrences(l):
	if l:
		head = l[0]
		counter = 0
		new_list = []
		for element in l:
			if element == head:
				counter += 1
			else:
				new_list.append(element)
		return [(head, counter)] + occurrences(new_list)
	return []