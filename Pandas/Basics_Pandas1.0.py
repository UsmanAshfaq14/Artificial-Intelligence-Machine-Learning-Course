# ============================================================
# Introduction to Pandas
# ============================================================

# Import the Pandas library (and NumPy for creating missing data examples)
import pandas as pd
import numpy as np

# ============================================================
# Hour 2: Series, DataFrame, and Data Input
# ============================================================

# 1a. Creating a Series:
# A Series is a one-dimensional labeled array.
data_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Pandas Series:")
print(data_series)

# 1b. Creating a DataFrame:
# A DataFrame is a two-dimensional, tabular data structure with labeled axes.
# Here we create a DataFrame from a dictionary.
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data_dict)
print("\nPandas DataFrame:")
print(df)

# 1c. Data Input Example:
# Typically, you might load data from a CSV file.
# For demonstration purposes, here's how you would read a CSV file:
# df = pd.read_csv('filename.csv')
# (Uncomment the above line when you have a CSV file to load.)

# ============================================================
# Hour 2 Continued: Selection and Indexing
# ============================================================

# a) Selecting Rows:
# Use .iloc[] to select rows by integer-location based indexing.
print("\nSelect the second row using iloc (index 1):")
print(df.iloc[1])  # Displays the second row

# b) Selecting Columns:
# Use bracket notation or dot notation to select a column.
print("\nSelect the 'Name' column:")
print(df['Name'])

# c) Conditional Selection:
# Select rows where 'Age' is greater than 30.
print("\nRows where Age > 30:")
print(df[df['Age'] > 30])

# d) Index Setting:
# Set a column as the index of the DataFrame.
df_indexed = df.set_index('Name')
print("\nDataFrame after setting 'Name' as the index:")
print(df_indexed)

# ============================================================
# Hour 3: Operations on DataFrames
# ============================================================

# a) Viewing Data:
# Use .head() to view the first few rows of the DataFrame.
print("\nFirst 2 rows of the DataFrame:")
print(df.head(2))

# b) Unique Values:
# Find unique values in the 'City' column.
print("\nUnique values in 'City':")
print(df['City'].unique())

# c) Value Counts:
# Count the frequency of each unique value in the 'City' column.
print("\nValue counts for 'City':")
print(df['City'].value_counts())

# d) Applying Custom Functions:
# For example, add 5 to each entry in the 'Age' column.
df['AgePlus5'] = df['Age'].apply(lambda x: x + 5)
print("\nDataFrame after applying a custom function (Age + 5):")
print(df)

# e) Obtaining Column and Index Names:
print("\nColumn names in the DataFrame:")
print(df.columns)
print("Index labels of the DataFrame:")
print(df.index)

# f) Sorting and Ordering:
# Sort the DataFrame by the 'Age' column in descending order.
df_sorted = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):")
print(df_sorted)

# g) Null Value Check:
# Check for missing values within the DataFrame.
print("\nChecking for null values in the DataFrame:")
print(df.isnull())

# h) Value Replacement:
# Replace a specific value in the DataFrame.
# For example, replace 'Chicago' with 'San Francisco' in the 'City' column.
df_replaced = df.replace({'City': {'Chicago': 'San Francisco'}})
print("\nDataFrame after replacing 'Chicago' with 'San Francisco':")
print(df_replaced)

# i) Dropping Rows and Columns:
# To drop a column, use the drop() method with the columns parameter.
df_dropped_column = df.drop(columns=['AgePlus5'])
print("\nDataFrame after dropping the 'AgePlus5' column:")
print(df_dropped_column)

# To drop a row, use the drop() method with the index parameter.
# Here, we drop the row with index 2 (i.e. the third row in the original DataFrame).
df_dropped_row = df.drop(index=2)
print("\nDataFrame after dropping the row with index 2:")
print(df_dropped_row)

# ============================================================
# Hour 4: Missing Data & Its Handling
# ============================================================

# Create a DataFrame with missing data (NaN values)
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [5, np.nan, np.nan, 8]
}
df_nan = pd.DataFrame(data_with_nan)
print("\nDataFrame with missing values:")
print(df_nan)

# a) Identifying Missing Data:
# Use isnull() to detect missing values and sum() to count them.
print("\nCount of missing values in each column:")
print(df_nan.isnull().sum())

# b) Handling Missing Data:
# Option 1: Drop rows with any missing values.
df_nan_drop = df_nan.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_nan_drop)

# Option 2: Fill missing values with a constant (e.g., 0).
df_nan_fill_zero = df_nan.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_nan_fill_zero)

# Option 3: Fill missing values using a strategy (e.g., column mean).
df_nan_fill_mean = df_nan.fillna(df_nan.mean())
print("\nDataFrame after filling missing values with column means:")
print(df_nan_fill_mean)
