import numpy as np

# Create a NumPy array
x = np.array([[0, 1], [2, 3]])

# Print the original array
print("Original array:")
print(x)

# Print the minimum element of the array
print("Minimum element of an array:")
print(np.min(x))

# Print the maximum element of the array
print("Maximum element of an array:")
print(np.max(x))

# Print the sum of all elements
print("Sum of all elements:")
print(np.sum(x))

# Print the sum of each column
print("Sum of each column:")
print(np.sum(x, axis=0))

# Print the sum of each row
print("Sum of each row:")
print(np.sum(x, axis=1))

# Print the cumulative sum of the array
print("Cumulative sum of an array:")
print(np.cumsum(x))


#OUTPUT
# Original array:
# [[0 1]
#  [2 3]]
# Minimum element of an array:
# 0
# Maximum element of an array:
# 3
# Sum of all elements:
# 6
# Sum of each column:
# [2 4]
# Sum of each row:
# [1 5]
# Cumulative sum of an array:
# [0 1 3 6]