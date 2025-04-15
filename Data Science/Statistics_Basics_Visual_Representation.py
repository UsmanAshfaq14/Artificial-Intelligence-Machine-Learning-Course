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
# Handle scipy's mode function based on version
try:
    # For newer scipy versions
    mode_result = stats.mode(data, keepdims=True)
    mode_value = mode_result.mode[0]
except TypeError:
    # For older scipy versions
    mode_result = stats.mode(data)
    mode_value = mode_result.mode[0]

variance_value = np.var(data, ddof=1)  # Sample variance
std_dev_value = np.std(data, ddof=1)   # Sample standard deviation
skewness_value = stats.skew(data)
kurtosis_value = stats.kurtosis(data)
range_value = max(data) - min(data)
iqr_value = np.percentile(data, 75) - np.percentile(data, 25)
q1, q3 = np.percentile(data, [25, 75])

# Determine skewness type for explanation
if abs(skewness_value) < 0.5:
    skew_type = "approximately symmetric"
elif 0.5 <= skewness_value < 1 or -1 < skewness_value <= -0.5:
    skew_type = "moderately skewed"
else:
    skew_type = "highly skewed"

if skewness_value > 0:
    skew_direction = "right (positive)"
    skew_explanation = "longer tail extends to the right, mean > median"
else:
    skew_direction = "left (negative)"
    skew_explanation = "longer tail extends to the left, mean < median"

# Determine kurtosis type
if kurtosis_value < -0.5:
    kurtosis_type = "platykurtic"
    kurtosis_explanation = "flatter than normal distribution with thinner tails"
elif kurtosis_value > 0.5:
    kurtosis_type = "leptokurtic"
    kurtosis_explanation = "more peaked than normal distribution with fatter tails"
else:
    kurtosis_type = "mesokurtic"
    kurtosis_explanation = "similar to normal distribution"

# Calculate optimal bin size
bin_width = 2 * iqr_value * (len(data) ** (-1/3))
n_bins = int(np.ceil((max(data) - min(data)) / bin_width)) if bin_width > 0 else 10
n_bins = max(5, min(n_bins, 15))  # Keep bins between 5 and 15

# Function to create title with clear border
def create_title_with_border(ax, title):
    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    ax.spines['top'].set_visible(True)
    ax.spines['top'].set_linewidth(2)
    ax.spines['top'].set_color('#4472C4')

# Function to add an explanation textbox
def add_explanation_box(ax, text, position=(0.5, 0.02)):
    props = dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4')
    ax.text(position[0], position[1], text, transform=ax.transAxes, fontsize=9,
            va='bottom', ha='center', bbox=props)

#----------------------------------------------------------------------------------
# PLOT 1: Central Tendency (Mean, Median, Mode)
#----------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
ax = plt.gca()
sns.histplot(data, kde=True, color='skyblue', bins=n_bins, ax=ax)

# Add vertical lines for mean, median, and mode
plt.axvline(mean_value, color='red', linestyle='--', linewidth=2, 
            label=f'Mean: {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='-', linewidth=2, 
            label=f'Median: {median_value:.2f}')
plt.axvline(mode_value, color='blue', linestyle='-.', linewidth=2, 
            label=f'Mode: {mode_value:.2f}')

create_title_with_border(ax, 'Central Tendency Measures')
plt.xlabel('Data Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(loc='upper right', fontsize=10)

explanation = """
CENTRAL TENDENCY MEASURES EXPLAINED:

• Mean (red dashed line): The average of all values ({:.2f})
  - Calculated by summing all values and dividing by the count
  - Sensitive to outliers
  - Best used with symmetric distributions

• Median (green solid line): The middle value when sorted ({:.2f})
  - 50% of values are above, 50% are below
  - Robust to outliers
  - Better representation for skewed data

• Mode (blue dash-dot line): Most frequently occurring value ({:.2f})
  - The peak(s) of the distribution
  - There can be multiple modes
  - Best for categorical data or detecting clusters
""".format(mean_value, median_value, mode_value)

add_explanation_box(ax, explanation, (0.5, -0.02))
plt.tight_layout()
plt.subplots_adjust(bottom=0.35)
# plt.show()  # Commented out for now, will show all at end

#----------------------------------------------------------------------------------
# PLOT 2: Dispersion Measures (Standard Deviation, Variance, Range, IQR)
#----------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))

# Create 2x2 grid
gs = GridSpec(2, 2, width_ratios=[3, 2], height_ratios=[1, 1], wspace=0.3, hspace=0.3)

# Main histogram with standard deviation
ax1 = plt.subplot(gs[:, 0])  # Take full first column
sns.histplot(data, kde=True, color='skyblue', bins=n_bins, ax=ax1)
ax1.axvline(mean_value, color='red', linestyle='--', linewidth=2, 
           label=f'Mean: {mean_value:.2f}')

# Add standard deviation bands
for i in range(1, 3):
    # Positive direction
    ax1.axvline(mean_value + i*std_dev_value, color='purple', alpha=0.7-i*0.2, 
               linestyle=':', linewidth=1.5, 
               label=f'+{i} Std Dev: {mean_value + i*std_dev_value:.2f}')
    # Negative direction
    ax1.axvline(mean_value - i*std_dev_value, color='purple', alpha=0.7-i*0.2, 
               linestyle=':', linewidth=1.5, 
               label=f'-{i} Std Dev: {mean_value - i*std_dev_value:.2f}')

ax1.set_title('Standard Deviation & Variance', fontsize=12, fontweight='bold')
ax1.set_xlabel('Data Values', fontsize=10)
ax1.set_ylabel('Frequency', fontsize=10)
ax1.legend(loc='upper right', fontsize=8)

# Box plot showing IQR
ax2 = plt.subplot(gs[0, 1])
sns.boxplot(y=data, ax=ax2, color='skyblue')
ax2.set_title('Box Plot (IQR)', fontsize=12, fontweight='bold')
ax2.set_ylabel('')

# Range visualization
ax3 = plt.subplot(gs[1, 1])
ax3.plot(data, [1]*len(data), 'bo', markersize=8)
ax3.axvline(min(data), color='green', linestyle='-', linewidth=2, label=f'Min: {min(data)}')
ax3.axvline(max(data), color='red', linestyle='-', linewidth=2, label=f'Max: {max(data)}')
ax3.axhline(1, color='skyblue', linestyle='-', linewidth=2)
ax3.set_ylim(0.5, 1.5)
ax3.set_yticks([])
ax3.set_title(f'Range: {range_value}', fontsize=12, fontweight='bold')
ax3.legend(loc='upper right', fontsize=8)

plt.suptitle('Dispersion Measures', fontsize=14, fontweight='bold')

explanation = """
DISPERSION MEASURES EXPLAINED:

• Standard Deviation ({:.2f}): Average distance of data points from the mean
  - Smaller values indicate data clustered closely around the mean
  - Larger values indicate more spread-out data
  - Approximately 68% of data falls within ±1 standard deviation from mean
  - Approximately 95% of data falls within ±2 standard deviations from mean

• Variance ({:.2f}): Square of the standard deviation
  - Measures average squared deviation from the mean
  - More sensitive to outliers than standard deviation

• Range ({:.2f}): Difference between maximum and minimum values
  - Simplest measure of spread, but highly sensitive to outliers

• Interquartile Range (IQR) ({:.2f}): Range of middle 50% of data (Q3-Q1)
  - More robust to outliers than range or standard deviation
  - Used to identify potential outliers (points > Q3+1.5*IQR or < Q1-1.5*IQR)
""".format(std_dev_value, variance_value, range_value, iqr_value)

plt.figtext(0.5, 0.01, explanation, ha='center', fontsize=9, 
            bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

plt.tight_layout()
plt.subplots_adjust(bottom=0.35)
# plt.show()  # Commented out for now

#----------------------------------------------------------------------------------
# PLOT 3: Distribution Shape (Skewness and Kurtosis)
#----------------------------------------------------------------------------------
plt.figure(figsize=(12, 7))
gs = GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[3, 1], wspace=0.3, hspace=0.4)

# Skewness visualization
ax1 = plt.subplot(gs[0, 0])
sns.histplot(data, kde=True, color='skyblue', bins=n_bins, ax=ax1)
ax1.axvline(mean_value, color='red', linestyle='--', linewidth=2, 
           label=f'Mean: {mean_value:.2f}')
ax1.axvline(median_value, color='green', linestyle='-', linewidth=2, 
           label=f'Median: {median_value:.2f}')

ax1.set_title(f'Skewness: {skewness_value:.2f} ({skew_type} to {skew_direction})', 
             fontsize=12, fontweight='bold')
ax1.set_xlabel('Data Values', fontsize=10)
ax1.set_ylabel('Frequency', fontsize=10)
ax1.legend(loc='upper right', fontsize=8)

# Kurtosis visualization (using the same histogram)
ax2 = plt.subplot(gs[0, 1])
sns.kdeplot(data, color='blue', ax=ax2, fill=True, alpha=0.3)
ax2.set_title(f'Kurtosis: {kurtosis_value:.2f} ({kurtosis_type})', 
             fontsize=12, fontweight='bold')
ax2.set_xlabel('Data Values', fontsize=10)
ax2.set_ylabel('Density', fontsize=10)

# Illustrations for different types of skewness
ax3 = plt.subplot(gs[1, 0])
ax3.axis('off')

# Skewness explanation
skew_exp = (
    f"SKEWNESS: {skewness_value:.2f} - {skew_type} to {skew_direction}\n\n"
    f"• {skew_explanation}\n"
    "• Positive skew: Tail extends to right (higher values)\n"
    "• Negative skew: Tail extends to left (lower values)\n"
    "• Symmetric: Mean = Median (approx.)"
)
ax3.text(0.5, 0.5, skew_exp, ha='center', va='center', fontsize=9,
        bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

# Kurtosis explanation
ax4 = plt.subplot(gs[1, 1])
ax4.axis('off')

kurt_exp = (
    f"KURTOSIS: {kurtosis_value:.2f} - {kurtosis_type}\n\n"
    f"• {kurtosis_explanation}\n"
    "• Leptokurtic (>0): Peaked with heavy tails (more outliers)\n"
    "• Platykurtic (<0): Flat with light tails (fewer outliers)\n"
    "• Mesokurtic (≈0): Similar to normal distribution"
)
ax4.text(0.5, 0.5, kurt_exp, ha='center', va='center', fontsize=9,
        bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

plt.suptitle('Distribution Shape: Skewness & Kurtosis', fontsize=14, fontweight='bold')
plt.tight_layout()
# plt.show()  # Commented out for now

#----------------------------------------------------------------------------------
# PLOT 4: Comprehensive Analysis (Full Page with Details)
#----------------------------------------------------------------------------------
plt.figure(figsize=(12, 12))
gs = GridSpec(4, 2, height_ratios=[3, 3, 3, 2], width_ratios=[2, 1], hspace=0.4, wspace=0.3)

# 1. Main histogram with all central tendency lines
ax_main = plt.subplot(gs[0, :])
sns.histplot(data, kde=True, color='skyblue', bins=n_bins, ax=ax_main)

# Add vertical lines for mean, median, and mode
ax_main.axvline(mean_value, color='red', linestyle='--', linewidth=1.5, 
              label=f'Mean: {mean_value:.2f}')
ax_main.axvline(median_value, color='green', linestyle='-', linewidth=1.5, 
              label=f'Median: {median_value:.2f}')
ax_main.axvline(mode_value, color='blue', linestyle='-.', linewidth=1.5, 
              label=f'Mode: {mode_value:.2f}')

# Add standard deviation bands
ax_main.axvline(mean_value + std_dev_value, color='purple', alpha=0.5, 
              linestyle=':', linewidth=1.5, 
              label=f'+1 Std Dev: {mean_value + std_dev_value:.2f}')
ax_main.axvline(mean_value - std_dev_value, color='purple', alpha=0.5, 
              linestyle=':', linewidth=1.5, 
              label=f'-1 Std Dev: {mean_value - std_dev_value:.2f}')

ax_main.set_title('Distribution Analysis with Central Tendency & Spread', fontsize=14, fontweight='bold')
ax_main.set_xlabel('Data Values', fontsize=12)
ax_main.set_ylabel('Frequency', fontsize=12)
ax_main.legend(loc='upper right', fontsize=9)

# Add skewness and kurtosis info
stats_text = (
    f"Distribution Shape:\n"
    f"• Skewness: {skewness_value:.2f} ({skew_type} to {skew_direction})\n"
    f"• Kurtosis: {kurtosis_value:.2f} ({kurtosis_type})"
)
ax_main.text(0.02, 0.95, stats_text, transform=ax_main.transAxes, 
            fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

# 2. Box plot with detailed annotations
ax_box = plt.subplot(gs[1, 0])
sns.boxplot(y=data, ax=ax_box, color='skyblue')
ax_box.set_title('Box Plot with Quartiles', fontsize=12, fontweight='bold')
ax_box.set_ylabel('Data Values', fontsize=10)

# Add annotations to box plot
min_val, q1, q2, q3, max_val = np.percentile(data, [0, 25, 50, 75, 100])
y_pos = 0
box_annotations = [
    (max_val, 'Maximum', 0.6),
    (q3, 'Q3 (75%)', 0.6),
    (q2, 'Median', 0.6),
    (q1, 'Q1 (25%)', 0.6),
    (min_val, 'Minimum', 0.6)
]

for val, label, offset in box_annotations:
    ax_box.annotate(f"{label}: {val:.1f}", xy=(0, val), xytext=(offset, val),
                   arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                   fontsize=9)

# 3. Statistics explanation
ax_box_exp = plt.subplot(gs[1, 1])
ax_box_exp.axis('off')
box_explanation = (
    "BOX PLOT MEASUREMENTS:\n\n"
    f"• IQR = {iqr_value:.2f} (Q3 - Q1)\n"
    f"• Q1 = {q1:.2f} (25th percentile)\n"
    f"• Median = {median_value:.2f} (50th percentile)\n"
    f"• Q3 = {q3:.2f} (75th percentile)\n"
    f"• Range = {range_value:.2f} (Max - Min)\n"
    f"• Potential outliers: < {q1-1.5*iqr_value:.2f} or > {q3+1.5*iqr_value:.2f}"
)
ax_box_exp.text(0.5, 0.5, box_explanation, va='center', ha='center', fontsize=10,
              bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

# 4. Detailed statistics table
ax_table = plt.subplot(gs[2, :])
ax_table.axis('off')

# Create a DataFrame for the statistics table
stats_df = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Mode', 'Standard Deviation', 'Variance', 
                 'Range', 'IQR', 'Skewness', 'Kurtosis'],
    'Value': [f"{mean_value:.2f}", f"{median_value:.2f}", f"{mode_value:.2f}", 
             f"{std_dev_value:.2f}", f"{variance_value:.2f}", 
             f"{range_value:.2f}", f"{iqr_value:.2f}",
             f"{skewness_value:.2f}", f"{kurtosis_value:.2f}"],
    'Definition': [
        "Average of all values", 
        "Middle value when sorted", 
        "Most frequent value", 
        "Average distance from mean",
        "Square of standard deviation",
        "Max - Min values",
        "Range of middle 50% (Q3-Q1)",
        "Asymmetry of distribution",
        "Peakedness of distribution"
    ],
    'Interpretation': [
        f"{'>' if mean_value > median_value else '<'} median indicates {skew_direction} skew", 
        "50% of values are above/below", 
        "Peak of the distribution", 
        f"{std_dev_value/mean_value*100:.1f}% of mean (coefficient of variation)",
        "Higher values = more spread data",
        "Sensitive to outliers",
        "Robust measure of spread",
        f"{skew_type} to the {skew_direction}",
        f"{kurtosis_type}"
    ]
})

# Create the table with more space
table = ax_table.table(
    cellText=stats_df.values,
    colLabels=stats_df.columns,
    loc='center',
    cellLoc='left',
    colWidths=[0.15, 0.1, 0.3, 0.3]
)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Header row
        cell.set_text_props(fontweight='bold', color='white')
        cell.set_facecolor('#4472C4')
    elif row % 2 == 1:  # Alternate row colors
        cell.set_facecolor('#D9E1F2')

ax_table.set_title('Comprehensive Statistical Analysis', fontsize=14, fontweight='bold', pad=20)

# 5. Summary insights
ax_insights = plt.subplot(gs[3, :])
ax_insights.axis('off')

# Create insights text based on data characteristics
if skewness_value > 0.5:
    skew_insight = "Distribution has significant positive skew, meaning mean > median. Consider using median for central tendency."
elif skewness_value < -0.5:
    skew_insight = "Distribution has significant negative skew, meaning mean < median. Consider using median for central tendency."
else:
    skew_insight = "Distribution is approximately symmetric, both mean and median are suitable measures of central tendency."

if std_dev_value/mean_value > 0.5:
    spread_insight = "Data shows high variability relative to the mean (high coefficient of variation)."
else:
    spread_insight = "Data shows moderate to low variability relative to the mean."

insights = (
    "SUMMARY INSIGHTS:\n\n"
    f"1. {skew_insight}\n\n"
    f"2. {spread_insight}\n\n"
    f"3. Distribution is {kurtosis_type}, which means it has {kurtosis_explanation}.\n\n"
    f"4. The middle 50% of values fall within the range of {q1:.2f} to {q3:.2f}."
)

ax_insights.text(0.5, 0.5, insights, va='center', ha='center', fontsize=10,
               bbox=dict(facecolor='#f0f0f0', alpha=0.8, edgecolor='#4472C4'))

plt.suptitle('Complete Statistical Analysis', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.95)

plt.show()  # Show all figures