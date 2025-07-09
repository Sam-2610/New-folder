# Check A Number Prime or Not

try:
    x = int(input("Enter a number:"))
    i = 2
    while i <= x // 2:
        if x % i == 0:
            print(x, "is not a prime number.")
            break
        i += 1
    else:
        print(x, "is a prime number.")
except Exception as e:
    print("Please Enter a Valid Integer!",e)