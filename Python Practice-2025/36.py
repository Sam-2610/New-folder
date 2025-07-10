# Transpose a Matrix

a = [[1,2,3],
     [4,1,2],
     [7,5,6]]

b = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i] = a[i][j]



for w in b:
    print(w)
