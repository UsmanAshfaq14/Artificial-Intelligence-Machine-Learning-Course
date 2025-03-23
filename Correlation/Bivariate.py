from scipy.stats import pearsonr
import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y = [12, 25, 35, 40, 60]

# Pearson Correlation
correlation, _ = pearsonr(x, y)
print(f"Pearson Correlation: {correlation}")

# Scatterplot
plt.scatter(x, y, color='purple')
plt.title('Bivariate Analysis')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()