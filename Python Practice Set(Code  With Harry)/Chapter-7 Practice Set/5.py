""" Write a program to find the sum of first n natural numbers using while loop. """

l = []
n = 1
while n <= 10:
    l.append(n)
    n += 1
print("Sum of first n natural numbers:", sum(l))