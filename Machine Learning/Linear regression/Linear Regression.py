from sklearn.linear_model import LinearRegression  # brings in our regression algorithm
import numpy as np                               # array-handling tools

# 1) Input data (features):
X = np.array([[1], [2], [3], [4], [5]])
#    5 examples → hours studied 1–5.

# 2) Output data (targets):
y = np.array([50, 55, 65, 70, 75])
#    Corresponding exam scores out of 100.

# 3) Create the model:
model = LinearRegression()
#    This will learn a straight line y = m*x + b that best fits the data.

# 4) Train the model:
model.fit(X, y)
#    Under the hood, it finds the slope (m) and intercept (b) that minimize the
#    sum of squared differences between predicted and actual scores.

# 5) Predict on new data:
predicted_score = model.predict(np.array([[6]]))
#    If a student studies 6 hours, what score do we expect?

# 6) Print formatted result:
print(f"Predicted score for 6 hours: {predicted_score[0]:.2f}")
# Output: Predicted score for 6 hours: 77.78
