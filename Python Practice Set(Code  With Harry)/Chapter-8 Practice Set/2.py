""" Write a python function to print multiplication table of a given number. """

def Multiplication_Table():
    x = int(input("Enter a number to print its multiplication table: "))
    for i in range(1, 11):
        print(f"{x} x {i} = {x * i}")

Multiplication_Table()
