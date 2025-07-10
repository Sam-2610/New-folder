# Factorial Of a Number

import math as m
try:
    num = int(input("Enter a Number: "))
    print(f"The Factorial of the Number {num} is {m.factorial(num)}")
except Exception as e:
    print("Please Enter a Valid Integer",e)

