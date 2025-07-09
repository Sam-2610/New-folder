""" A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.   """

with open("hello.txt", "r") as f:
    content = f.read()
    if "Donkey" in content.lower():
        c = content.replace("Donkey", "#####")
        with open("hello.txt", "w") as f:
           f.write(c)
