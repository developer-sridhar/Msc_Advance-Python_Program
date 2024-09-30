import pandas as pd

# Create a dictionary with straight quotes and correct syntax
data = {
    'key': ['cs0', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6', 'cs7', 'cs8'],
    'Name': ['Sridhar', 'Yuvaraj', 'Bharath', 'Richard', 'Dinesh', 'Dhanush', 'Muthukumar','Thrisha','Jesse'],
    'Age': [20, 20, 20, 20, 20, 20, 20, 20, 20],
    'Sex': ['Male', 'Male','Male','Male','Male','Male','Male','Female','Female',],
    'Qualification': ['Msc','Msc','Msc','Msc','Msc','Msc','Msc','Msc','Msc']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)


#OUTPUT
#    key        Name  Age     Sex Qualification
# 0  cs0     Sridhar   20    Male           Msc
# 1  cs1     Yuvaraj   20    Male           Msc
# 2  cs2     Bharath   20    Male           Msc
# 3  cs3     Richard   20    Male           Msc
# 4  cs4      Dinesh   20    Male           Msc
# 5  cs5     Dhanush   20    Male           Msc
# 6  cs6  Muthukumar   20    Male           Msc
# 7  cs7     Thrisha   20  Female           Msc
# 8  cs8       Jesse   20  Female           Msc