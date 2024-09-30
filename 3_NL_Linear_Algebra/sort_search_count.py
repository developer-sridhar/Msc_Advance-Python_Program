import numpy as np

# Define the array
Arr = np.array([[1, 20, 5], [21, 4, 3], [11, 5, 50]])

# Sort the array
SortedArr = np.sort(Arr, axis=None)  # Sorting all elements in the array

# Print statements
print("Hello world")
print("Original Array:")
print(Arr)

print("\nSorted Array:")
print(SortedArr)

# Count the sum of the array elements
CountingArr = np.sum(Arr)
print(CountingArr)  # Fixed the capitalization of print


#OUTPUT
# Hello world
# Original Array:
# [[ 1 20  5]
#  [21  4  3]
#  [11  5 50]]

# Sorted Array:
# [ 1  3  4  5  5 11 20 21 50]
# 120