"""  A list contains the multiplication table of 7. write a program to convert it to vertical 
string of same numbers. """
l = [7 * m for m in range(1, 11)]
vertical_string = "\n".join(str(i) for i in l)
print(vertical_string)
