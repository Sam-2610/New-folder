def simple_pattern():
    n = int(input("Enter the Value of n : "))
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

simple_pattern()