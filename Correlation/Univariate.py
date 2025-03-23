import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [14, 18, 15, 16, 22, 19, 24, 20]

# Central Tendency and Variability
mean = np.mean(data)
median = np.median(data)
mode = pd.Series(data).mode()[0]
std_dev = np.std(data, ddof=1)

# Visualization
plt.hist(data, bins=5, color='skyblue', alpha=0.7)
plt.title('Univariate Analysis')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

print(f"Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {std_dev}")