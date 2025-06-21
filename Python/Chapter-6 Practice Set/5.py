""" Write a program which finds out whether a given name is present in a list or not. """


l = ['Sam', 'John', 'Sara', 'Tom', 'Jerry']
x = input("Enter the name: ")

found = False
for i in l:
    if i.lower() == x.lower():
        print(f"{x} is present in the list.")
        found = True
        break

if not found:
    print(f"{x} is not present in the list.")

        
    
       
  