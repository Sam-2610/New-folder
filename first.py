import numpy as np

a = np.array([[1,2,3],[9,8,7]])
b = np.array([[1,2,3],[4,5,6]])
c = np.array([[1.2,2.3,3.4],[4.5,5.6,6.7]])
d = np.array((1,2,3,4))
e = np.array((1,np.nan,3,np.nan))
f = np.array((1,np.nan,3,np.nan))
g = np.array((1,np.inf,3,np.inf))

# Modify a value
a[0,1] = 6 

print(a)
print(type(a))
print(a.shape)
print(a.ndim)
print(a.size)

print(a[0,0])

print(b)
print(b[0,2])
print(np.transpose(b))

print(a.dtype)
print(c.dtype)

# Creating special arrays
print(np.zeros((4,3)))
print(np.ones((4,3)))
print(np.full((4,3), 1))
print(np.eye(3,4))

# Random numbers
print(np.random.rand(4,3))

# Arithmetic operations
print(a + b)
print(a - b)
print(a * b)
print(np.sqrt(a))
print(np.sum(a, axis=0))

# Insert, append, concatenate
print(np.insert(a, 0, 4, axis=0))
print(np.append(b, [[7,8,9]], axis=0)) 
print(np.concatenate((a,b), axis=0))
print(np.delete(a, [0], axis=None))
print(np.vstack((a,b)))
print(np.hstack((b,a)))

# Split arrays
print(np.split(d, 2))      # Split 1D array
print(np.hsplit(a, 3))     # Split into 3 vertical slices (columns)
print(np.vsplit(a, 2))     # Split into 2 horizontal slices (rows)

# NaN and Inf handling
print(np.isnan(e))
print(np.nan_to_num(f))
print(np.isinf(g))
