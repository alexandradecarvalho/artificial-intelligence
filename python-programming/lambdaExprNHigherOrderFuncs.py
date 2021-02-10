#1 - Lambda expression that, given an integer n, returns True if it's odd and False otherwise
isOdd = lambda n : n % 2 == 0

#2 - Lambda expression that, given a number n, returns True if it's positive and False otherwise

#3 - Lambda expression that, given two numbers x and y, returns True if |x| < |y| and False otherwise

#4 - Lambda expression that, given a pair (x,y), representing Cartesian coordinates of a point, returns a pair (r, θ), corresponding to the polar coordinates of that point

#5 - Function that, given 3 functions of two arguments each, f, g, and h, returns the function with 3 arguments x, y and z = h(f(x,y), g(y,z))

#6 - Function that, given a list and a unary boolean function, returns True if the function is positive for all elements in the list and False otherwise

#7 - Function that, given a list and a unary boolean function, returns True if the function is positive for at least one element in the list and False otherwise

#8 - Function that, given two lists, returns True if all elements in the first list are also in the second one, and False otherwise

#9 - Function that, given a not empty list and an order relationship, returns the lowest element on the list according to that order

#10 - Function that, given a not empty list and an order relationship, returns a tuple with the lowest element on the list according to that order and a list with all the other elements

#11 - Function that, given a list with at least 2 elements and an order relationship, returns a triple with the two lowest elements in the list according to that order and a list with all the other elements

#12 - Function that, given a list of tuples (x,y), representing Cartesian coordinates of points, returns a list of pairs (r, θ), corresponding to the polar coordinates of those points

#13 - Function that, given two lists and an order relationship, and knowing that the lists are ordered by the order relationship, returns the ordered merge of both lists, maintaining any repetition

#14 - Function that, given a list of lists and a function, applies it to each element of the lists and concatenates them

#15 - Function that, given a tuple of lists and a binary function, returns a list with the results of applying the function to the pairs of elements in the same position of both lists

#16 - Function that, given a list of lists, a function and its neutral element, returns a list of numbers resulting in the reduction of each list through the function

if __name__ == "__main__":
    print("isOdd ? [200:" + str(isOdd(200)) + ", 353:" + str(isOdd(353)) + ", 0:" + str(isOdd(0)) + ", -5:" + str(isOdd(-5)) + "]")
