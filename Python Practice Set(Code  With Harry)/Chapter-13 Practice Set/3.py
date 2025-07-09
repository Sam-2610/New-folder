""" Write a program to filter a list of numbers which are divisible by 5.  """

l = [i for i in range(1, 101)]

def mul(x):
    return x % 5 == 0

print(list(filter(mul, l)))

