import pandas as pd
import numpy as np

# Create a NumPy array with 12 elements
data = np.array(['s', 'r', 'i', 'd', 'h', 'a', 'r'])

# Create a Pandas Series with the appropriate index (12 indices)
ser = pd.Series(data, index=[10, 11, 12, 13, 14, 15, 16])

# Print the value at index 18
print(ser[15])

#OUTPUT
# a