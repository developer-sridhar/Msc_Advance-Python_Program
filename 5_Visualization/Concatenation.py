import pandas as pd

# Define the first dictionary containing employee data
data1 = {
    'Name': ['Sridhar', 'Yuvaraj', 'Bharath', 'Richard', 'Muthukumar'],
    'Age': [20, 20, 20, 20, 20],  # Ensure ages are integers
    'Address': ['Chennai', 'Madurai', 'Vellore', 'Kanchipuram', 'Kumbakonam'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'NIL']  # Ensure quotes are correct
}

# Define the second dictionary containing employee data
data2 = {
    'Name': ['Dinesh', 'Dhanush', 'Thrisha', 'Jesse'],
    'Age': [20, 20, 20, 20],  # Ensure ages are integers
    'Address': ['Thiruvanamalai', 'Thiruvallur', 'Kodaikanal', 'Ooty'],
    'Qualification': ['Btech', 'BA', 'Bcom', 'BBA']  # Corrected 'Bhons' to 'BBA'
}

# Convert the dictionaries into DataFrames
df1 = pd.DataFrame(data1, index=[0, 1, 2, 3, 4])
df2 = pd.DataFrame(data2, index=[5, 6, 7, 8])  # Corrected index to avoid overlap

# Print both DataFrames
print("DataFrame 1:\n", df1, "\n\nDataFrame 2:\n", df2)

# Using pd.concat() method to combine the DataFrames
frames = [df1, df2]
res1 = pd.concat(frames, ignore_index=True)

# Print the concatenated DataFrame
print("\nConcatenated DataFrame:\n", res1)


#OUTPUT
# DataFrame 1:
#           Name  Age      Address Qualification
# 0     Sridhar   20      Chennai           Msc
# 1     Yuvaraj   20      Madurai            MA
# 2     Bharath   20      Vellore           MCA
# 3     Richard   20  Kanchipuram           Phd
# 4  Muthukumar   20   Kumbakonam           NIL 

# DataFrame 2:
#        Name  Age         Address Qualification
# 5   Dinesh   20  Thiruvanamalai         Btech
# 6  Dhanush   20     Thiruvallur            BA
# 7  Thrisha   20      Kodaikanal          Bcom
# 8    Jesse   20            Ooty           BBA

# Concatenated DataFrame:
#           Name  Age         Address Qualification
# 0     Sridhar   20         Chennai           Msc
# 1     Yuvaraj   20         Madurai            MA
# 2     Bharath   20         Vellore           MCA
# 3     Richard   20     Kanchipuram           Phd
# 4  Muthukumar   20      Kumbakonam           NIL
# 5      Dinesh   20  Thiruvanamalai         Btech
# 6     Dhanush   20     Thiruvallur            BA
# 7     Thrisha   20      Kodaikanal          Bcom
# 8       Jesse   20            Ooty           BBA