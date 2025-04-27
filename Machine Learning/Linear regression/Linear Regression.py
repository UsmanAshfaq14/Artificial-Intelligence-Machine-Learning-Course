from sklearn.linear_model import LinearRegression  # brings in our regression algorithm
import numpy as np                               # array-handling tools

# 1) Input data (features):
X = np.array([[2], [4], [6], [8], [10]])
#    5 examples → hours studied 2-10.

# 2) Output data (targets):
y = np.array([40, 60, 80, 100, 120])
#    Corresponding exam scores out of 150.

# 3) Create the model:
model = LinearRegression()
#    This will learn a straight line y = m*x + b that best fits the data.

# 4) Train the model:
model.fit(X, y)
#    Under the hood, it finds the slope (m) and intercept (b) that minimize the
#    sum of squared differences between predicted and actual scores.

# 5) Predict on new data:
predicted_score = model.predict(np.array([[5]]))
#    If a student studies 6 hours, what score do we expect?

# 6) Print formatted result:
print(f"Predicted score for 12 hours: {predicted_score[0]:.2f}")
#    If a student studies 12 hours, we expect them to score 140.00.
