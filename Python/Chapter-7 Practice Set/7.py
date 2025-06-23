"""  Write a program to print multiplication table of n using for loops in reversed 
order. """

x = int(input("Enter a number to print its multiplication table: "))
for i in range(10,0,-1):
    print(f"{x} x {i} = {x * i}")