# Check for leap Year
try:
    x = int(input("Enter a Year: "))
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print(f"The Year {x} is Leap Year!")
    else:
        print(f"The Year {x} is not a Leap Year!")
except Exception as e:
    print("Please Enter a Valid Year!")