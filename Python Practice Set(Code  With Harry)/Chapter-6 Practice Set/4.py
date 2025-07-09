""" Write a program to find whether a given username contains less than 10 
characters or not.  """


username = input("Enter Your Username:")

if len(username) <= 10:
    print("Username is less than 10 characters.\n Username Created")
else:
    print("Username is more than 10 characters.\n Username not Created")    