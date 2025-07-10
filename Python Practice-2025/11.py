# Find Largest Among Three
try:
    l = []
    for i in range(3):
        x = int(input(f"Enter the Number {i + 1}: "))
        l.append(x)
    print(f" The Largest Among Three is: {max(l)}")
except Exception as e:
    print("Please Enter a Valid Integer!",e)
   
   

   