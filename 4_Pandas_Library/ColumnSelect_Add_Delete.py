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

# Select two columns
print(df[['Name', 'Address']])



# OUTPUT
#     Name    Address
# 0    Raj      Delhi
# 1   Raju  Bangalore
# 2   Raja    Chennai
# 3  Rajan      Patna