'''A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams.'''


str = input("Enter a string: ")

if str.lower() == "make a lot of money":
    print("This is a Spam Message")
elif str.lower() == "buy now":
    print("This is a Spam Message")
elif str.lower() == "subscribe this":
    print("This is a Spam Message")
elif str.lower() == "click this":
    print("This is a Spam Message")
else:
    print("This is not a spam Message")



    