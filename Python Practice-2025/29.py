# Print the Fibonacci Sequence
try:
    num = int(input("Enter a Number: "))
    a, b = 0, 1
    l = []

    if num <= 0:
        print("Please enter a positive number.")
    elif num == 1:
        l = [a]
    else:
        l = [a, b]
        for _ in range(2, num):
            c = a + b
            a, b = b, c
            l.append(c)

    print(f"The first {num} numbers of the Fibonacci sequence are: {l}")

except Exception as e:
    print("Please Enter a Valid Integer!", e)
