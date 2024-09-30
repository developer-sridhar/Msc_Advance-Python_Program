import numpy as np

# Create a 3D NumPy array
a = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])

# Print the dimension of the given ndarray
print("Dimension of the given Ndarray =", a.ndim)

# Print the shape of the given ndarray
print("Shape of the given Ndarray =", a.shape)

# Print the size of the given ndarray
print("Size of the given Ndarray =", a.size)

# Print the data type of the given ndarray
print("Data type of the given Ndarray =", a.dtype)

# Print the size of each element in the ndarray
print("Size of each element in Ndarray =", a.itemsize)

#OUTPUT
# Dimension of the given Ndarray = 3
# Shape of the given Ndarray = (1, 4, 3)
# Size of the given Ndarray = 12
# Data type of the given Ndarray = int32
# Size of each element in Ndarray = 4