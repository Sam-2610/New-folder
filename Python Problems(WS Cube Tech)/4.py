# Find the area of triangle
try:
    b = int(input("Enter the base of triangle: "))
    h = int(input("Enter the height of triangle: "))
    print(f"The Area of the triangle is: {0.5*b*h}")
except Exception as e:
    print("Please Enter a Valid integer!",e)
    
    