""" Create a class “Programmer” for storing information of few programmers 
working at Microsoft. """

class Programmer:
    Company = "Microsoft"

    def __init__(self,language,salary):
        self.language = language
        self.salary = salary


Sam = Programmer("C#",20000)
Alex = Programmer("Python",30000)

print(f"Sam Works in the Company of {Sam.Company} his language is {Sam.language} and Salary is {Sam.salary}")
print(f"Alex Works in the Company of {Alex.Company} his language is {Alex.language} and Salary is {Alex.salary}")