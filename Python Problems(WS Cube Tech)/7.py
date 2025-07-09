# Convert Celcius to Farenhite
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
except Exception as e:
    print("Please enter a valid number! Error:", e)
