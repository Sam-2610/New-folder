# Check if number is even or odd
try:
    x =int(input("Enter a number: "))
    if x % 2 == 0:
        print(f"The Number {x} is Even!")
    else:
        print(f"The Number {x} is Odd!")
except Exception as e:
    print("Please Enter a Valid Integer!")