"""  Write a program to find the maximum of the numbers in a list using the reduce 
function. """

from functools import reduce
l = [1,2,3,45,34,65]
def lar(x, y):
    return x if x > y else y

print(reduce(lar, l))
        