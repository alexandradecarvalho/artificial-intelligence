import math 

#1 - Lambda expression that, given an integer n, returns True if it's odd and False otherwise
isOdd = lambda n : n % 2 == 0

#2 - Lambda expression that, given a number n, returns True if it's positive and False otherwise
isPositive = lambda n : abs(n) == n

#3 - Lambda expression that, given two numbers x and y, returns True if |x| < |y| and False otherwise
isLower = lambda x,y : abs(x) < abs(y)

#4 - Lambda expression that, given a pair (x,y), representing Cartesian coordinates of a point, returns a pair (r, θ), corresponding to the polar coordinates of that point
polarCoordinates = lambda pair : None if pair[0] == 0 else (math.sqrt(pow(pair[0],2) + pow(pair[1],2)), math.atan(pair[1]/pair[0]))

#5 - Function that, given 3 functions of two arguments each, f, g, and h, returns the function with 3 arguments x, y and z = h(f(x,y), g(y,z))
def compoundFunction(f,g,h,x,y,z):
    return h(f(x,y), g(y,z))

#6 - Function that, given a list and a unary boolean function, returns True if the function is positive for all elements in the list and False otherwise
def areAll(l, funct):
    if l:
        return funct(l[0]) and areAll(l[1:], funct)
    return True

#7 - Function that, given a list and a unary boolean function, returns True if the function is positive for at least one element in the list and False otherwise
def isOne(l, funct):
    for element in l:
        if funct(element):
            return True
    return False

#8 - Function that, given two lists, returns True if all elements in the first list are also in the second one, and False otherwise
def subgroup(l1,l2):
    if l1:
        return l1[0] in l2 and subgroup(l1[1:], l2)
    return True

#9 - Function that, given a not empty list and an order relationship, returns the lowest element on the list according to that order
def lowest(l, relationship):
    if len(l) > 1:
        if relationship(l[0],l[-1]):
            return lowest(l[:-1], relationship)
        else:
            return lowest(l[1:], relationship)
    elif len(l) == 1:
        return l[0]
    else:
        return None

#10 - Function that, given a not empty list and an order relationship, returns a tuple with the lowest element on the list according to that order and a list with all the other elements
def popLowest(l, relationship):
	if l:
		minor_node = l[0] if relationship(l[0],l[-1]) else l[-1]
		next_search_list = l[:-1] if relationship(l[0],l[-1]) else l[1:]
		without_lowest_list = l[1:] if relationship(l[0],l[-1]) else l[:-1]

		recursive_answer = popLowest(next_search_list, relationship)
		if recursive_answer == None:
			return (minor_node, without_lowest_list)
		else:
			recursive_mini = recursive_answer[0]
			return (minor_node, without_lowest_list) if not relationship(recursive_mini, minor_node) else (recursive_mini, [x for x in l if x != recursive_mini])
	else:
		return None

#11 - Function that, given a list with at least 2 elements and an order relationship, returns a triple with the two lowest elements in the list according to that order and a list with all the other elements

#12 - Function that, given a list of tuples (x,y), representing Cartesian coordinates of points, returns a list of pairs (r, θ), corresponding to the polar coordinates of those points

#13 - Function that, given two lists and an order relationship, and knowing that the lists are ordered by the order relationship, returns the ordered merge of both lists, maintaining any repetition

#14 - Function that, given a list of lists and a function, applies it to each element of the lists and concatenates them

#15 - Function that, given a tuple of lists and a binary function, returns a list with the results of applying the function to the pairs of elements in the same position of both lists

#16 - Function that, given a list of lists, a function and its neutral element, returns a list of numbers resulting in the reduction of each list through the function

if __name__ == "__main__":
    
    print("1 - isOdd ? [200:" + str(isOdd(200)) + ", 353:" + str(isOdd(353)) + ", 0:" + str(isOdd(0)) + ", -5:" + str(isOdd(-5)) + "]")
    print("2 - isPositive ? [200:" + str(isPositive(200)) + ", 353:" + str(isPositive(353)) + ", 0:" + str(isPositive(0)) + ", -5:" + str(isPositive(-5)) + "]")
    print("3 - isLower ? [|200| < |353|:" + str(isLower(200,353)) + ", |353| < |0|:" + str(isLower(353,0)) + ", |0| < |-5|:" + str(isLower(0, -5)) + ", |-5|<|3|:" + str(isLower(-5,3)) + "]")
    print("4 - polarCoordinates ? [(200,353):" + str(polarCoordinates((200,353))) + ", (353,0):" + str(polarCoordinates((353,0))) + ", (0,-5):" + str(polarCoordinates((0, -5))) + ", (-5,3):" + str(polarCoordinates((-5,3))) + "]")
    
    bothTrue = lambda x, y : x and y 
    arePositive = lambda x, y : True if x >= 0 and y >= 0 else False
    print("5 - compoundFunction ? [bothTrue(arePositive(200,353), isLower(353,0)):" + str(compoundFunction(arePositive, isLower, bothTrue, 200,353,0)) + ", isLower(bothTrue(353,0), arePositive(0,-5)):" + str(compoundFunction(bothTrue, arePositive, isLower, 353,0, -5)) + ", arePositive(isLower(0, -5), bothTrue(-5,3)):" + str(compoundFunction(isLower, bothTrue, arePositive, 0, -5, 3)) + "]")

    print("6 - areAll ? [isOdd([200,353,0]):" + str(areAll([200,353,0], isOdd)) + ", isPositive([353,0,-5]):" + str(areAll([353,0,-5], isPositive)) + ", isPositive([0,3,200]):" + str(areAll([0,3,200], isPositive)) + "]")
    print("7 - isOne ? [isOdd([200,353,0]):" + str(isOne([200,353,0], isOdd)) + ", isPositive([353,0,-5]):" + str(isOne([353,0,-5], isPositive)) + ", isOdd([0,3,200]):" + str(isOne([1,3,-5], isOdd)) + "]")
    print("8 - subgroup ? [[200,353,0],[-5,1,3]:" + str(subgroup([200,353,0], [-5,1,3])) + ", [353,0,-5],[200,0,353]:" + str(subgroup([353,0,-5], [200,0,353])) + ", [0,3,200],[3,353,35]:" + str(subgroup([0,3,200], [3,353,35])) + ", [3,200],[3,353,35,200]:" + str(subgroup([3,200], [3,353,35,200])) + "]")
    
    absLT = lambda x, y : True if abs(x) < abs(y) else False
    print("9 - lowest ? [absLT([200,353,0,-5,3]):" + str(lowest([200,353,0,-5,3], absLT)) + "]")
    
    print("10 - popLowest ? [absLT([200,353,0,-5,3]):" + str(popLowest([200,353,0,-5,3], absLT)) + "]")