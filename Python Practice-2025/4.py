"""  Find the area of triangle """

# Exception Handling

""" try:
    b = int(input("Enter the base of triangle: "))
    h = int(input("Enter the height of triangle: "))
    print(f"The Area of the triangle is: {0.5*b*h}")
except Exception as e:
    print("Please Enter a Valid integer!",e) """

# Function

def Area_of_Triangle(b,h):
    return 0.5*b*h

b = int(input("Enter the Base of Triangle : "))
h = int(input("Enter the Height : "))
print(Area_of_Triangle(b,h))
    
    