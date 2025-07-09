# Multiplication Generator
try:
    x = int(input("Enter a Number: "))
    for i in range(1,11):
        print(f"{i} * {x} = {x*i}")
except Exception as e:
    print("Please Enter a Valid Integer!",e)
