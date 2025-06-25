""" Bubble Sort in Arrays """
arr = []
x = int(input("Enter the number of numbers you want to sort: "))

# Taking input
for v in range(x):
    z = int(input(f"Enter Number {v+1}: "))
    arr.append(z)

# Bubble Sort
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
