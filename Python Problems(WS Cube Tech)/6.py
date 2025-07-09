# Convert kilometer into miles
try:
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} kilometers is equal to {miles:.2f} miles")
except Exception as e:
    print("Please enter a valid number! Error:", e)
