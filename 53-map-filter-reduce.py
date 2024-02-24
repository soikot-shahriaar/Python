# these are built-in functions that allow us to apply a function to a sequence of elements and return a new sequence.
# These functions are known as higher-order functions

## map()
# applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:


l = [1, 2, 4, 6, 4, 3]

# newl = []
# for item in l:
#   newl.append(cube(item))

newl = list(map(lambda x: x * x * x, l))
print(newl)


## filter
# filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.


def filter_function(a):
    return a > 2


newnewl = list(filter(filter_function, l))
print(newnewl)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]


# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
    return x + y


# higher-order function that applies a function to a sequence and returns a single value.
# It is a part of the functools module.
sum = reduce(mysum, numbers)

# Print the sum
print(sum)