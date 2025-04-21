# ============================================
# Exploratory Data Analysis with Pandas and Seaborn
# Python-Only Classroom Assignment Solution
# ============================================

# Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set plot style for better aesthetics
sns.set(style="whitegrid")

# -----------------------------
# Task 1: Data Loading and Inspection
# -----------------------------

# Load the built-in "tips" dataset from Seaborn
df = sns.load_dataset("tips")

# Display the first few rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

# Print the shape of the DataFrame (number of rows and columns)
print("\nDataset Shape:", df.shape)

# Display column names and their data types
print("\nData Types:")
print(df.dtypes)

# Check for missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Task 2: Data Manipulation and Analysis
# -----------------------------

# Descriptive Statistics for Numerical Columns
print("\nDescriptive Statistics for Numerical Columns:")
print(df.describe())

# Calculate specific statistics for 'total_bill' and 'tip'
total_bill_stats = df['total_bill'].agg(['mean', 'median', 'std'])
tip_stats = df['tip'].agg(['mean', 'median', 'std'])
print("\nTotal Bill Statistics (Mean, Median, Std):")
print(total_bill_stats)
print("\nTip Statistics (Mean, Median, Std):")
print(tip_stats)

# Frequency counts for categorical columns 'day' and 'smoker'
print("\nFrequency Counts for 'day':")
print(df['day'].value_counts())
print("\nFrequency Counts for 'smoker':")
print(df['smoker'].value_counts())

# Group by 'day' and calculate average 'total_bill' and 'tip'
group_by_day = df.groupby('day')[['total_bill', 'tip']].mean()
print("\nAverage Total Bill and Tip per Day:")
print(group_by_day)

# Group by 'smoker' status and calculate total and average 'total_bill'
group_by_smoker = df.groupby('smoker')['total_bill'].agg(['sum', 'mean'])
print("\nTotal and Mean Total Bill by Smoker Status:")
print(group_by_smoker)

# Sort the DataFrame by 'total_bill' in descending order and display the top rows
sorted_df = df.sort_values(by='total_bill', ascending=False)
print("\nDataFrame Sorted by Total Bill (Descending):")
print(sorted_df.head())

# Filter rows where the tip is above 8
high_tip_df = df[df['tip'] > 8]
print("\nRows with Tip Greater than 8:")
print(high_tip_df)

# -----------------------------
# Task 3: Data Visualization with Seaborn
# -----------------------------

# 1. Histogram with KDE for 'total_bill'
plt.figure(figsize=(8, 6))
sns.histplot(df['total_bill'], kde=True)
plt.title("Histogram and KDE of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# 2. Box Plot for 'total_bill' by Day
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Box Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.show()

# 3. Violin Plot for 'tip' by Smoker Status
plt.figure(figsize=(8, 6))
sns.violinplot(x='smoker', y='tip', data=df)
plt.title("Violin Plot of Tip by Smoker Status")
plt.xlabel("Smoker")
plt.ylabel("Tip")
plt.show()

# 4. Swarm Plot for 'total_bill' by Day
plt.figure(figsize=(8, 6))
sns.swarmplot(x='day', y='total_bill', data=df)
plt.title("Swarm Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 5. Heatmap of Correlation Matrix for numerical variables
corr_matrix = df[['total_bill', 'tip', 'size']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()

# 6. Optional: Pair Plot for numerical columns colored by 'day'
sns.pairplot(df, hue="day")
plt.suptitle("Pair Plot of Tips Dataset (Colored by Day)", y=1.02)
plt.show()

# -----------------------------
# Task 4: Reporting and Interpretation (Printed Report)
# -----------------------------
report = """
Summary Report:
----------------
1. Descriptive Statistics:
   - The numerical columns ('total_bill', 'tip', 'size') exhibit similar mean and median values,
     indicating fairly symmetric distributions with moderate variability.
   - Frequency counts of 'day' and 'smoker' help understand the overall composition of the dataset.

2. GroupBy Analysis:
   - Grouping by 'day' reveals that average total bills and tips vary across weekdays.
   - Grouping by 'smoker' status shows differences in total and average billing amounts,
     suggesting that customer behavior may differ based on smoking habits.

3. Visualizations:
   - The histogram with KDE shows that most total bills lie in the moderate range, with a slight right skew due to a few high-value bills.
   - The box plot across days highlights variability and outliers in bill amounts.
   - The violin plot demonstrates that tip distributions are fairly similar between smokers and non-smokers.
   - The swarm plot illustrates individual data points, revealing overlapping distributions with some high outliers.
   - The heatmap indicates a strong positive correlation (approximately 0.67) between 'total_bill' and 'tip',
     confirming that higher bills typically correspond with higher tips.

Real-World Relevance:
----------------------
Managers can use these insights to:
   - Adjust staffing levels on days with higher average bills.
   - Design promotions targeting groups with higher spending.
   - Monitor and investigate outlier transactions for potential operational issues.

In conclusion, the analysis provides a clear view of customer spending and tipping behavior, delivering actionable insights for improving restaurant operations.
"""

print(report)
