
[![Logistic Regression: Sigmoid Function and Threshold | by Mukesh ...](https://tse2.mm.bing.net/th?id=OIP.fPrw6E62EvL0ABTxOEq9zgHaEp&pid=Api)](https://medium.com/%40cmukesh8688/logistic-regression-sigmoid-function-and-threshold-b37b82a4cd79)

**Summary:** Logistic Regression is a simple, yet powerful, **binary classification** algorithm that models the probability of an outcome (0 or 1) by applying the **sigmoid function** to a linear combination of input features ([Logistic Regression in Machine Learning – GeeksforGeeks](https://www.geeksforgeeks.org/understanding-logistic-regression/?utm_source=chatgpt.com)). It transforms any real-valued input into the (0,1) interval, yielding interpretable probability estimates ([Logistic regression – Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)). Because its cost function (log-loss) is **convex**, optimization reliably converges to a global minimum ([Cost Function in Logistic Regression – GeeksforGeeks](https://www.geeksforgeeks.org/ml-cost-function-in-logistic-regression/?utm_source=chatgpt.com)). Despite its simplicity, it remains a go-to baseline in fields like healthcare, finance, and social sciences.

---

## Introduction

Logistic Regression belongs to **supervised learning**, where we train a model on input–output pairs. Use it when your **dependent variable** (target) is **categorical**—for example, “pass/fail” or “spam/not spam”—and your **independent variables** (features) can be numeric or categorical ([Logistic regression – Simple English Wikipedia](https://simple.wikipedia.org/wiki/Logistic_Regression?utm_source=chatgpt.com)).

---

## Key Concepts

### Independent vs. Dependent Variables

- **Independent variables** (<img src="https://latex.codecogs.com/png.latex?x" alt="x" />) are the inputs we observe (e.g., hours studied).  
- **Dependent variable** (<img src="https://latex.codecogs.com/png.latex?y" alt="y" />) is the output we predict and must be **discrete** (0 or 1).

### Why Use Logistic Regression?

- Naturally handles **binary classification** by modeling probabilities.  
- Coefficients <img src="https://latex.codecogs.com/png.latex?a_0" alt="a_0" />, <img src="https://latex.codecogs.com/png.latex?a_1" alt="a_1" /> can be interpreted as changes in **log-odds**, offering clear explainability.  
- Outputs are bounded between 0 and 1, so you never predict impossible probabilities.

---

## The Sigmoid Function

The **sigmoid** (logistic) function is defined by

<img src="https://latex.codecogs.com/png.latex?\dpi{150}\sigma(z)=\frac{1}{1+e^{-z}}" alt="\sigma(z)=\frac{1}{1+e^{-z}}" />

where <img src="https://latex.codecogs.com/png.latex?z=a_0+a_1x" alt="z = a_0 + a_1 x" />. This yields the **hypothesis**

<img src="https://latex.codecogs.com/png.latex?\dpi{150}P\left(y=1\mid x\right)=h(x)=\sigma\left(a_0+a_1x\right)=\frac{1}{1+e^{-\left(a_0+a_1x\right)}}" alt="P(y=1 | x) = h(x) = \sigma(a_0 + a_1 x) = 1/(1+e^{-(a_0 + a_1 x)})" />

- As <img src="https://latex.codecogs.com/png.latex?z\to+\infty" alt="z → +∞" />, <img src="https://latex.codecogs.com/png.latex?\sigma(z)\to1" alt="\sigma(z) → 1" />.  
- As <img src="https://latex.codecogs.com/png.latex?z\to-\infty" alt="z → −∞" />, <img src="https://latex.codecogs.com/png.latex?\sigma(z)\to0" alt="\sigma(z) → 0" />.  
- At <img src="https://latex.codecogs.com/png.latex?z=0" alt="z = 0" />, <img src="https://latex.codecogs.com/png.latex?\sigma(0)=0.5" alt="\sigma(0) = 0.5" />.

---

## Formula Breakdown

- <img src="https://latex.codecogs.com/png.latex?y" alt="y" />: **dependent variable** ∈ <img src="https://latex.codecogs.com/png.latex?%7B0,1%7D" alt="{0,1}" /> (e.g., fail or pass)  
- <img src="https://latex.codecogs.com/png.latex?x" alt="x" />: **independent variable** (feature) (e.g., hours studied)  
- <img src="https://latex.codecogs.com/png.latex?a_0" alt="a_0" />: **intercept** (bias term) shifts the curve left/right  
- <img src="https://latex.codecogs.com/png.latex?a_1" alt="a_1" />: **coefficient** (weight) on <img src="https://latex.codecogs.com/png.latex?x" alt="x" /> controls slope (steepness)  

---

## How <img src="https://latex.codecogs.com/png.latex?a_0" alt="a_0" /> and <img src="https://latex.codecogs.com/png.latex?a_1" alt="a_1" /> Shape the Curve

- A larger <img src="https://latex.codecogs.com/png.latex?%7Ca_1%7C" alt="|a_1|" /> makes the S-curve **steeper**, transitioning more sharply between 0 and 1.  
- Changing <img src="https://latex.codecogs.com/png.latex?a_0" alt="a_0" /> **shifts** the midpoint of the curve left or right along the <img src="https://latex.codecogs.com/png.latex?x" alt="x" />-axis.  

---

## Worked Example

Let’s pick simple values:  
- <img src="https://latex.codecogs.com/png.latex?a_0=-4" alt="a_0 = -4" />  
- <img src="https://latex.codecogs.com/png.latex?a_1=2" alt="a_1 = 2" />  
- <img src="https://latex.codecogs.com/png.latex?x=3" alt="x = 3" />

1. **Linear combination**:  
   <img src="https://latex.codecogs.com/png.latex?z=a_0+a_1x=-4+2\times3=2" alt="z = a_0 + a_1 x = -4 + 2 × 3 = 2" />

2. **Sigmoid output**:  
   <img src="https://latex.codecogs.com/png.latex?P\left(y=1\mid x=3\right)=\frac{1}{1+e^{-2}}\approx0.88" alt="P(y=1 | x=3) = 1/(1+e^{-2}) ≈ 0.88" />

A student studying 3 hours thus has an **88%** chance of passing.

---

## Cost Function & Optimization

### Log-Loss (Cross-Entropy)

Training minimizes the **log-loss**:  
<img src="https://latex.codecogs.com/png.latex?J(a_0,a_1)=-\frac{1}{m}\sum_{i=1}^{m}\bigl[y^{(i)}\log h(x^{(i)})+(1-y^{(i)})\log\bigl(1-h(x^{(i)})\bigr)\bigr]" alt="J(a_0,a_1) = -1/m Σ [y^(i) log h(x^(i)) + (1 - y^(i)) log(1 - h(x^(i)))]" />

This function is **convex**, ensuring a single global minimum.

### Gradient Descent

Parameters are updated via:  
<img src="https://latex.codecogs.com/png.latex?a_j:=a_j-\alpha\frac{\partial J}{\partial a_j}" alt="a_j := a_j - α ∂J/∂a_j" />

where <img src="https://latex.codecogs.com/png.latex?\alpha" alt="α" /> is the **learning rate**. Variants like **stochastic** or **mini-batch** gradient descent are common on large datasets.

---

## Implementation in Scikit-Learn

```python
# 1) Import libraries
from sklearn.linear_model import LogisticRegression
import numpy as np

# 2) Prepare data
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0,   0,   0,   1,   1,   1])

# 3) Create model
clf = LogisticRegression(penalty='l2', solver='liblinear', C=1.0)
clf.fit(X, y)

# 4) Predict probability
prob = clf.predict_proba(np.array([[3.5]]))[0, 1]
print(f"Probability of pass for 3.5 hours: {prob:.2f}")
```

- **`C`** controls strength of regularization: smaller → stronger penalty.  
- **Solvers**: `liblinear`, `lbfgs`, `sag`, `saga`, `newton-cg`.  
- `.predict_proba()` returns probabilities for each class.  