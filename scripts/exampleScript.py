import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the style for our plots
plt.style.use('ggplot')
sns.set_palette('deep')

# Data Collection
# For this demo, we're creating sample data. In a real scenario, you'd load your data from a file.
print("--- Data Collection ---")
data = {
    'student_id': range(1, 101),
    'gender': np.random.choice(['Male', 'Female', 'Non-binary'], 100),
    'ethnicity': np.random.choice(['White', 'Black', 'Hispanic', 'Asian', 'Other'], 100),
    'major': np.random.choice(['Computer Science', 'Biology', 'Chemistry', 'Physics', 'Mathematics'], 100),
    'gpa': np.random.uniform(2.0, 4.0, 100),
    'year': np.random.choice([1, 2, 3, 4], 100),
    'first_gen': np.random.choice([True, False], 100)
}

# Create a DataFrame from our data
df = pd.DataFrame(data)

# Display the first few rows of our data
print("First few rows of our data:")
print(df.head())

# Data Cleaning
print("\n--- Data Cleaning ---")

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# If there were missing values, we might handle them here (e.g., by filling or dropping)

# Remove any duplicate rows
df.drop_duplicates(inplace=True)
print("\nShape after removing duplicates:", df.shape)

# Ensure 'year' is treated as a category and 'gpa' is rounded to 2 decimal places
df['year'] = df['year'].astype('category')
df['gpa'] = df['gpa'].round(2)

print("\nUpdated Data Types:")
print(df.dtypes)

# Data Exploration
print("\n--- Data Exploration ---")

# Display summary statistics for our numerical data
print("\nSummary Statistics for GPA:")
print(df['gpa'].describe())

# Display counts for our categorical data
print("\nMajor Distribution:")
print(df['major'].value_counts())

print("\nGender Distribution:")
print(df['gender'].value_counts())

# Data Visualization
print("\n--- Data Visualization ---")

# Create a bar plot showing the distribution of majors
plt.figure(figsize=(10, 6))
sns.countplot(x='major', data=df)
plt.title('Distribution of Majors')
plt.xlabel('Major')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()

# Create a box plot showing GPA distribution by gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='gender', y='gpa', data=df)
plt.title('GPA Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('GPA')
plt.tight_layout()
plt.show()

# Create a scatter plot of GPA vs Year, colored by first-generation status
plt.figure(figsize=(10, 6))
sns.scatterplot(x='year', y='gpa', hue='first_gen', data=df)
plt.title('GPA vs Year, colored by First Generation Status')
plt.xlabel('Year')
plt.ylabel('GPA')
plt.tight_layout()
plt.show()

# Basic Analysis
print("\n--- Basic Analysis ---")

# Calculate average GPA by major
avg_gpa_by_major = df.groupby('major')['gpa'].mean().sort_values(ascending=False)
print("\nAverage GPA by Major:")
print(avg_gpa_by_major)

# Calculate the percentage of first-generation students by major
first_gen_pct_by_major = df.groupby('major')['first_gen'].mean() * 100
print("\nPercentage of First-Generation Students by Major:")
print(first_gen_pct_by_major)

print("\nThis script demonstrates basic data cleaning, exploration, visualization, and analysis techniques.")
print("You can adapt this to your actual data and specific research questions.")