# Extended Univariate Linear Regression with Extra Predictions and Plot

import matplotlib.pyplot as plt
#UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 11: character maps to <undefined>
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Check if the user provided an argument for the number of extra predictions

# 1. Original dataset (hours studied → marks obtained)
x = [2, 4, 6, 8, 10]           # independent variable (X)
y = [40, 60, 80, 100, 120]     # dependent variable (Y)

# 2. Calculate means of X and Y
mean_x = sum(x) / len(x)       # average of hours studied
mean_y = sum(y) / len(y)       # average of marks obtained

# 3. Compute slope (m) and intercept (b) using closed-form formulas
#    m = Σ[(xi - mean_x)*(yi - mean_y)] / Σ[(xi - mean_x)**2]
num = sum((xi - mean_x)*(yi - mean_y) for xi, yi in zip(x, y))
den = sum((xi - mean_x)**2 for xi in x)
m = num / den                  # slope of the best-fit line

#    b = mean_y - m * mean_x
b = mean_y - m * mean_x        # y-intercept of the best-fit line

# 4. Define extra data points for prediction
extra_hours = [12, 24, 30, 5, 15]

# 5. Compute predictions for all extra points
predictions = {hrs: m*hrs + b for hrs in extra_hours}

# 6. Print learned model and predictions
print(f"Learned model: Y = {m:.2f}·X + {b:.2f}")
print("Predictions for extra study hours:")
for hrs, mark in predictions.items():
    print(f"  {hrs:2d} hours → {mark:.2f} marks")

# 7. Plotting
plt.figure(figsize=(8, 5))

#   a) original data points
plt.scatter(x, y, label="Original data", marker='o')

#   b) extra data points
plt.scatter(extra_hours, list(predictions.values()), 
            label="Extra predictions", marker='x')

#   c) regression line
#      create a range of X values for the line
x_line = [min(x + extra_hours) - 1, max(x + extra_hours) + 1]
y_line = [m*xi + b for xi in x_line]
plt.plot(x_line, y_line, label=f"Fit: Y = {m:.1f}X + {b:.1f}")

# 8. Labels and legend
plt.title("Hours Studied vs. Marks Obtained")
plt.xlabel("Hours Studied (X)")
plt.ylabel("Marks Obtained (Y)")
plt.legend()
plt.grid(True)

# 9. Display the plot
plt.show()
