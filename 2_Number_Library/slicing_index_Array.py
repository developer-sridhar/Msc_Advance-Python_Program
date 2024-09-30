import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 0, -4], [4, 6, 7, 0], [3, -7, 8, 5]])

# Slicing array: Select the first 2 rows and alternate columns (0 and 2)
temp = arr[:2, ::2]
print("Array with first 2 rows and alternate columns (0 and 2):\n", temp)

# Indexing array: Extract elements at specified indices
temp = arr[[0, 1, 2, 1], [3, 2, 1, 0]]
print("\nElements at indices (0,3), (1,2), (2,1), (1,0):\n", temp)


#OUTPUT
# Array with first 2 rows and alternate columns (0 and 2):
#  [[1 0]
#  [4 7]]

# Elements at indices (0,3), (1,2), (2,1), (1,0):
#  [-4  7 -7  4]