""" Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. """

with open("poems.txt", "r") as f:
    content = f.read()
    if "twinkle" in content.lower():
        print("Yes, it contains the word 'twinkle'")
    else:
        print("No, it doesn't contain the word 'twinkle'")
