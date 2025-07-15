import random

try:
    userch = int(input("Enter Your Guessing Number:"))
    comch = random.randrange(1,101)
    print(f"Your Guess:{userch}")
    print(f"The Number:{comch}")
    if userch == comch:
        print("You Guessed it!")
    else:
        print("Try Again")
        
except Exception as e:
    print("Error",e)