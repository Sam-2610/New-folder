"""  Write a program to print multiplication table of a given number using while loop. """


x = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(f"{x} x {i} = {x * i}")
    i += 1