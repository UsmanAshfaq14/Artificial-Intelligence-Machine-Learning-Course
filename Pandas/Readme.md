# Introduction to Pandas

Pandas is an open-source Python library that provides high-performance, easy-to-use data structures and data analysis tools. It is built on top of NumPy and is essential for data manipulation and analysis, offering powerful and flexible data handling capabilities through its two main data structures: Series and DataFrame.

In this lecture, we explored several key aspects of Pandas:
- Creating and manipulating **Series** and **DataFrames**
- Data input from various sources (like CSV files)
- **Selection** and **Indexing** of data (rows, columns, conditional selection, and index setting)
- Common **DataFrame operations** (viewing data, unique counts, applying functions, sorting, etc.)
- Techniques for identifying and handling **Missing Data**

This document can be used both as a teaching tool during lectures and as a study reference for students.

---

## Table of Contents

1. [Overview of Pandas](#overview-of-pandas)
2. [Data Structures in Pandas](#data-structures-in-pandas)
   - [Series](#series)
   - [DataFrame](#dataframe)
   - [Data Input](#data-input)
3. [Selection and Indexing](#selection-and-indexing)
   - [Row and Column Selection](#row-and-column-selection)
   - [Conditional Selection](#conditional-selection)
   - [Index Setting](#index-setting)
4. [DataFrame Operations](#dataframe-operations)
   - [Viewing Data: `head()`](#viewing-data-head)
   - [Unique Values and Value Counts](#unique-values-and-value-counts)
   - [Applying Custom Functions](#applying-custom-functions)
   - [Retrieving Metadata: Column and Index Names](#retrieving-metadata)
   - [Sorting and Ordering](#sorting-and-ordering)
   - [Null Value Check and Value Replacement](#null-value-check-and-value-replacement)
   - [Dropping Rows and Columns](#dropping-rows-and-columns)
5. [Handling Missing Data](#handling-missing-data)
6. [Usage and Installation](#usage-and-installation)
7. [Conclusion](#conclusion)
8. [References](#references)

---

## Overview of Pandas

Pandas is a cornerstone for data analysis in Python. It simplifies data manipulation tasks through:
- **High-level data structures:** Such as Series (1D) and DataFrame (2D).
- **Integrated I/O support:** Easily read and write data from files like CSV, Excel, and SQL databases.
- **Data alignment and integrated handling of missing data:** Ensuring robust data analysis even when data is incomplete.
- **Time Series functionality:** Facilitating financial and temporal data analysis.

**Why Pandas?**
- **Efficiency:** Fast operations on large datasets.
- **Flexibility:** Allows easy reshaping, merging, and aggregation of data.
- **Integration:** Works seamlessly with other Python libraries (NumPy, Matplotlib, Seaborn).

---

## Data Structures in Pandas

### Series

A **Series** is a one-dimensional labeled array that can hold various data types (integers, strings, floats, etc.). It is similar to a column in a spreadsheet or a database.

**Key Features:**
- Each element has an associated label (index).
- Useful for time series data or any one-dimensional labeled data.

**Example:**
```python
import pandas as pd

# Creating a Series from a list with custom index labels.
data_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(data_series)
```

### DataFrame

A **DataFrame** is a two-dimensional tabular data structure with labeled axes (rows and columns). It is similar to a spreadsheet, SQL table, or R data frame.

**Key Features:**
- Columns can be of different data types.
- Supports both row and column indexing.
- Facilitates data cleaning, merging, reshaping, and aggregation.

**Example:**
```python
# Creating a DataFrame from a dictionary.
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data_dict)
print(df)
```

### Data Input

Pandas makes it simple to import data from various file formats such as CSV, Excel, and JSON.

**Example:**
```python
# Reading data from a CSV file (uncomment when a file is available).
# df = pd.read_csv('filename.csv')
```

---

## Selection and Indexing

Pandas provides versatile methods for data selection and indexing, essential for data exploration and manipulation.

### Row and Column Selection

- **Row Selection:** Use `.iloc[]` for integer-location-based indexing.
- **Column Selection:** Access columns using bracket notation or dot notation.

**Example:**
```python
# Selecting the second row using iloc.
print(df.iloc[1])

# Selecting the 'Name' column.
print(df['Name'])
```

### Conditional Selection

Filter the DataFrame based on a condition. For example, select rows where the age is greater than 30.

**Example:**
```python
print(df[df['Age'] > 30])
```

### Index Setting

Change the DataFrame's default index by setting a column as the index. This helps when a specific column (like an identifier) provides a meaningful label for rows.

**Example:**
```python
df_indexed = df.set_index('Name')
print(df_indexed)
```

---

## DataFrame Operations

Pandas comes with a rich set of methods to perform a variety of operations on DataFrames.

### Viewing Data: `head()`

View the first few rows of the DataFrame to get an overview of the data.

**Example:**
```python
print(df.head(2))
```

### Unique Values and Value Counts

Determine the distinct values in a column and count their frequency.

**Example:**
```python
print(df['City'].unique())
print(df['City'].value_counts())
```

### Applying Custom Functions

Apply custom functions to DataFrame columns with `apply()`. This is useful for data transformation and feature engineering.

**Example:**
```python
df['AgePlus5'] = df['Age'].apply(lambda x: x + 5)
print(df)
```

### Retrieving Metadata

Get metadata such as column names and index labels.

**Example:**
```python
print("Columns:", df.columns)
print("Index:", df.index)
```

### Sorting and Ordering

Sort the DataFrame by a given column using `sort_values()`.

**Example:**
```python
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)
```

### Null Value Check and Value Replacement

Check for missing values using `isnull()` and replace specific values with `replace()`.

**Example:**
```python
print(df.isnull())
df_replaced = df.replace({'City': {'Chicago': 'San Francisco'}})
print(df_replaced)
```

### Dropping Rows and Columns

Remove unwanted rows or columns using the `drop()` method.

**Example:**
```python
df_dropped_column = df.drop(columns=['AgePlus5'])
print(df_dropped_column)
df_dropped_row = df.drop(index=2)
print(df_dropped_row)
```

---

## Handling Missing Data

Missing data is a common issue in real-world datasets. Pandas provides several strategies to address missing data:

### Identifying Missing Data

Use `isnull()` to detect missing values and `sum()` to count them by column.

**Example:**
```python
print(df.isnull().sum())
```

### Dropping Missing Data

Remove rows or columns with missing values using `dropna()`.

**Example:**
```python
df_clean = df.dropna()
print(df_clean)
```

### Filling Missing Data

Replace missing values with a specified constant or a computed statistic (e.g., mean) using `fillna()`.

**Example:**
```python
df_filled = df.fillna(0)
print(df_filled)
```

---

## Usage and Installation

**Installation:**
To use Pandas, install it via pip:
```bash
pip install pandas
```

**Running the Examples:**
- Save the provided code snippets in a Python script or Jupyter Notebook.
- Execute the script with `python script_name.py`, or run the cells in a Notebook sequentially.

**Use Cases:**
- **Data Cleaning:** Remove or impute missing values and outliers.
- **Data Transformation:** Reshape data for analysis, merge multiple datasets, and perform aggregation.
- **Exploratory Data Analysis (EDA):** Gain initial insights into dataset characteristics using summary statistics and visualizations.

---

## Conclusion

This lecture on Pandas covered the essentials for managing and analyzing data:
- **Data Structures:** Series and DataFrames allow robust handling of 1D and 2D data.
- **Selection/Indexing:** Flexible methods for filtering and accessing data.
- **DataFrame Operations:** A wide array of functions for viewing, sorting, summarizing, and modifying data.
- **Missing Data Handling:** Strategies to identify, remove, or fill missing values, ensuring data integrity for further analysis.

Mastering these concepts provides a strong foundation for advanced data analysis and machine learning tasks.

---

## References

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python Data Science Handbook by Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Data Wrangling with Pandas Cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---