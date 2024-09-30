import pandas as pd

# Define a dictionary containing employee data
data = {
    'Name': ['Raj', 'Raju', 'Raja', 'Rajan'],
    'Age': [27, 24, 22, 23],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Define the address list
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Add the Address column to the DataFrame
df['Address'] = address

# Drop the Qualification column
df.drop(['Qualification'], axis=1, inplace=True)

# Print descriptive statistics of the DataFrame
print(df.describe())

# Print the last 2 rows of the DataFrame
print(df.tail(2))


# OUTPUT
#              Age
# count   4.000000
# mean   24.000000
# std     2.160247
# min    22.000000
# 25%    22.750000
# 50%    23.500000
# 75%    24.750000
# max    27.000000
#     Name  Age  Address
# 2   Raja   22  Chennai
# 3  Rajan   23    Patna