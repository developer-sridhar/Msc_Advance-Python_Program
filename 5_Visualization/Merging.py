import pandas as pd

# Define the first dictionary containing employee data
data1 = {
    'key': ['CS0', 'CS1', 'CS2', 'CS3'],
    'Name': ['Sridhar', 'Yuvaraj', 'Bharath', 'Richard'],
    'Age': [27, 24, 22, 32]  # Ensure ages are integers
}

# Define the second dictionary containing employee data
data2 = {
    'key': ['CS0', 'CS1', 'CS2', 'CS3'],  # Ensure keys match for merging
    'Address': ['Maduravoyal', 'Nerkundram', 'Koyambedu', 'Anna Nagar'],
    'Qualification': ['Btech', 'BA', 'Bcom', 'BBA']  # Corrected 'Bhons' to 'BBA'
}

# Convert the dictionaries into DataFrames
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)

# Print both DataFrames
print("DataFrame 1:\n", df, "\n\nDataFrame 2:\n", df1)

# Using .merge() function with one unique key combination
res = pd.merge(df, df1, on='key')

# Print the result of the merge
print("\nMerged DataFrame:\n", res)


# OUTPUT
# DataFrame 1:
#     key     Name  Age
# 0  CS0  Sridhar   27
# 1  CS1  Yuvaraj   24
# 2  CS2  Bharath   22
# 3  CS3  Richard   32

# DataFrame 2:
#     key       Address Qualification
# 0  CS0  Maduravoyal         Btech
# 1  CS1    Nerkundram            BA
# 2  CS2     Koyambedu          Bcom
# 3  CS3    Anna Nagar           BBA

# Merged DataFrame:
#     key     Name  Age       Address Qualification
# 0  CS0  Sridhar   27  Maduravoyal         Btech
# 1  CS1  Yuvaraj   24    Nerkundram            BA
# 2  CS2  Bharath   22     Koyambedu          Bcom
# 3  CS3  Richard   32    Anna Nagar           BBA