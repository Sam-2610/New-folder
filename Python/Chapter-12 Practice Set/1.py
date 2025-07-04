""" . Write a program to print third, fifth and seventh element from a list using enumerate 
function. """

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for i, item in enumerate(list1):
    if i in [2, 4, 6]:
        print(f"{i+1}th element: {item}")
