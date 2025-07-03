class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Example usage:
c1 = Complex(11, 22)
c2 = Complex(33, 55)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
