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
		return (l[0] == element) or exists(l[1:], element)
	else:
		return False

# 4 - Recursive function that, given two lists, returns their concatenation
def concatenation(l1, l2):
    if l2:
        l1.append(l2[0])
        concatenation((l1), l2[1:])
    return l1

# 5 - Recursive function that, given a list, returns its reverse
def reverse(l):
	if l:
		return [l[-1]] + reverse(l[:-1])
	else:
		return []

# 6 - Recursive function that, given a list, checks if it is a palindrome
def isPalindrome(l):
	if l:
		return (l[0] == l[-1]) and isPalindrome(l[1:-1])
	else:
		return True

# 7 - Recursive function that, given a list of lists, returns their concatenation
def multipleConcatenation(l):
	if len(l) > 1:
		print(l[0] + l[1])
		return l[0] + l[1] + multipleConcatenation(l[2:])
	elif len(l) == 1:
		return l[0]
	else:
		return []

# 8 - Recursive function that, given a list and elements x and y, returns a similar list but on which all occurrences of x are replaced by y
def replace(l, original, new):
	final_list = []
	if l:
		if l[0] == original:
			final_list.append(new)
		else:
			final_list.append(l[0])

		return final_list + replace(l[1:], original, new)
	return []

# 9 - Recursive function that, given two ordered lists of numbers, returns their ordered merge, keeping any repetitions
def orderedMerge(l1, l2):
    if l2:
        l1.append(l2[0])
        orderedMerge(l1, l2[1:])
    return sorted(l1)

# 10 - Recursive function that, given a list, returns a list of all subsets in a form of list of lists
def allSubsets(l):
	return reduce(lambda result, x: result + [subset + [x] for subset in result], l, [[]])