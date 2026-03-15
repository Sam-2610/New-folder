""" Check if number is even or odd """
# Exceptional Handling 

""" try:
    x =int(input("Enter a number: "))
    if x % 2 == 0:
        print(f"The Number {x} is Even!")
    else:
        print(f"The Number {x} is Odd!")
except Exception as e:
    print("Please Enter a Valid Integer!",e) """

# Function

def check(a):
    if a % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

a = int(input("Enter a Number : "))
print(check(a))