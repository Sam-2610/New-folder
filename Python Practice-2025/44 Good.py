# Factorial of a Number Using Recrusion
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n - 1)

try:
    n = int(input("Enter a Number: "))
    if n < 0:
        print("Factorial does not exist for negative numbers.")
    else:
        print(f"The Factorial is {facto(n)}")
except Exception as e:
    print("Please Enter a Valid Integer!", e)
