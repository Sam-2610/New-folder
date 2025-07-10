# Check Armstrong Number
try:
    num = int(input("Enter a number: "))
    total = 0
    temp = num
    power = len(str(num))  # Number of digits

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    if total == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except Exception as e:
    print("Please enter a valid integer!", e)

