""" Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. """


with open("table.txt", "w") as f:
    for i in range(2, 21):
        f.write(f"Table of {i}:\n")
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
        f.write("\n")  # Adds a blank line after each table


