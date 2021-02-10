#1 - Function that, given a list, returns its head (0) element 
def head(l):
	if l:
		return l[0]
	else:
		return None

#2 - Function that, given a list, returns its tail (all elements but the first) 
def tail(l):
	if len(l) > 1:
		return l[1:]
	else:
		return None

#3 - Function that, given a tuple of equal-sized lists, returns a list of tuples of elements in the same position 
def ranking(tup):
    l1, l2 = tup
    if len(l1) != len(l2):
        return None
    if l1 and l2:
        new_tuple = (l1[1:], l2[1:])
        return [(l1[0],l2[0])] + ranking(new_tuple)
    else:
        return []


#4 - Function that, given a list of numbers, returns the lowest element 
def menor(l):
	pass

#5 - Function that, given a list of numbers, returns a tuple of the lowest element and a list of all the other elements 
def popLowest(l):
	pass 

#6 - Function that, given a list of numbers, returns a tuple of the largest and lowest elements 
def highLow(l1, l2):
    pass

#7 - Function that, given a list of numbers, returns a triple of the largest and lowest elements and a list of all the other elements 
def popHighLow(l):
	pass

#8 - Function that, given an ordered list of numbers, returns, if possible, a tuple of its mean and median
def meanMedian(l):
	pass 
