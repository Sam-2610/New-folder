# Display Calendar
import calendar as c
try:
    y = int(input("Enter a Year : "))
    m = int(input("Enter a Month : "))
    print(f"The Calendar is : {c.month(y,m)}")
except Exception as e:
    print("Please Provide Valid Input!!")