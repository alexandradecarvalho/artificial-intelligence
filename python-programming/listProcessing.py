import copy 

# 1 - Recursive function that, given a list, returns its size
def size(l):
	s = 0
	if l:
		s += 1 + size(l[1:])	
	return s

# 2 - Recursive function that, given a list of numbers, returns their sum
def numberSum(l):
	sum = 0
	if l:
		sum += l[0] + numberSum(l[1:])
	return sum

# 3 - Recursive function that, given a list and an element, checks if the element exists on the list, returning the respective boolean
def exists(l, element):
	if l:
		return (int(l[0]) == element) or exists(l[1:], element)
	else:
		return False

# 4 - Recursive function that, given two lists, returns their concatenation
def concatenation(l1, l2):
	if l2:
		l1 += l2[0] + concatenation(l2[1:])
	return l1

# 5 - Function that, given a list, returns its reverse
def reverse(l):
	pass

# 6 - Function that, given a list, checks if it is a palindrome
def isPalindrome(l):
	pass

# 7 - Function that, given a list of lists, returns their concatenation
def multipleConcatenation(l):
	pass

# 8 - Function that, given a list and elements x and y, returns a similar list but on which all occurences of x are replaced by y
def replace(l, original, new):
	pass

# 9 - Function that, given two ordered lists of numbers, returns their ordered merge, keeping any repetitions
def orderedMerge(l1, l2):
	pass

# 10 - Function that, given a list, returns a list of all subsets in a form of list of lists
def allSubsets(l):
	pass