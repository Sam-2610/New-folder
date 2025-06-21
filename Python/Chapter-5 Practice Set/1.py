"""  Write a program to input eight numbers from the user and display all the unique 
numbers (once). """

a = set()
for i in range(8):
    x = int(input(f"Enter a number {i+1}:"))
    a.add(x)
print("Unique numbers are:", a)


