import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from matplotlib.gridspec import GridSpec

# Sample data
data = [4, 10, 29, 33, 42, 67]

# Calculate statistical measures
mean_value = np.mean(data)
median_value = np.median(data)
std_dev_value = np.std(data, ddof=1)  # Sample standard deviation

# Calculate z-scores for all data points
z_scores = [(x - mean_value) / std_dev_value for x in data]
percentiles = [stats.percentileofscore(data, x) for x in data]
quartiles = np.percentile(data, [25, 50, 75])
q1, q2, q3 = quartiles
iqr_value = q3 - q1

# Create the figure for Measures of Position
plt.figure(figsize=(12, 10))
gs = GridSpec(3, 2, height_ratios=[3, 3, 2], wspace=0.3, hspace=0.4)

# 1. Z-Score Visualization
ax_z = plt.subplot(gs[0, :])
bars = ax_z.bar(np.arange(len(data)), z_scores, color='skyblue', alpha=0.7)
ax_z.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax_z.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='±1 std dev')
ax_z.axhline(y=-1, color='red', linestyle='--', alpha=0.7)
ax_z.axhline(y=2, color='orange', linestyle=':', alpha=0.7, label='±2 std dev')
ax_z.axhline(y=-2, color='orange', linestyle=':', alpha=0.7)

# Add value labels on top of bars
for i, (d, z) in enumerate(zip(data, z_scores)):
    ax_z.annotate(f'{d}\n(z={z:.2f})', xy=(i, z), xytext=(0, 5 if z >= 0 else -15),
                 textcoords='offset points', ha='center', va='bottom' if z >= 0 else 'top',
                 fontsize=9, fontweight='bold')

ax_z.set_title('Z-Scores for Each Data Point', fontsize=14, fontweight='bold')
ax_z.set_xlabel('Data Point Index', fontsize=12)
ax_z.set_ylabel('Z-Score (Standard Deviations from Mean)', fontsize=12)
ax_z.set_xticks(np.arange(len(data)))
ax_z.set_xticklabels([f'#{i+1}' for i in range(len(data))])
ax_z.legend(loc='upper right')

# Add explanation for z-scores
z_score_exp = """
Z-SCORE EXPLAINED:

• Z-score represents how many standard deviations a data point is from the mean
• Z-score = (x - mean) / standard deviation
• Positive z-score: Above the mean
• Negative z-score: Below the mean
• About 68% of data falls between z = -1 and z = 1
• About 95% of data falls between z = -2 and z = 2
• Values with |z| > 2 are often considered unusual
• Z-scores allow comparison of values from different distributions
"""
ax_z.text(0.02, -2.5, z_score_exp, transform=ax_z.transAxes, fontsize=9,
          bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

# 2. Percentile Visualization
ax_perc = plt.subplot(gs[1, 0])
# Sort data and corresponding percentiles for visualization
sorted_indices = np.argsort(data)
sorted_data = [data[i] for i in sorted_indices]
sorted_percentiles = [percentiles[i] for i in sorted_indices]

# Create percentile curves
ax_perc.plot(sorted_data, sorted_percentiles, 'bo-', linewidth=2)
ax_perc.axhline(y=25, color='green', linestyle='--', alpha=0.7, label='Q1 (25%)')
ax_perc.axhline(y=50, color='red', linestyle='-', alpha=0.7, label='Median (50%)')
ax_perc.axhline(y=75, color='purple', linestyle='--', alpha=0.7, label='Q3 (75%)')

# Add annotations for specific data points
for i, (d, p) in enumerate(zip(sorted_data, sorted_percentiles)):
    ax_perc.annotate(f'{d}\n({p:.1f}%)', xy=(d, p), xytext=(0, 5),
                    textcoords='offset points', ha='center', va='bottom',
                    fontsize=8, fontweight='bold')

ax_perc.set_title('Percentile Distribution', fontsize=12, fontweight='bold')
ax_perc.set_xlabel('Data Value', fontsize=10)
ax_perc.set_ylabel('Percentile', fontsize=10)
ax_perc.set_ylim(0, 105)
ax_perc.legend(loc='upper left')

# 3. Quartile Visualization
ax_quartile = plt.subplot(gs[1, 1])
# Create a more detailed box plot
sns.boxplot(y=data, ax=ax_quartile, color='skyblue')

# Add annotations for quartiles
quartile_annotations = [
    (q3, 'Q3 (75%)', 0.4),
    (q2, 'Median', 0.4),
    (q1, 'Q1 (25%)', 0.4)
]

for val, label, offset in quartile_annotations:
    ax_quartile.annotate(f"{label}: {val:.1f}", xy=(0, val), xytext=(offset, 0),
                        xycoords=('axes fraction', 'data'), textcoords=('axes fraction', 'data'),
                        arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                        fontsize=9)

ax_quartile.set_title('Quartile Analysis', fontsize=12, fontweight='bold')
ax_quartile.set_xlabel('', fontsize=10)
ax_quartile.set_ylabel('Data Values', fontsize=10)

# 4. Explanation of Percentiles and Quartiles
ax_pos_exp = plt.subplot(gs[2, :])
ax_pos_exp.axis('off')

pos_exp = """
MEASURES OF POSITION EXPLAINED:

Z-SCORES:
• Z = (x - mean) / standard deviation
• Standardized measures that convert values to standard deviation units
• Allow comparison across different datasets with different units
• Common interpretations: |z| > 1.96 (unusual in both tails at 5% significance level)

PERCENTILES:
• The pth percentile is the value below which p% of observations fall
• 50th percentile = median
• Used in standardized testing (e.g., "scored in the 90th percentile")
• Percentile rank: percentage of scores in distribution at or below a given value

QUARTILES:
• Quartiles divide data into four equal parts (25% each)
• Q1 (25th percentile): First quartile, 25% of data falls below this value
• Q2 (50th percentile): Second quartile, same as median
• Q3 (75th percentile): Third quartile, 75% of data falls below this value
• IQR (Interquartile Range) = Q3 - Q1: Contains middle 50% of data
• Used for outlier detection: Values < Q1 - 1.5×IQR or > Q3 + 1.5×IQR are potential outliers

For this dataset:
• Z-scores range from {:.2f} to {:.2f}
• Q1 (25%) = {:.2f}, Median (50%) = {:.2f}, Q3 (75%) = {:.2f}
• IQR = {:.2f}
""".format(min(z_scores), max(z_scores), q1, q2, q3, iqr_value)

ax_pos_exp.text(0.5, 0.5, pos_exp, ha='center', va='center', fontsize=10,
              bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

plt.suptitle('Measures of Position: Z-Scores, Percentiles & Quartiles', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()