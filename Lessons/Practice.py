# 1st Approach

""" import numpy as np

arr = np.array([1, 2, 3, 4, 5])

current_min = arr[0]

for x in arr:
    if x < current_min:
        current_min = x  # use assignment (=), not equality (==)

print(current_min)  # prints the minimum value
print(arr) """

# 2ns Approach

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr.min())
