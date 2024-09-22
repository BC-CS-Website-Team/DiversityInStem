import pandas as pd
import os

# Define input and output file paths
input_file = '../data/raw/EnrollmentByRaceAndEthnicity.csv'
output_file = '../data/processed/CleanedEnrollmentData2022.csv'


# Read the CSV file
df = pd.read_csv(input_file)

# Print column names for debugging
print("Columns in the CSV file:", df.columns.tolist())

# Filter for specific columns
# Note: We're using the actual column names from your CSV file
columns_to_keep = ['IPEDS_Race', 'Year', 'Enrollment', 'University', 'share']
df_filtered = df[columns_to_keep]

# Filter for the year 2022
df_filtered = df_filtered[df_filtered['Year'] == 2022]

# Filter for specific university values
universities_to_keep = ['Baccalaureate Colleges', 'Berea College']
df_filtered = df_filtered[df_filtered['University'].isin(universities_to_keep)]

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the processed data to the output file
df_filtered.to_csv(output_file, index=False)

print(f"Processed data has been saved to {output_file}")
