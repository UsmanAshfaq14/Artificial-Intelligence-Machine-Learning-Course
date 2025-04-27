from sklearn.linear_model import LinearRegression  # brings in our regression algorithm
import numpy as np                               # array-handling tools

# 1) Input data (features):
#    each row is [hours studied, attendance %]
X = np.array([
    [2,  80],
    [4,  85],
    [6,  90],
    [8,  95],
    [10, 100]
])

# 2) Output data (targets):
#    corresponding exam scores
y = np.array([40, 60, 80, 100, 120])

# 3) Create the model:
model = LinearRegression()
#    This will learn a plane (in 2D feature space) y = m1*X1 + m2*X2 + b.

# 4) Train the model:
model.fit(X, y)
#    Under the hood, it finds the coefficients and intercept that minimize
#    the sum of squared errors.

# 5) Inspect the learned parameters:
print(f"Slope for hours studied (m1): {model.coef_[0]:.2f}")
print(f"Slope for attendance     (m2): {model.coef_[1]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

# 6) Predict on new data:
#    e.g., a student who studies 12 hours and has 95% attendance
new_student = np.array([[12, 95]])
predicted_score = model.predict(new_student)

# 7) Print formatted result:
print(f"Predicted score for 12 hrs study & 95% attendance: {predicted_score[0]:.2f}")
