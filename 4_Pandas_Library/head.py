import pandas as pd

# Define a dictionary containing employee data
data = {
    'Name': ['Raj', 'Raju', 'Raja', 'Rajan'],
    'Age': [27, 24, 22, 32],
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

# Display the first 2 rows of the DataFrame
print(df.head(2))

# OUTPUT
#    Name  Age    Address
# 0   Raj   27      Delhi
# 1  Raju   24  Bangalore