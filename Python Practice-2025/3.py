"""  Find Square Root """

# Exception Handling

""" try:
    x = int(input("Enter a NUmber: "))
    sq = x ** 0.5
    print(sq)
except Exception as e:
    print("Please Enter a valid integer!",e) """

# Function

def sqaure_root(num1):
    return num1 ** 0.5

num1 = int(input("Enter a Number : "))
print(sqaure_root(num1))