""" Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. """

dict = {}
for  i in range(4):
    x = input(f"Enter the keys {i+1}:")
    y = input(f"Enter the values {i+1}:")
    dict[x] = y
print("Dictionary:", dict)
