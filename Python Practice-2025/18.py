# Reverse a Number
try:
    n = int(input("Enter a Number: "))
    reversed_num = int(str(n)[::-1]) if n >= 0 else -int(str(-n)[::-1])
    print(f"Reversed Number: {reversed_num}")
except ValueError:
    print("Please enter a valid integer!")
