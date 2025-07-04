"""  Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
present, a message without exiting the program must be printed prompting the same. """

files = ['1.txt', '2.txt', '3.txt']

for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\nContents of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found.")
