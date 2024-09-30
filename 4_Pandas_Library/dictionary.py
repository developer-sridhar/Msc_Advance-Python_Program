import pandas as pd

# Create a dictionary
dictionary = {'A': 10, 'B': 63, 'C': 32}

# Create a Pandas Series from the dictionary
s = pd.Series(dictionary)

# Print the Series
print(s)


# OUTPUT:
# A    10
# B    63
# C    32
# dtype: int64
