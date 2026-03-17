def decreasin_pattern():
    n = int(input("Enter the Value of n : "))
    for i in range(n):
        for j in range(i,n):
            print("*",end="")

        print()

decreasin_pattern()