# Univariate Linear Regression with Closed-Form Formula

**Equation: `Y = mX + b`**

**Where:**
- `Y` = output (marks obtained)
- `X` = input (hours studied)
- `m` = slope of the line (how many marks change for 1 more hour studied)
  - `m = sum((X_i - mean(X)) * (Y_i - mean(Y))) / sum((X_i - mean(X))^2)`
- `b` = y-intercept (marks when hours studied = 0)
  - `b = mean(Y) - m * mean(X)`

---

## Predicting Student Marks

- Hours studied: `X = [2, 4, 6, 8, 10]`
- Marks obtained: `Y = [40, 60, 80, 100, 120]`

---

### Step 1: Calculate the mean of X and Y

```
mean(X) = (2 + 4 + 6 + 8 + 10) / 5 = 6
mean(Y) = (40 + 60 + 80 + 100 + 120) / 5 = 80
```

### Step 2: Find deviations and their products/squares

- Compute `X - mean(X)`: `[-4, -2, 0, 2, 4]`
- Compute `Y - mean(Y)`: `[-40, -20, 0, 20, 40]`

| X-mean | Y-mean | product | square of X-mean |
|--------|--------|---------|------------------|
| -4     | -40    | 160     | 16               |
| -2     | -20    | 40      | 4                |
| 0      | 0      | 0       | 0                |
| 2      | 20     | 40      | 4                |
| 4      | 40     | 160     | 16               |
| **Sum**|        | **400** | **40**           |

- Sum of products = 400
- Sum of squares = 40

### Step 3: Calculate the slope `m`
```
m = 400 / 40 = 10
```

### Step 4: Calculate the intercept `b`
```
b = mean(Y) - m * mean(X)
  = 80 - 10 * 6
  = 20
```

### Step 5: Make predictions

The formula is `Y = 10X + 20`.

- For 12 hours: `Y = 10 * 12 + 20 = 140`
- For 24 hours: `Y = 10 * 24 + 20 = 260`

### Extra Predictions
- 5 hours: `Y = 10*5 + 20 = 70`
- 15 hours: `Y = 10*15 + 20 = 170`
- 30 hours: `Y = 10*30 + 20 = 320`

---

## Key Points

1. The data points lie exactly on a straight line, so the fit is perfect (`MSE = 0`, `R^2 = 1`).
2. Slope `m = 10` means each extra hour studied adds 10 marks.
3. Intercept `b = 20` is the starting mark if no hours are studied (extrapolated).
4. Be careful when predicting far outside the studied range (extrapolation).
5. Assumptions: linear relationship, independent points, constant variance of errors.

---

## Python Code Snippet

```python
import numpy as np
import matplotlib.pyplot as plt

# Original data
given_X = np.array([2, 4, 6, 8, 10])
given_Y = np.array([40, 60, 80, 100, 120])

# 1. Calculate means
mean_X = given_X.mean()
mean_Y = given_Y.mean()

# 2. Compute slope (m) and intercept (b)
num = ((given_X - mean_X) * (given_Y - mean_Y)).sum()
den = ((given_X - mean_X)**2).sum()
m = num / den
b = mean_Y - m * mean_X

# 3. Extra points to predict
new_X = np.array([5, 12, 15, 24, 30])
pred_Y = m * new_X + b

# 4. Print results
print(f"Line: Y = {m:.2f}X + {b:.2f}")
for x_val, y_val in zip(new_X, pred_Y):
    print(f"  {x_val} hrs -> {y_val:.2f} marks")

# 5. Plot
all_X = np.concatenate((given_X, new_X))
line_X = np.linspace(all_X.min() - 1, all_X.max() + 1, 100)
line_Y = m * line_X + b

plt.scatter(given_X, given_Y, label='Original data')
plt.scatter(new_X, pred_Y, marker='x', label='New predictions')
plt.plot(line_X, line_Y, label='Best-fit line')
plt.xlabel('Hours Studied (X)')
plt.ylabel('Marks (Y)')
plt.title('Univariate Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
```



