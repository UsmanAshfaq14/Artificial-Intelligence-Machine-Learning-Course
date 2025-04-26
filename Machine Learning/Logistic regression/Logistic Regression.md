
[![Logistic Regression: Sigmoid Function and Threshold | by Mukesh ...](https://tse2.mm.bing.net/th?id=OIP.fPrw6E62EvL0ABTxOEq9zgHaEp&pid=Api)](https://medium.com/%40cmukesh8688/logistic-regression-sigmoid-function-and-threshold-b37b82a4cd79)

**Summary:** Logistic Regression is a simple, yet powerful, **binary classification** algorithm that models the probability of an outcome (0 or 1) by applying the **sigmoid function** to a linear combination of input features ([Logistic Regression in Machine Learning – GeeksforGeeks](https://www.geeksforgeeks.org/understanding-logistic-regression/?utm_source=chatgpt.com)). It transforms any real-valued input into the (0,1) interval, yielding interpretable probability estimates ([Logistic regression – Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)). Because its cost function (log-loss) is **convex**, optimization reliably converges to a global minimum ([Cost Function in Logistic Regression – GeeksforGeeks](https://www.geeksforgeeks.org/ml-cost-function-in-logistic-regression/?utm_source=chatgpt.com)). Despite its simplicity, it remains a go-to baseline in fields like healthcare, finance, and social sciences.

---

## Introduction  
Logistic Regression belongs to **supervised learning**, where we train a model on input–output pairs. Use it when your **dependent variable** (target) is **categorical**—for example, “pass/fail” or “spam/not spam”—and your **independent variables** (features) can be numeric or categorical ([Logistic regression – Simple English Wikipedia](https://simple.wikipedia.org/wiki/Logistic_Regression?utm_source=chatgpt.com)).

---

## Key Concepts  

### Independent vs. Dependent Variables  
- **Independent variables** (\(x\)) are the inputs we observe (e.g., hours studied).  
- **Dependent variable** (\(y\)) is the output we predict and must be **discrete** (0 or 1).

### Why Use Logistic Regression?  
- Naturally handles **binary classification** by modeling probabilities.  
- Coefficients \(a_0, a_1\) can be interpreted as changes in **log-odds**, offering clear explainability.  
- Outputs are bounded between 0 and 1, so you never predict impossible probabilities.

---

## The Sigmoid Function  

The **sigmoid** (logistic) function is defined by  
$$
\sigma(z) = \frac{1}{1 + e^{-z}},
$$  
where \(z = a_0 + a_1 x\). This yields the **hypothesis**  
$$
P(y=1 \mid x) \;=\; h(x) \;=\; \sigma\bigl(a_0 + a_1 x\bigr)
               = \frac{1}{1 + e^{-(a_0 + a_1 x)}}.
$$  
- As \(z \to +\infty\), \(\sigma(z)\to 1\).  
- As \(z \to -\infty\), \(\sigma(z)\to 0\).  
- At \(z=0\), \(\sigma(0)=0.5\).

---

## Formula Breakdown  
- \(y\): **dependent variable** ∈ \(\{0,1\}\) (e.g., fail or pass)  
- \(x\): **independent variable** (feature) (e.g., hours studied)  
- \(a_0\): **intercept** (bias term) shifts the curve left/right  
- \(a_1\): **coefficient** (weight) on \(x\) controls slope (steepness)  

---

## How \(a_0\) and \(a_1\) Shape the Curve  
- A larger \(\lvert a_1\rvert\) makes the S-curve **steeper**, transitioning more sharply between 0 and 1.  
- Changing \(a_0\) **shifts** the midpoint of the curve left or right along the \(x\)-axis.  

---

## Worked Example  

Let’s pick simple values:  
- \(a_0 = -4\)  
- \(a_1 = 2\)  
- \(x = 3\)  

1. **Linear combination**:  
   $$
     z = a_0 + a_1 x = -4 + 2 \times 3 = 2.
   $$  
2. **Sigmoid output**:  
   $$
     P(y=1 \mid x=3)
     = \frac{1}{1 + e^{-2}}
     \approx 0.88.
   $$  

A student studying 3 hours thus has an **88%** chance of passing.

---

## Cost Function & Optimization  

### Log-Loss (Cross-Entropy)  
Training minimizes the **log-loss**:  
$$
J(a_0,a_1)
= -\frac{1}{m}\sum_{i=1}^m\Bigl[y^{(i)}\log h(x^{(i)}) + (1 - y^{(i)})\log\bigl(1 - h(x^{(i)})\bigr)\Bigr].
$$  
This function is **convex**, ensuring a single global minimum.

### Gradient Descent  
Parameters are updated via:  
$$
a_j := a_j - \alpha \,\frac{\partial J}{\partial a_j},
$$  
where \(\alpha\) is the **learning rate**. Variants like **stochastic** or **mini-batch** gradient descent are common on large datasets.

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

-   **`C`** controls strength of regularization: smaller → stronger penalty.
    
-   **Solvers**: `liblinear`, `lbfgs`, `sag`, `saga`, `newton-cg`.
    
-   `.predict_proba()` returns probabilities for each class.
    

