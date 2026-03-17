def increasin_pattern():
    n = int(input("Enter the Value of n : "))
    for i in range(n):
        for j in range(i + 1):
            print("*",end="")
        
        print()

increasin_pattern()