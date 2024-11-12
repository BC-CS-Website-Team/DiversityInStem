import pandas as pd

# Sample DataFrame
data = 'Fall2023GeographicalReportBereaCollege.xlsx'
df = pd.read_excel(data)

# Count unique values in 'column_name'
unique_count = df['Country'].unique()
print(unique_count)

# Count the number of occurrences of each unique value in 'column_name'
value_counts = df['Country'].value_counts()
print(value_counts)