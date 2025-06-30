""" Create a class “Programmer” for storing information of few programmers 
working at Microsoft. """

class Programmer:
    company = "Microsoft"  

    def __init__(self, name, salary, shift):
        self.name = name
        self.salary = salary
        self.shift = shift


rohan = Programmer("Rohan", 25000, "Morning")
roro = Programmer("Roro", 30000, "Night")
sam = Programmer("Sam", 28000, "Evening")


print(f"Name: {rohan.name}, Company: {rohan.company}, Salary: {rohan.salary}, Shift: {rohan.shift}")
print(f"Name: {roro.name}, Company: {roro.company}, Salary: {roro.salary}, Shift: {roro.shift}")
print(f"Name: {sam.name}, Company: {sam.company}, Salary: {sam.salary}, Shift: {sam.shift}")
