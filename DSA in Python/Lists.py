# append(): Adds an element to the end of the list.

lst = [1, 2, 3]
lst.append(4)  # [1, 2, 3, 4]

# insert(): Inserts an element at a specific index.

lst.insert(1, 10)  # [1, 10, 2, 3]

# extend(): Adds multiple elements to the list.

lst.extend([5, 6])  # [1, 10, 2, 3, 5, 6]


# pop(): Removes and returns the element at a specific index (default is the last element).

lst.pop()  # Removes 6
lst.pop(1)  # Removes 10

# remove(): Removes the first occurrence of a specific value.

lst.remove(2)  # [1, 3, 5]

# clear(): Removes all elements from the list.

lst.clear()  # []


# index(): Finds the index of the first occurrence of a value.

lst = [1, 2, 3, 2]
lst.index(2)  # 1

# count(): Counts the occurrences of a value.

lst.count(2)  # 2


# sort(): Sorts the list in ascending order (in-place).

lst.sort()  # [1, 2, 3, 5]

# sorted(): Returns a new sorted list without modifying the original.

sorted_lst = sorted(lst, reverse=True)  # [5, 3, 2, 1]

# reverse(): Reverses the list in-place.

lst.reverse()  # [5, 3, 2, 1]

# copy(): Creates a shallow copy of the list.
new_lst = lst.copy()

# List Comprehension: Create new lists using concise syntax.

squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# zip(): Combine multiple lists element-wise.

list1 = [1, 2]
list2 = [3, 4]
zipped = list(zip(list1, list2))  # [(1, 3), (2, 4)]

# map(): Apply a function to all elements.

doubled = list(map(lambda x: x*2, lst))  # [10, 6, 4, 2]


# in and not in: Check if an element exists in the list.

3 in lst  # type: ignore # True
7 not in lst  # type: ignore # True

# Slicing

lst = [1, 2, 3, 4, 5]
print(lst[1:4])  # [2, 3, 4]
print(lst[::-1]) # Reverse the list

# Unpacking

a, b, c = [1, 2, 3]

# Emurate()

for i, val in enumerate(lst):
    print(i, val)

# Filtering using List Compreshions

even = [x for x in lst if x % 2 == 0]

# Flating in 2d list

matrix = [[1,2],[3,4]]
flat = [item for sublist in matrix for item in sublist]
