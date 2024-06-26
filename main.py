import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
df = pd.read_csv('C:\\Users\\kaurm\\Documents\\Jas2\\Financial Database\\financial_well_being_2017.csv.csv')

# Display the first few rows of the dataframe
print(df.head())

# Perform basic cleaning (if needed)
# Example: Handle missing values
df = df.dropna()

# Example: Calculate a new column, if applicable
# For example, we can create a 'savings' column if we have 'income' and 'expenses' columns
# df['savings'] = df['income'] - df['expenses']

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_financial_well_being_2017.csv', index=False)

# Create visualizations

# Example Visualization 1: Histogram of Financial Well-Being Scores
plt.figure(figsize=(10, 6))
sns.histplot(df['FWBscore'], kde=True)
plt.title('Distribution of Financial Well-Being Scores')
plt.xlabel('Financial Well-Being Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('financial_well_being_distribution.png')

# Example Visualization 2: Bar Plot of Financial Well-Being by Age Group
# Assuming we have an 'agecat' column for age categories
plt.figure(figsize=(10, 6))
sns.barplot(x='agecat', y='FWBscore', data=df, estimator=sum)
plt.title('Financial Well-Being by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Financial Well-Being Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('financial_well_being_by_age_group.png')

print("Data cleaning, transformation, and visualizations complete.")
