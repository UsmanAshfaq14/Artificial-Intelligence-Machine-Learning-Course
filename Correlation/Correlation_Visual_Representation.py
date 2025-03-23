import pandas as pd
from sklearn.datasets import load_diabetes
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset with frame
df = load_diabetes(as_frame=True)
# convert into pandas dataframe
df = df.frame
# Print first 5 rows
#print(df.head())
df.head()

# Find the pearson correlations matrix
corr = df.corr(method = 'pearson')
corr
#print(corr)

# Plot the heatmap
plt.figure(figsize=(12,8), dpi =200)
sns.heatmap(corr,annot=True,fmt=".2f", linewidth=.5)
plt.show()
# Save the plot
#plt.savefig('heatmap.png')







