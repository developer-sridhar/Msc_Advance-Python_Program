import pandas as pd

# Use forward slashes in the file path
df = pd.read_csv("C:/Users/Alam-Alfan/OneDrive/Desktop/MSc Python/Python_Syllabus/4_Pandas_Library/nba.csv")

# First grouping based on "Team"
gkk = df.groupby(['Team', 'Position'])

# Print the first value in each group
print(gkk.first())

#OUTPUT
#                                              Name  ...      Salary
# Team              Position                          ...
# Atlanta Hawks     C                     AJ Horford  ...  12000000.0
#                   PF                Kris Humphries  ...   1000000.0
#                   PG               Dennis Schroder  ...   1763400.0
#                   SF                 Kent Bazemore  ...   2000000.0
#                   SG               Tim Hardaway Jr  ...   1304520.0
# Boston Celtics    C                   Kelly Olynyk  ...   2165160.0
#                   PF                 Jones Jerebko  ...   5000000.0
#                   PG                 Avery Bradley  ...   7730337.0
#                   SF                   Jae Crowder  ...   6796117.0
#                   SG                  John Holland  ...   1148640.0
# Brooklyn Nets     C                    Brook Lopez  ...  19689000.0
#                   PF              Chris McCullough  ...   1140240.0
#                   PG                   Jarret Jack  ...   6300000.0
#                   SG              Bojan Bogdanovic  ...   3425510.0
# Charlotte Hornets C                   AJ Jefferson  ...  13500000.0
#                   PF             Taylor Hansbrough  ...    947276.0
#                   PG               Jorge Gutierrez  ...    189455.0
#                   SF        Michael Kidd-Gilchrist  ...   6331404.0

# [18 rows x 7 columns]