#  Write a program to sum a list with 4 numbers. 

l = []
for i in range(4):
    x = int(input(f"Enter number {i+1}:"))
    l.append(x)
total = sum(l)
print("Sum of the list:", total)    
        