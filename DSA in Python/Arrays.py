import array as a

# Create an integer array
arr = a.array('i', [1, 2, 3, 4, 5, 6])

# Traversal
print("Traversing array:")
for i in arr:
    print(i)

# Insertion
arr.insert(2, 99)  # Insert 99 at index 2
print("After Insertion:", arr)

# Remove
arr.remove(99)  # Removes first occurrence of 99
print("After Removal:", arr)

# Searching
print("Index of 5:", arr.index(5))

# Sorting (only works on Python 3.10+ for array)
# Convert to list for safe sorting
sorted_arr = a.array('i', sorted(arr))
print("Sorted Array (Asc):", sorted_arr)

sorted_arr_desc = a.array('i', sorted(arr, reverse=True))
print("Sorted Array (Desc):", sorted_arr_desc)

# Merging two arrays
arr2 = a.array('i', [1, 2, 3])
merged = arr + arr2
print("Merged Array:", merged)

# Slicing
print("Sliced Array (index 1 to 2):", arr[1:3])

# Reversing (in-place, returns None)
arr.reverse()
print("Reversed Array:", arr)

# Count occurrences
print("Count of 2:", arr.count(2))

# Typecode of array
print("Typecode:", arr.typecode)

# Itemsize (in bytes)
print("Item size in bytes:", arr.itemsize)

# Buffer info (address, number of elements)
print("Buffer Info:", arr.buffer_info())

# Extend the array with another array
arr.extend(arr2)
print("After Extend:", arr)

# From list
li = [10, 20, 30]
arr.fromlist(li)
print("After fromlist:", arr)

# To list
arr_list = arr.tolist()
print("Converted to List:", arr_list)
