with open("Hello.txt", "r") as f:
    data = f.readlines()
    c = 0
    for i in data:
        c += 1
        if "python" in i.lower():
            print("Python is present in line No.", c)

