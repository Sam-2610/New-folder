""" Write a program to find the greatest of four numbers entered by the user.  """

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

greatest = max(a, b, c, d)
print(f"{greatest} is the greatest number.")
