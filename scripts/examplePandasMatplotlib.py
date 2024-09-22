import pandas as pd
import matplotlib.pyplot as plt

# 1. Loading Data
# df = pd.read_csv('stem_students.csv')

# Sample data (use this if you don't have a CSV file yet)
data = {
    'student_id': range(1, 11),
    'gender': ['Female', 'Male', 'Female', 'Non-binary', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'ethnicity': ['White', 'Black', 'Hispanic', 'Asian', 'White', 'Black', 'Asian', 'White', 'Hispanic', 'White'],
    'major': ['Computer Science', 'Biology', 'Physics', 'Mathematics', 'Chemistry', 'Computer Science', 'Physics', 'Mathematics', 'Biology', 'Chemistry'],
    'gpa': [3.8, 3.6, 3.9, 4.0, 3.7, 3.5, 3.8, 3.9, 3.6, 4.0],
    'year': [2, 3, 4, 1, 2, 3, 4, 2, 1, 3],
    'first_gen': [True, False, True, False, True, True, False, False, True, False]
}
df = pd.DataFrame(data)

# 2. Basic Data Exploration
print("First few rows of the dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# 3. Data Cleaning
# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicates (if any)
df.drop_duplicates(inplace=True)

# 4. Filtering Data
# Get all Computer Science students
cs_students = df[df['major'] == 'Computer Science']
print("\nComputer Science students:")
print(cs_students)

# Get all female students
female_students = df[df['gender'] == 'Female']
print("\nFemale students:")
print(female_students)

# 5. Grouping and Aggregation
# Average GPA by major
avg_gpa_by_major = df.groupby('major')['gpa'].mean().sort_values(descending=True)
print("\nAverage GPA by major:")
print(avg_gpa_by_major)

# Count of students by ethnicity
ethnicity_counts = df['ethnicity'].value_counts()
print("\nCount of students by ethnicity:")
print(ethnicity_counts)

# 6. Calculation and Adding New Columns
# Calculate the percentage of first-generation students
first_gen_percentage = (df['first_gen'].sum() / len(df)) * 100
print(f"\nPercentage of first-generation students: {first_gen_percentage:.2f}%")

# Add a new column for GPA category
df['gpa_category'] = pd.cut(df['gpa'], bins=[0, 2.0, 3.0, 3.5, 4.0], labels=['Poor', 'Average', 'Good', 'Excellent'])
print("\nDataset with GPA category:")
print(df)

# 7. Basic Data Visualization with Matplotlib
plt.figure(figsize=(10, 6))
df['major'].value_counts().plot(kind='bar')
plt.title('Distribution of Majors')
plt.xlabel('Major')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Saving processed data
# df.to_csv('processed_stem_students.csv', index=False)
# Uncomment the line above if you want to save the processed data to a new CSV file