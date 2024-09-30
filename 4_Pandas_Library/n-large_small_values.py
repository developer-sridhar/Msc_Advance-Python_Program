import pandas as pd

# Create a DataFrame with the specified data
df = pd.DataFrame(
    [[10, 20, 30, 40],
     [7, 14, 21, 28],
     [55, 15, 8, 12],
     [15, 14, 1, 8],
     [7, 1, 1, 8],
     [95, 4, 9, 2]],
    columns=['apple', 'orange', 'banana', 'pear'],
    index=['basket1', 'basket2', 'basket3', 'basket4', 'basket5', 'basket6']
)

# Print the DataFrame
print("\n-------- DataFrame -----------\n")
print(df)

# Get the n smallest values for 'apple'
print("\n-------- nsmallest ----------\n")
print(df.nsmallest(2, 'apple'))

# Get the n largest values for 'apple'
print("\n-------- nlargest ----------\n")
print(df.nlargest(2, 'apple'))


#OUTPUT
# -------- DataFrame -----------

#          apple  orange  banana  pear
# basket1     10      20      30    40
# basket2      7      14      21    28
# basket3     55      15       8    12
# basket4     15      14       1     8
# basket5      7       1       1     8
# basket6     95       4       9     2

# -------- nsmallest ----------

#          apple  orange  banana  pear
# basket2      7      14      21    28
# basket5      7       1       1     8

# -------- nlargest ----------

#          apple  orange  banana  pear
# basket6     95       4       9     2
# basket3     55      15       8    12