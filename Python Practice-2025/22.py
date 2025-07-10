# Check if a Number is Divisible by another Number
try:
    n = int(input("Enter the Divident: "))
    x = int(input("Enter the Divisor: "))
    if x < 0 or n < 0:
        print("Please Enter a Positive Number!")
    elif n % x == 0:
        print(f"The Number {n} is Divisible by {x}")
    else:
        print(f"The Number {n} is Not Divisible by {x}")
except Exception as e:
    print("Please Enter a Valid Integer!")