# Print Sum of Two Matrices
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[3,2,1],
     [6,5,4],
     [9,8,7]]

c = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]
        
        

for d in c:
    print(d)


   