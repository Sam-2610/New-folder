""" Write a program to detect double space in a string.  """

str1 = input("Enter a string: ")
if "  " in str1:
    print("Double space detected.")
else:
    print("No double space detected.")