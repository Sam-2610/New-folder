""" Write a program using functions to find greatest of numbers. """


def Greatest():
    num = int(input("Enter how many numbers you want to compare: "))
    numbers = []

    for i in range(num):
        x = int(input(f"Enter number {i + 1}: "))
        numbers.append(x)

    greatest = max(numbers)
    
    print("Numbers entered:", numbers)
    print("The Greatest Number Among Them is:", greatest)

Greatest()


