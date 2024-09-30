import pandas as pd

# Initialize a DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], columns=['a', 'b', 'c'])

# Convert DataFrame to NumPy array
arr = df.to_numpy()

# Print the NumPy array
print('\nNumpy Array \n-----------------\n', arr)

# Print the type of the array
print(type(arr))


# OUTPUT
# Numpy Array
# -----------------
#  [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# <class 'numpy.ndarray'>