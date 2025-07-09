# Find Factors of a Number
try:
    l = []
    x = int(input("Enter a Number: "))
    for i in range(1, x + 1):
        if x % i == 0:
            l.append(i)
    print(f"The factors of {x} are: {l}")
except Exception as e:
    print("Please Enter a Valid Integer!", e)
