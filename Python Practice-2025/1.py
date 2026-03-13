""" Python Program to Add Two Numbers """
# Exceptional Handling
""" try:
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    print(f"The Sum of Two Numbers: {a + b}")
except Exception as e:
    print("Please Enter a Valid Integer!",e) """

# Function

def sum(a,b):
    return a + b

a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
print(f"The sum of two Numbers is : {sum(a,b)}")