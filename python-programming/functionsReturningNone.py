#1 - Recursive function that, given a list, returns its head (0) element 
def head(l):
	if l:
		return l[0]
	else:
		return None

#2 - Recursive function that, given a list, returns its tail (all elements but the first) 
def tail(l):
	if len(l) > 1:
		return l[1:]
	else:
		return None

#3 - Recursive function that, given a tuple of equal-sized lists, returns a list of tuples of elements in the same position 
def ranking(tup):
    l1, l2 = tup
    if len(l1) != len(l2):
        return None
    if l1 and l2:
        new_tuple = (l1[1:], l2[1:])
        return [(l1[0],l2[0])] + ranking(new_tuple)
    else:
        return []

#4 - Recursive function that, given a list of numbers, returns the lowest element 
def lowest(l):
    if len(l) > 1:
        if l[0] > l[-1]:
            return lowest(l[1:])
        else:
            return lowest(l[:-1])
    elif len(l) == 1:
        return l[0]
    else:
        return None

#5 - Recursive function that, given a list of numbers, returns a tuple of the lowest element and a list of all the other elements 
def popLowest(l):
	if l:
		minor_node = l[0] if l[0] < l[-1] else l[-1]
		next_search_list = l[:-1] if l[0] < l[-1] else l[1:]
		without_lowest_list = l[1:] if l[0] < l[-1] else l[:-1]

		recursive_answer = popLowest(next_search_list)
		if recursive_answer == None:
			return (minor_node, without_lowest_list)
		else:
			recursive_mini = recursive_answer[0]
			return (minor_node, without_lowest_list) if recursive_mini >= minor_node else (recursive_mini, [x for x in l if x != recursive_mini])
	else:
		return None

#6 - Recursive function that, given a list of numbers, returns a tuple of the largest and lowest elements 
def highLow(l):
	if len(l) > 1:
		recursive_answer = highLow(l[1:-1])
		minor = l[0] if l[0] < l[-1] else l[-1]
		maxim = l[0] if l[0] > l[-1] else l[-1]
		
		if recursive_answer:
			return (recursive_answer[0] if recursive_answer[0] > maxim else maxim, recursive_answer[1] if recursive_answer[1] < minor else minor)	
		else:
			return (maxim, minor)
	else:
		return None


#7 - Recursive function that, given a list of numbers, returns a triple of the largest and lowest elements and a list of all the other elements 
def popHighLow(l):
	if len(l) > 1:
		recursive_answer = popHighLow(l[1:-1])
		minor = l[0] if l[0] < l[-1] else l[-1]
		maxim = l[0] if l[0] > l[-1] else l[-1]
		
		if recursive_answer:
			minor = minor if minor < recursive_answer[1] else recursive_answer[1]
			maxim = maxim if maxim > recursive_answer[0] else recursive_answer[0]
			return (maxim, minor, [x for x in l if x != maxim and x != minor] + recursive_answer[2])	
		else:
			return (maxim, minor, [])
	else:
		return None

#8 - Recursive function that, given an ordered list of numbers, returns, if possible, a tuple of its mean and median
def meanMedian(l):
	if len(l) > 1: 
		recursive_answer = meanMedian(l[1:-1])
		if recursive_answer:
			return (recursive_answer[0] + ((l[0] + l[-1] - recursive_answer[0]) / len(l)), recursive_answer[1])
		else:
			return ((l[0] + l[-1])/2, (l[0] + l[1]) / 2)
	elif len(l) == 1:
		return (l[0], l[0])
	else:
		return None