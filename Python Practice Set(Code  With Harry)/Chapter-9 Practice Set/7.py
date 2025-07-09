"""  Write a program to make a copy of a text file “this. txt”  """

with open("this.txt", "r") as f:
    content = f.read()
    with open("copy.txt", "w") as f1:
        f1.write(content)
        print("Content copied successfully")
   