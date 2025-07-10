class Calculator:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def sqrt(self, num):
        return num ** 0.5

# Create a single instance
calc = Calculator()

# Call methods with input values
print("Square of 5:", calc.square(5))
print("Cube of 3:", calc.cube(3))
print("Square Root of 49:", calc.sqrt(49))
