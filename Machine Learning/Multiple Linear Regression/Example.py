import numpy as np
import matplotlib.pyplot as plt

# Given data
X1 = np.array([2, 4, 6, 8, 10])   # hours studied
X2 = np.array([80, 85, 90, 95, 100]) # attendance %
Y  = np.array([40, 60, 80, 100, 120]) # marks obtained

# 1. Means
mean_X1, mean_X2, mean_Y = X1.mean(), X2.mean(), Y.mean()

# 2. Deviations
d1, d2, dY = X1 - mean_X1, X2 - mean_X2, Y - mean_Y

# 3. Slopes
m1 = (d1 * dY).sum() / (d1**2).sum()
m2 = (d2 * dY).sum() / (d2**2).sum()

# 4. Intercept
b = mean_Y - m1*mean_X1 - m2*mean_X2

# 5. Predict for new student
new_X1, new_X2 = 12, 95
predicted_Y = m1*new_X1 + m2*new_X2 + b
print(f"Predicted marks for hours={new_X1}, attendance={new_X2}%: {predicted_Y:.2f}")

# 6. Plot Actual vs Predicted
predictions = m1*X1 + m2*X2 + b
plt.scatter(Y, predictions, label='Predicted vs Actual')
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--', label='Ideal')
plt.xlabel('Actual Marks')
plt.ylabel('Predicted Marks')
plt.title('Multiple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()