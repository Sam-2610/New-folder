def pattern1():
    n = 5
    for i in range(n):
        for j in range(n):
            print("*",end="")

        print()

def pattern2():
    n = 5
    for i in range(n):
        for j in range(i + 1):
            print("*",end="")

        print()

def pattern3():
    n = 5
    for i in range(n):
        for j in range(i,n):
            print("*",end="")

        print()

def pattern4():
    n = 5
    for i in range(n):
        for j in range(1, i + 2):
            print(j,end="")

        print()

def pattern5():
    n = 5
    for i in range(1,n):
        for j in range(i):
            print(i,end="")

        print()

pattern1()
pattern2()
pattern3()
pattern4()
pattern5()

