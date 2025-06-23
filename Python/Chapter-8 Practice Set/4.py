""" Write a python program using function to convert Celsius to Fahrenheit.  """

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

celsius_to_fahrenheit()
