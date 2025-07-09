""" Python Program to Add Two Numbers """
try:
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    print(f"The Sum of Two Numbers: {a + b}")
except Exception as e:
    print("Please Enter a Valid Integer!",e)