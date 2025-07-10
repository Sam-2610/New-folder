# Find Square Root
try:
    x = int(input("Enter a NUmber: "))
    sq = x ** 0.5
    print(sq)
except Exception as e:
    print("Please Enter a valid integer!",e)