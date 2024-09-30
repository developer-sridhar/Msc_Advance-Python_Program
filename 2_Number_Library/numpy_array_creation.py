import numpy as np

# Create a NumPy array
npArray = np.array([1.3, 2.6, 3.4, 4.3, 5.4, 6.8, 7.2, 8.5, 9.3], dtype=float)

# Print contents of the NumPy array
print("Contents of the npArray:", npArray)

# Slicing examples
print(npArray[2:5])    # Elements from index 2 to 4
print(npArray[:4])     # First four elements
print(npArray[5:])     # Elements from index 5 to the end
print(npArray[:])      # All elements

# Tuple to array conversion
tuple1 = ([8.5, 4.2, 6], [1, 2, 3.5]) 
array2 = np.asarray(tuple1)
print(array2)

# Another NumPy array
s = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s[2:5])    # Elements from index 2 to 4
print(s[:4])     # First four elements
print(s[6:])     # Elements from index 6 to the end
print(s[:])      # All elements


#OUTPUT
# Contents of the npArray: [1.3 2.6 3.4 4.3 5.4 6.8 7.2 8.5 9.3]
# [3.4 4.3 5.4]
# [1.3 2.6 3.4 4.3]
# [6.8 7.2 8.5 9.3]
# [1.3 2.6 3.4 4.3 5.4 6.8 7.2 8.5 9.3]
# [[8.5 4.2 6. ]
#  [1.  2.  3.5]]
# [2 3 4]
# [0 1 2 3]
# [6 7 8 9]
# [0 1 2 3 4 5 6 7 8 9]