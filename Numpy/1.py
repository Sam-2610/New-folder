import numpy as np

""" # Types Basics

a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a.ndim)
print(a.size)

# Acess 

x = np.array([1,2,3,4,5])
print(x[3])

x[1] = 20

print(x)

# Matrices

c = np.array([[1,2,3],[6,7,8]])
print(c)
print(c[1,2])
print(np.transpose(c))

# Data Types

q = np.array([1,2,3,4,5])
w = np.array([1.0,2.3,3.4,4.6,5.8])

print(q.dtype)
print(w.dtype)

# In-built Arrays

z = np.zeros((2,3))
print(z)

f = np.full((4,3),1)
print(f)

t = np.random.rand(4,3)
print(t)

# Array Slice Indexing

i = "satyam"
print(i[1:4])

randInt = np.random.randint(10,size=(4,3))

print(randInt)

print(randInt[:2])
print(randInt[:1:2])
print(randInt[2:5,1:3])

# Basic Array Operations

x = np.array([[1,2,3],
              [6,7,8]])
y = np.array([[0,1,2],
              [4,5,6]])

print(x + y)
print(x - y)
print(x * y)
print(x @ y)
print(np.sqrt(x))
 """
# Broadcasting

b = np.ones([2,3])
print(5 * b)

n = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
m = np.array([0,1,2])

print(n + m)

# Avanced Numpy

np.insert(array,)
