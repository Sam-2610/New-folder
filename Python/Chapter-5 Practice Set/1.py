"""  Write a program to input eight numbers from the user and display all the unique 
numbers (once). """

s = set()
for i in range(8):
    x = int(input(f"Enter a number {i+1}:"))
    s.add(x)
print("Set of numbers:", s.intersection(s))

