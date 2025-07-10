# Find sum of Natural Numbers
try:
    n = int(input("Enter a Number: "))
    if n < 0:
        print("Please Enter a Positive NUmber!")
    else:
        total = n * (n + 1) // 2
        print(f"The Sum of Natural Numbers till {n} is {total}")
except Exception as e:
    print("Please Enter a Valid Integer",e)
