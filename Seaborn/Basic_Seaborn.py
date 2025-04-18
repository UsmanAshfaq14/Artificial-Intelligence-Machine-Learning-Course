# ================================================================
# Introduction to Seaborn: Distribution, Categorical, and Matrix Plots
# ================================================================

# Import necessary libraries: Seaborn for plotting, Matplotlib to display the plots,
# NumPy for generating sample data, and Pandas for accessing built-in datasets.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set a visual theme for better aesthetics.
sns.set_theme(style="whitegrid")


# ================================================================
# Hour 2: Distribution Plots
# ================================================================

# Generate random data from a normal distribution.
data = np.random.randn(1000)

# 1. Distribution Plot using histplot (instead of the deprecated distplot).
# We also enable kernel density estimation (kde) to show the estimated density.
plt.figure(figsize=(8, 6))
sns.histplot(data, bins=30, kde=True, stat="density")  # 'stat="density"' scales y-axis to density.
plt.title("Distribution Plot (histplot) of Random Data")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

# 2. Joint Plot:
# Create two related datasets to show the relationship between them.
x = np.random.randn(1000)
y = x * 0.5 + np.random.randn(1000) * 0.5
# 'jointplot' creates a scatter plot with marginal distributions.
sns.jointplot(x=x, y=y, kind="scatter", height=8)
plt.suptitle("Joint Plot: Scatter with Marginal Distributions", y=1.02)
plt.show()

# 3. Pair Plot:
# Load the Iris dataset (a built-in dataset in Seaborn).
iris = sns.load_dataset("iris")
# 'pairplot' creates a matrix of scatter plots and histograms for each pair of variables.
sns.pairplot(iris, hue="species")
plt.suptitle("Pair Plot of the Iris Dataset", y=1.02)
plt.show()

# 4. Rug Plot:
# Rug Plot adds small tick marks for each observation along the x-axis.
plt.figure(figsize=(8, 6))
sns.rugplot(data)
plt.title("Rug Plot of Random Data")
plt.xlabel("Value")
plt.show()

# 5. KDE Plot:
# Updated to use 'fill=True' instead of the deprecated 'shade=True'.
plt.figure(figsize=(8, 6))
sns.kdeplot(data, fill=True)
plt.title("KDE Plot of Random Data")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()


# ================================================================
# Hour 3: Categorical Data Plots
# ================================================================

# Load the "tips" dataset, which includes both numerical and categorical variables.
tips = sns.load_dataset("tips")

# 1. Catplot (formerly factorplot):
# Create a swarm plot for categorical data. The hue parameter separates data by smoker status.
g = sns.catplot(x="day", y="total_bill", hue="smoker", data=tips, kind="swarm", height=6)
g.fig.suptitle("Catplot (Swarm) of Total Bill by Day, Separated by Smoker Status", y=0.95)
plt.show()

# 2. Box Plot:
plt.figure(figsize=(8, 6))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 3. Violin Plot:
plt.figure(figsize=(8, 6))
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 4. Strip Plot:
plt.figure(figsize=(8, 6))
# 'jitter=True' adds a small random noise to prevent overplotting.
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
plt.title("Strip Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 5. Swarm Plot:
plt.figure(figsize=(8, 6))
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.title("Swarm Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 6. Bar Plot:
# Bar plot showing average total bill per day.
plt.figure(figsize=(8, 6))
sns.barplot(x="day", y="total_bill", data=tips, estimator=np.mean)
plt.title("Bar Plot: Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()

# 7. Count Plot:
# Count plot showing the number of observations per day.
plt.figure(figsize=(8, 6))
sns.countplot(x="day", data=tips)
plt.title("Count Plot: Number of Orders by Day")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()


# ================================================================
# Hour 4: Matrix Plots (Heatmap)
# ================================================================

# Creating a correlation matrix:
# The "tips" dataset contains non-numeric columns (e.g., 'smoker', 'day', etc.), which
# can cause conversion errors. We select only the numeric columns.
numeric_tips = tips.select_dtypes(include=[np.number])
corr_matrix = numeric_tips.corr()

plt.figure(figsize=(8, 6))
# 'heatmap' displays the correlation matrix with annotations.
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap of Correlation Matrix (Tips Dataset - Numeric Columns Only)")
plt.show()
