"""  Create a class ‘Employee’ and add salary and increment properties to it. """

class Employee:
    


    def __init__(self,salary):
        self.salary = salary

    @property
        
    def incre(self):
        return str((self.salary) + 1000)
        


E1 = Employee(1000)
print(E1.incre)

E1.salary = 5000
print(E1.incre)

E1.salary = 6000
print(E1.incre)