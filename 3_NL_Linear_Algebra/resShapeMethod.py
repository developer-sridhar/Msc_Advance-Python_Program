import numpy as geek

# Create an original array
array1 = geek.arange(4)
print("Original array:\n", array1)

# Reshape the array into 2 rows and 2 columns
array2 = geek.arange(4).reshape(2, 2)
print("\nArray reshaped with 2 rows and 2 columns:\n", array2)


# OUTPUT
# Original array:
#  [0 1 2 3]

# Array reshaped with 2 rows and 2 columns:
#  [[0 1]
#  [2 3]]