# Find the HCF
import math as m
try:
    x = int(input("Enter a Number: "))
    y = int(input("Enter another Number: "))
    print(f"The HCF of Number {x} and {y} is {m.gcd(x,y)}")
except Exception as e:
    print("Please Enter a Valid Integer!")