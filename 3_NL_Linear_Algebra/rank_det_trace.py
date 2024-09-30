import numpy as np

# Create a NumPy matrix
mat = np.array([[50, 29], [30, 44]])

# Print the Numpy matrix
print("Numpy matrix is:")
print(mat)

# Calculate the determinant
det = np.linalg.det(mat)
print("\nDeterminant of the given 2x2 matrix:")
print(int(det))

# Calculate the rank
rank = np.linalg.matrix_rank(mat)
print("Rank of the given matrix is:", rank)

# Calculate the trace
print("Trace of the matrix:", mat.trace())



#OUTPUT
# Numpy matrix is:
# [[50 29]
#  [30 44]]

# Determinant of the given 2x2 matrix:
# 1330
# Rank of the given matrix is: 2
# Trace of the matrix: 94