""" Write a python function which converts inches to cms. """

def conversion():
    inches = float(input("Enter the length in inches: "))
    cm = inches * 2.54

    print(f"Inches into centimeters: {cm}cm")

conversion()