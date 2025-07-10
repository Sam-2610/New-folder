# Fabonai Sequence Using Recrusion
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
try:
    
    n = int(input("Enter a Number : "))
    if n < 0:
        print("Enter a Positive Number!")
    else:
        for i in range(n):
            print(fibo(i))

except Exception as e:
    print("Please Enter a Valid Integer!",e)