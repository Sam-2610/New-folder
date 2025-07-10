# Convert Decimal to Binary,Octal,HexaDecimal
try:
    d = int(input("Enter a Number in Decimal: "))
    print(f"The Decimal Number {d} in Binary is: {bin(d)}")
    print(f"The Decimal Number {d} in Octal is: {oct(d)}")
    print(f"The Decimal Number {d} in Hexadecimal is: {hex(d)}")
except Exception as e:
    print("Please Enter a Valid Integer!",e)