""" Write a program to mine a log file and find out whether it contains ‘python’.  """

with open("server.log","r") as f:
    data = f.read()
    if "python" in data.lower():
        print("Python is present in the file")
