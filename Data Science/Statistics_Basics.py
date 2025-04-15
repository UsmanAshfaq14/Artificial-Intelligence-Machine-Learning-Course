import statistics
from scipy.stats import skew, kurtosis
import numpy as np

# Sample data
data = [4, 10, 29, 33, 42, 67]

# The mean, or average, is calculated by summing all the values in a dataset and dividing by the number of values. It's sensitive to outliers, which can skew the mean significantly.
# Formula: mean = sum(data) / len(data)
mean_manual = sum(data) / len(data)
mean_builtin = statistics.mean(data)
print(f"Mean (Manual): {mean_manual}")
print(f"Mean (Built-in): {mean_builtin}")

# The median is the middle value in a dataset when it's ordered from smallest to largest. It's less sensitive to outliers than the mean.
# For odd number of observations: median = middle value
# For even number of observations: median = (middle1 + middle2) / 2
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median_manual = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median_manual = sorted_data[n//2]
median_builtin = statistics.median(data)
print(f"Median (Manual): {median_manual}")
print(f"Median (Built-in): {median_builtin}")

# The mode is the value that appears most frequently in a dataset. It's useful for identifying the most common value.
# Note: A dataset may have one mode, more than one mode, or no mode at all.
try:
    mode_builtin = statistics.mode(data)
    print(f"Mode (Built-in): {mode_builtin}")
except statistics.StatisticsError:
    print("Mode (Built-in): No unique mode found.")

# The range is the difference between the largest and smallest values in a dataset. It provides an idea of the spread of the data.
# Formula: range = max(data) - min(data)
range_value = max(data) - min(data)
print(f"Range: {range_value}")

# The variance measures how far each number in the dataset is from the mean. It's a measure of dispersion.
# Formula (Sample Variance): variance = sum((x - mean)^2) / (n - 1)
variance_manual = sum((x - mean_manual) ** 2 for x in data) / (len(data) - 1)
variance_builtin = statistics.variance(data)
print(f"Variance (Manual): {variance_manual}")
print(f"Variance (Built-in): {variance_builtin}")

# The standard deviation is the square root of the variance. It provides a measure of the average distance of data points from the mean.
# Formula: standard deviation = sqrt(variance)
std_dev_manual = variance_manual ** 0.5
std_dev_builtin = statistics.stdev(data)
print(f"Standard Deviation (Manual): {std_dev_manual}")
print(f"Standard Deviation (Built-in): {std_dev_builtin}")

# The coefficient of variation (CV) is a relative measure of dispersion. It's calculated as the ratio of the standard deviation to the mean.
# Formula: CV = (standard deviation / mean) * 100
cv_manual = (std_dev_manual / mean_manual) * 100
print(f"Coefficient of Variation: {cv_manual}%")

# Skewness measures the asymmetry of the data distribution. It indicates whether the data is skewed to the left or right.
# Positive skewness indicates a distribution with a tail on the right side; negative skewness indicates a tail on the left side.
skewness_value = skew(data)
print(f"Skewness: {skewness_value}")

# Kurtosis measures the "tailedness" of the data distribution. It indicates whether the data has heavier or lighter tails than a normal distribution.
# Positive kurtosis indicates heavier tails; negative kurtosis indicates lighter tails.
kurtosis_value = kurtosis(data)
print(f"Kurtosis: {kurtosis_value}")

# --------- MEASURES OF POSITION ---------

# Z-Score (Standard Score)
# Z-score measures how many standard deviations a data point is from the mean.
# Formula: z = (x - mean) / standard_deviation
print("\n----- Measures of Position -----")
print("\nZ-Scores:")
z_scores_manual = [(x - mean_manual) / std_dev_manual for x in data]
for i, z in enumerate(z_scores_manual):
    print(f"Data point {data[i]}: Z-score = {z:.3f}")

# Using scipy for built-in z-score calculation
z_scores_scipy = [(x - mean_builtin) / std_dev_builtin for x in data]
print("\nZ-scores represent the number of standard deviations a value is from the mean.")
print("Positive z-score: above the mean | Negative z-score: below the mean")

# Percentiles
# Percentiles divide the dataset into 100 equal parts.
# The kth percentile is the value below which k% of observations fall.
print("\nPercentiles:")
for point in data:
    # Calculate what percentile each data point falls into
    count_below = sum(1 for x in data if x < point)
    percentile = (count_below / len(data)) * 100
    print(f"Data point {point}: approximately {percentile:.1f}th percentile")

# Using numpy's percentile function to find specific percentiles
p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)  # This is the median
p75 = np.percentile(data, 75)
p90 = np.percentile(data, 90)
print(f"\nSpecific percentiles in the dataset:")
print(f"25th percentile: {p25}")
print(f"50th percentile (median): {p50}")
print(f"75th percentile: {p75}")
print(f"90th percentile: {p90}")

# Quartiles
# Quartiles divide the dataset into four equal parts.
print("\nQuartiles:")
q1 = np.percentile(data, 25)  # First quartile (25%)
q2 = np.percentile(data, 50)  # Second quartile (50%) - same as median
q3 = np.percentile(data, 75)  # Third quartile (75%)
print(f"Q1 (25%): {q1}")
print(f"Q2 (50%, median): {q2}")
print(f"Q3 (75%): {q3}")

# Interquartile Range (IQR)
# IQR is the difference between the third and first quartiles
iqr = q3 - q1
print(f"Interquartile Range (IQR): {iqr}")

# Using IQR to identify potential outliers
# A common rule is that values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR are potential outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(f"\nOutlier boundaries using IQR method:")
print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")
outliers = [x for x in data if x < lower_bound or x > upper_bound]
if outliers:
    print(f"Potential outliers: {outliers}")
else:
    print("No outliers detected using the IQR method.")