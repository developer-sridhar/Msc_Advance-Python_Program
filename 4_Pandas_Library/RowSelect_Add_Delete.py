import pandas as pd

# Define a dictionary containing student data
data = {
    'name': ['Sridhar', 'Dhanush', 'Santhosh', 'Iyappan', 'Tamilarasan'],
    'address': ['Maduravoyal', 'Mogappair West', 'Porur', 'Vanagaram', 'Redhills'],
    'tamil': [90, 88, 76, 44, 22],
    'english': [88, 90, 65, 44, 35],
    'maths': [45, 67, 89, 98, 67]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Select and print the 4th row
print("\nAfter selecting 4th row:")
print(df.iloc[3])

# Create a new entry
new_entry = {
    'name': 'Yuvaraj', 
    'address': 'Nerkundram',
    'tamil': 88,
    'english': 90,
    'maths': 67
}

# Append the new entry to the DataFrame using pd.concat
df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

# Print the updated DataFrame
print("\nUpdated DataFrame after appending a new entry:")
print(df)

# Delete the second row (index 1)
print("\nAfter deleting the second row:")
df = df.drop(df.index[1])
print(df)



# OUTPUT:
#     Original DataFrame:
#           name         address  tamil  english  maths
# 0      Sridhar     Maduravoyal     90       88     45
# 1      Dhanush  Mogappair West     88       90     67
# 2     Santhosh           Porur     76       65     89
# 3      Iyappan       Vanagaram     44       44     98
# 4  Tamilarasan        Redhills     22       35     67

# After selecting 4th row:
# name         Iyappan
# address    Vanagaram
# tamil             44
# english           44
# maths             98
# Name: 3, dtype: object

# Updated DataFrame after appending a new entry:       
#           name         address  tamil  english  maths
# 0      Sridhar     Maduravoyal     90       88     45
# 1      Dhanush  Mogappair West     88       90     67
# 2     Santhosh           Porur     76       65     89
# 3      Iyappan       Vanagaram     44       44     98
# 4  Tamilarasan        Redhills     22       35     67
# 5      Yuvaraj      Nerkundram     88       90     67

# After deleting the second row:
#           name      address  tamil  english  maths
# 0      Sridhar  Maduravoyal     90       88     45
# 2     Santhosh        Porur     76       65     89
# 3      Iyappan    Vanagaram     44       44     98
# 4  Tamilarasan     Redhills     22       35     67
# 5      Yuvaraj   Nerkundram     88       90     67