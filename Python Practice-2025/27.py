# Count Number of lines in a File
with open("first.txt", "r") as f:
    lines = f.readlines()
    count = len(lines)

if count > 0:
    print(f"The number of lines in the file is: {count}")
else:
    print("File has no lines!")
