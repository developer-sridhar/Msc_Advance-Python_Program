import pandas as pd  # Corrected import statement

# Define the first dictionary containing employee data
data1 = {
    'key': ['CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'CS8'],
    'Name': ['Sridhar', 'Yuvaraj', 'Bharath', 'Richard', 'Dinesh', 'Dhanush', 'Muthukumar', 'Thrisha', 'Jesse'],
    'Age': [20, 21, 22, 23, 24, 25, 26, 27, 28]  # Ensured ages are integers and matched length
}

# Define the second dictionary containing employee data
data2 = {
    'key': ['CS0', 'CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'CS8'],  # Ensure keys match for merging
    'Address': ['Maduravoyal', 'Nerkundram', 'Koyambedu', 'Anna Nagar', 'Thiruvanamalai', 'Thiruvallur', 'Kodaikanal', 'Ooty', 'Pondicherry'],
    'Qualification': ['Btech', 'BA', 'Bcom', 'BBA', 'MSc', 'PhD', 'MCA', 'MBA', 'MSc']  # Updated qualifications to match length
}

# Convert the dictionaries into DataFrames
df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2)  

# Print both DataFrames
print("DataFrame 1:\n", df1, "\n\nDataFrame 2:\n", df2)

# Using pd.concat() method to combine the DataFrames with inner join
res2 = pd.concat([df1, df2], axis=1, join='inner')

# Print the concatenated DataFrame
print("\nConcatenated DataFrame with inner join:\n", res2)



# OUTPUT
# DataFrame 1:
#     key        Name  Age
# 0  CS0     Sridhar   20
# 1  CS1     Yuvaraj   21
# 2  CS2     Bharath   22
# 3  CS3     Richard   23
# 4  CS4      Dinesh   24
# 5  CS5     Dhanush   25
# 6  CS6  Muthukumar   26
# 7  CS7     Thrisha   27
# 8  CS8       Jesse   28

# DataFrame 2:
#     key         Address Qualification
# 0  CS0     Maduravoyal         Btech
# 1  CS1      Nerkundram            BA
# 2  CS2       Koyambedu          Bcom
# 3  CS3      Anna Nagar           BBA
# 4  CS4  Thiruvanamalai           MSc
# 5  CS5     Thiruvallur           PhD
# 6  CS6      Kodaikanal           MCA
# 7  CS7            Ooty           MBA
# 8  CS8     Pondicherry           MSc

# Concatenated DataFrame with inner join:
#     key        Name  Age  key         Address Qualification
# 0  CS0     Sridhar   20  CS0     Maduravoyal         Btech
# 1  CS1     Yuvaraj   21  CS1      Nerkundram            BA
# 2  CS2     Bharath   22  CS2       Koyambedu          Bcom
# 3  CS3     Richard   23  CS3      Anna Nagar           BBA
# 4  CS4      Dinesh   24  CS4  Thiruvanamalai           MSc
# 5  CS5     Dhanush   25  CS5     Thiruvallur           PhD
# 6  CS6  Muthukumar   26  CS6      Kodaikanal           MCA
# 7  CS7     Thrisha   27  CS7            Ooty           MBA
# 8  CS8       Jesse   28  CS8     Pondicherry           MSc