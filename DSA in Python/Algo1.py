""" Algorithm: Find The Lowest Value in an Array """

import array
arr = array.array('i',[1,2,3,4,5,44,33])
minval = arr[0]
for i in arr:
    if i < minval:
        minval = i

print(f"lowest Value:{minval}")