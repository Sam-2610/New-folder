# Sum of Natural Numbers Using Recursion
def nsum(n):
    if n <= 1:
        return n
    else:
        return n + nsum(n-1)
    
try:

    n = int(input("Enter the Terms: "))
    print("Sum:", nsum(n))
except Exception as e:
    print("Please Enter a Valid Integer!",e)
    