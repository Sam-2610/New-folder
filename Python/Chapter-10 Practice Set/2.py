""" Write a class “Calculator” capable of finding square, cube and square root of a 
number. """

class Calculator:
    def sqrt(self):
        num = 22
        c = num**2
        return c 
    
    def cube(self):
        number = 11
        x = number**3
        return x


    def sqroot(self):
        n = 16
        b = n**0.5
        return b
    


t = Calculator()
print(t.sqrt())

v = Calculator()
print(v.cube())

z = Calculator()
print(z.sqroot())
    
   

        



