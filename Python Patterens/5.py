def rightside_increasing():
    n = int(input("Enter the Value of n : "))
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i + 1):
            print("*",end="")

        print()

rightside_increasing()