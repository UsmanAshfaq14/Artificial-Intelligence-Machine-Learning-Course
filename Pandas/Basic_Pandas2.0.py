# ============================================================
# Import Libraries
# ============================================================

# Import Pandas for data manipulation and NumPy for generating sample data.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# NOTE: If you are using a Jupyter Notebook, you might want to uncomment the following line 
# to display plots inline:
# %matplotlib inline

# ============================================================
# Section 1: Merging, Joining, and Concatenation
# ============================================================

# Create two DataFrames with a common key ('ID').
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Score': [85, 90, 95, 80]
})

# ----- Merging (Joining on 'ID') -----
# Inner Join: Only common IDs in both DataFrames.
inner_join = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Join:\n", inner_join)

# Left Join: All IDs from df1, plus matching rows from df2.
left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:\n", left_join)

# Right Join: All IDs from df2, plus matching rows from df1.
right_join = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join:\n", right_join)

# Outer Join: All IDs from both DataFrames.
outer_join = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join:\n", outer_join)

# ----- Concatenation -----
# Concatenating DataFrames vertically (stacking rows).
concat_vertical = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nVertical Concatenation:\n", concat_vertical)

# Concatenating DataFrames horizontally (side-by-side).
concat_horizontal = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:\n", concat_horizontal)

# ============================================================
# Section 2: GroupBy
# ============================================================

# Create a sample DataFrame that includes a categorical variable.
df_sales = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'B', 'C', 'A', 'C'],
    'Sales': [100, 150, 200, 130, 120, 300, 250]
})

# Group the DataFrame by the 'Product' column and calculate the sum of 'Sales' for each group.
grouped_sales = df_sales.groupby('Product')['Sales'].sum()
print("\nTotal Sales by Product:\n", grouped_sales)

# ============================================================
# Section 3: Discretization and Binning
# ============================================================

# Create sample continuous data (e.g., ages or scores).
data_values = np.random.randint(0, 100, size=20)
print("\nContinuous Data:\n", data_values)

# Define bins. For example, dividing the data into three groups.
bins = [0, 33, 66, 100]
# Label each bin as "Low", "Medium", or "High".
labels = ['Low', 'Medium', 'High']
# Use pd.cut to assign each data point to a bin.
binned_data = pd.cut(data_values, bins=bins, labels=labels)
print("\nBinned Data (Discretization):\n", binned_data)

# ============================================================
# Section 4: Additional Operations on DataFrames
# ============================================================

# Example DataFrame for additional operations.
df_operations = pd.DataFrame({
    'A': np.random.randint(1, 50, 10),
    'B': np.random.randint(1, 50, 10),
    'C': np.random.randint(1, 50, 10)
})
print("\nOriginal DataFrame for Operations:\n", df_operations)

# ---- Sorting: Sort by column 'A'.
df_sorted = df_operations.sort_values(by='A')
print("\nDataFrame Sorted by Column 'A':\n", df_sorted)

# ---- Checking for Null Values: (None expected in this example).
print("\nChecking for Null Values:\n", df_operations.isnull())

# ---- Value Replacement: Replace all instances of a specific value.
# For demonstration, suppose we want to replace any occurrence of the value 25 with 100.
df_replaced = df_operations.replace(25, 100)
print("\nDataFrame after Value Replacement (25 -> 100):\n", df_replaced)

# ============================================================
# Section 5: Data Output/Saving
# ============================================================

# Save the sales DataFrame to a CSV file.
# This command writes the DataFrame to a file named 'sales_data.csv' in CSV format.
df_sales.to_csv('sales_data.csv', index=False)
print("\nData saved to 'sales_data.csv'.")

# ============================================================
# Section 6: Pandas for Plotting
# ============================================================
# Create a sample DataFrame for various plots.
df_plot = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
})

# ---- Line Plot:
df_plot.plot.line(title="Line Plot")
plt.show()  # Display the line plot

# ---- Bar Plot:
# For a categorical bar plot, create a small DataFrame.
df_bar = pd.DataFrame({
    'Category': ['X', 'Y', 'Z'],
    'Values': [10, 20, 15]
})
df_bar.plot.bar(x='Category', y='Values', title="Bar Plot")
plt.show()

# ---- Area Plot:
df_plot.plot.area(title="Area Plot")
plt.show()

# ---- Density Plot (Kernel Density Estimation):
df_plot.plot.kde(title="Density (KDE) Plot")
plt.show()

# ---- Histogram:
df_plot.plot.hist(title="Histogram", bins=5)
plt.show()

# ---- Scatter Plot:
# Scatter plot requires two numeric columns to compare.
df_plot.plot.scatter(x='A', y='B', title="Scatter Plot")
plt.show()

# ---- Horizontal Bar Plot:
df_bar.plot.barh(x='Category', y='Values', title="Horizontal Bar Plot")
plt.show()

# ---- Box Plot:
df_plot.plot.box(title="Box Plot")
plt.show()

# ---- Hexbin Plot:
# Hexbin plot is good for visualizing the density of points.
df_plot.plot.hexbin(x='A', y='B', gridsize=10, title="Hexbin Plot")
plt.show()

# ---- KDE Plot:
# The KDE plot is similar to the density plot shown earlier.
df_plot.plot.kde(title="KDE Plot")
plt.show()

# ---- Pie Plot:
# For a pie chart, we use data that represents parts of a whole.
df_bar.set_index('Category')['Values'].plot.pie(title="Pie Chart", autopct='%1.1f%%')
plt.show()
