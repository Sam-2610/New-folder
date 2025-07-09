# Check if a number is positive,negative or zero
try:
    x = int(input("Enter a Number: "))
    if x < 0:
        print(f"The Number {x} is Negative!")
    elif x > 0:
        print(f"The Number {x} is Positive!")
    else:
        print(f"The Number is Zero!")
except Exception as e:
    print("Please Enter a Valid Integer!",e)