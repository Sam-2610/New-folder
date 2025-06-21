""" Write a program to accept marks of 6 students and display them in a sorted 
manner.  """

marks = []
for i in range(6):
    x =int(input(f"Enter the marks of student {i+1}:"))
    marks.append(x)
    marks.sort()
print("Marks list:", marks)