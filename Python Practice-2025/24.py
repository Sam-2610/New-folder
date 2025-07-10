# Copy a File
with open("Poems.txt","r") as f:
    data = f.read()
    with open("firdt.txt","w") as d:
        content = d.write(data)