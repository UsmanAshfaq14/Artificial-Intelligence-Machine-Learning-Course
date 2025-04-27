# Multiple Linear Regression with Closed-Form Formula

**Equation: `Y = m1*X1 + m2*X2 + ... + mn*Xn + b`**

**Where:**
- `Y` = output (marks obtained)
- `X1, X2, ..., Xn` = inputs (hours studied, attendance, etc.)
- `m1, m2, ..., mn` = slopes (how many marks change for one-unit change in each input)
  - `mi = sum((Xi - mean(Xi)) * (Y - mean(Y))) / sum((Xi - mean(Xi))^2)`
- `b` = intercept (marks when all inputs = 0)
  - `b = mean(Y) - m1*mean(X1) - m2*mean(X2) - ... - mn*mean(Xn)`

---

## Predicting Student Marks

- Hours studied: `X1 = [2, 4, 6, 8, 10]`
- Attendance (%): `X2 = [80, 85, 90, 95, 100]`
- Marks obtained: `Y  = [40, 60, 80, 100, 120]`

---

## Step 1: Calculate the mean of each variable
```
mean(X1) = (2 + 4 + 6 + 8 + 10) / 5 = 6
mean(X2) = (80 + 85 + 90 + 95 + 100) / 5 = 90
mean(Y)  = (40 + 60 + 80 + 100 + 120) / 5 = 80
```

## Step 2: Compute deviations, products, and squares

- `X1 - mean(X1)`: `[-4, -2, 0, 2, 4]`
- `X2 - mean(X2)`: `[-10, -5, 0, 5, 10]`
- `Y  - mean(Y)` : `[-40, -20, 0, 20, 40]`

| Variable | Deviation | Deviation * (Y-mean) | Squared Deviation |
|----------|-----------|----------------------|-------------------|
| X1       | -4, -2, 0, 2, 4     | 160, 40, 0, 40, 160  | 16, 4, 0, 4, 16   |
| X2       | -10, -5, 0, 5, 10   | 400, 100, 0, 100, 400| 100, 25, 0, 25,100|

- Sum for X1: `sum(dev*Y_dev) = 400`, `sum(dev^2) = 40`
- Sum for X2: `sum(dev*Y_dev) =1000`, `sum(dev^2) =250`

## Step 3: Calculate slopes m1 and m2
```
m1 = 400 / 40   = 10
m2 = 1000 / 250 = 4
```

## Step 4: Calculate intercept b
```
b = mean(Y)
  - m1 * mean(X1)
  - m2 * mean(X2)
  = 80 - 10*6 - 4*90
  = 80 - 60 - 360
  = -340
```

The fitted formula is:
```
Y = 10*X1 + 4*X2 - 340
```

## Step 5: Predict for a new student
```
X1 = 12 hours, X2 = 95%
Y = 10*12 + 4*95 - 340
  = 120 + 380 - 340
  = 160 marks
```

---

## Key Points
1. Each extra hour studied adds `m1=10` marks.
2. Each extra percent attendance adds `m2=4` marks.
3. The intercept `b=-340` is the starting offset (applied when X1 and X2 are zero).
4. Data fit perfectly (MSE=0, R²=1) in this example.
5. Be cautious when predicting far outside the training range.

---

## Python Code Snippet
```python
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
```



