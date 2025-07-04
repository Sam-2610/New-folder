""" Store the multiplication tables generated in problem 3 in a file named Tables.txt. """

def mul():
    x = int(input("Enter a Number: "))
    table = ""
    for i in range(1, 11):
        line = f"{x} * {i} = {x * i}\n"
        table += line
    return table

data = mul()

with open("Tables.txt", "w") as f:
    f.write(data)

print("Multiplication table saved to Tables.txt")



   



