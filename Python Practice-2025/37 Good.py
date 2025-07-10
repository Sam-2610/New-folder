a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[3, 2, 1],
     [6, 5, 4],
     [9, 8, 7]]

# Result matrix of dimensions (3x3)
c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Matrix multiplication logic
for i in range(len(a)):            # row of a
    for j in range(len(b[0])):     # column of b
        for k in range(len(b)):    # or len(a[0])
            c[i][j] += a[i][k] * b[k][j]

# Print result
for row in c:
    print(row)
