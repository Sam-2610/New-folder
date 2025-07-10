# Print Power of 2
try:
    n = int(input("Enter a Terms: "))
    result = list(map(lambda x : 2 ** x, range(1,n+1)))
    print(f"The Power of 2 in {n} terms is : {result}")
except Exception as e:
    print("Please Enter a Valid Integer!")