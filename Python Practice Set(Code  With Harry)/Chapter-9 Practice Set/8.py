"""  Write a program to find out whether a file is identical & matches the content of 
another file.  """

with open("this.txt", "r") as f:
    data = f.read()
    with open("poems.txt", "r") as f2:
        content = f2.read()
        if data.lower().strip() == content.lower().strip():
            print("Both files are same")
        else:
            print("Both files are not same")
            