## Images:
![A Guide to Activation functions in Artificial Neural Networks](https://tse2.mm.bing.net/th?id=OIP.cH9yqgrUxVyeg0Gy-Nc_LAHaFw&cb=iwc1&pid=Api)  
![Plot Decision Boundary in Logistic Regression: Python Example](https://tse1.mm.bing.net/th?id=OIP.0YoS7XYANPk2evRz06EBFwHaF1&pid=Api)  
![One versus Rest Logistic Regression [56]. | Download Scientific Diagram](https://tse4.mm.bing.net/th?id=OIP.hNVjYLcBwxrENOQFHcBcNgHaGh&pid=Api)  
![How to implement multinomial logistic regression in Python](https://tse2.mm.bing.net/th?id=OIP.zSlNiy0SG5GCsT2R8l20WwHaIh&pid=Api)

**Summary:** Multiclass (or multinomial) logistic regression extends binary logistic regression to predict one of <img src="https://latex.codecogs.com/png.latex?K%3E2" alt="K>2" /> classes by modeling a probability distribution over the classes using the **softmax** function. It offers both direct optimization of the multinomial loss and reduction to binary subproblems via **one-vs-rest** (OvR) or **one-vs-one** (OvO) strategies, with parameters learned by minimizing **categorical cross-entropy** using gradient-based solvers like L-BFGS or SAGA ([en.wikipedia.org](https://en.wikipedia.org/wiki/Multinomial_logistic_regression?utm_source=chatgpt.com), [en.wikipedia.org](https://en.wikipedia.org/wiki/Softmax_function?utm_source=chatgpt.com), [scikit-learn.org](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html?utm_source=chatgpt.com)).

## Introduction  
Multiclass logistic regression is a type of **supervised learning** used when the **dependent variable** can take one of <img src="https://latex.codecogs.com/png.latex?K" alt="K" /> discrete categories (e.g., digit labels 0–9) and the **independent variables** (features) are numeric or categorical ([en.wikipedia.org](https://en.wikipedia.org/wiki/Multinomial_logistic_regression?utm_source=chatgpt.com)).  
It predicts the probability <img src="https://latex.codecogs.com/png.latex?\dpi{150}P\left(y=k\mid x\right)" alt="P(y=k | x)" /> for each class <img src="https://latex.codecogs.com/png.latex?k=1,\dots,K" alt="k = 1, …, K" />, forming a full probability distribution across all classes.

## Key Concepts  
### Independent vs. Dependent Variables  
- **Independent variables** <img src="https://latex.codecogs.com/png.latex?x" alt="x" /> are the inputs we observe (e.g., pixel intensities).  
- **Dependent variable** <img src="https://latex.codecogs.com/png.latex?y" alt="y" /> is the target label and must be one of <img src="https://latex.codecogs.com/png.latex?K" alt="K" /> discrete values (class indices) ([en.wikipedia.org](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)).  

### Multiclass Strategies  
1. **Direct (Multinomial) Approach:** Train a single model to minimize the multinomial loss via the **softmax** activation over <img src="https://latex.codecogs.com/png.latex?K" alt="K" /> linear scores ([scikit-learn.org](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html?utm_source=chatgpt.com)).  
2. **One-vs-Rest (OvR):** Fit <img src="https://latex.codecogs.com/png.latex?K" alt="K" /> binary classifiers, each distinguishing one class from all others; at prediction, choose the class with the highest score ([scikit-learn.org](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html?utm_source=chatgpt.com)).  
3. **One-vs-One (OvO):** Fit <img src="https://latex.codecogs.com/png.latex?K(K-1)/2" alt="K(K–1)/2" /> classifiers for each pair of classes; use majority voting at prediction time ([scikit-learn.org](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html?utm_source=chatgpt.com)).  

## The Softmax Function  
The **softmax** function generalizes the sigmoid to multiple dimensions:  
<img src="https://latex.codecogs.com/png.latex?\dpi{150}\text{softmax}(z)_k=\frac{e^{z_k}}{\sum_{j=1}^K e^{z_j}}" alt="softmax(z)_k = e^{z_k} / ∑_{j=1}^K e^{z_j}" />,  
where <img src="https://latex.codecogs.com/png.latex?z=[z_1,\dots,z_K]" alt="z = [z₁, …, z_K]" /> are the raw scores (logits) for each class ([en.wikipedia.org](https://en.wikipedia.org/wiki/Softmax_function?utm_source=chatgpt.com)). It ensures each <img src="https://latex.codecogs.com/png.latex?P(y=k\mid x)" alt="P(y=k | x)" /> ∈ (0,1) and <img src="https://latex.codecogs.com/png.latex?\sum_kP(y=k\mid x)=1" alt="∑_k P(y=k | x) = 1" />.

## Model Formulation  
For feature vector <img src="https://latex.codecogs.com/png.latex?x" alt="x" /> and parameter matrix <img src="https://latex.codecogs.com/png.latex?\Theta=[\theta_1,\dots,\theta_K]" alt="Θ = [θ₁, …, θ_K]" /> (each <img src="https://latex.codecogs.com/png.latex?\theta_k" alt="θₖ" /> includes a bias term), the model defines:  
<img src="https://latex.codecogs.com/png.latex?\dpi{150}P(y=k\mid x;\Theta)=\frac{e^{\theta_k^T x}}{\sum_{j=1}^K e^{\theta_j^T x}}" alt="P(y=k | x; Θ) = e^{θₖᵀ x} / ∑_{j=1}^K e^{θⱼᵀ x}" />.  
At prediction, the class with the highest probability is chosen.

## Cost Function & Optimization  
### Categorical Cross-Entropy  
The loss over <img src="https://latex.codecogs.com/png.latex?m" alt="m" /> samples is  
<img src="https://latex.codecogs.com/png.latex?\dpi{150}J(\Theta)=-\frac{1}{m}\sum_{i=1}^m\sum_{k=1}^K y_{i,k}\log P(y=k\mid x^{(i)};\Theta)" alt="J(Θ) = -1/m Σ_{i=1}^m Σ_{k=1}^K y_{i,k} log P(y=k | x^(i); Θ)" />,  
where <img src="https://latex.codecogs.com/png.latex?y_{i,k}" alt="y_{i,k}" /> is 1 if sample <img src="https://latex.codecogs.com/png.latex?i" alt="i" /> belongs to class <img src="https://latex.codecogs.com/png.latex?k" alt="k" />, else 0 ([geeksforgeeks.org](https://www.geeksforgeeks.org/categorical-cross-entropy-in-multi-class-classification/?utm_source=chatgpt.com)). This loss is **convex** in <img src="https://latex.codecogs.com/png.latex?\Theta" alt="Θ" />, yielding a unique global minimum.

### Optimization  
Parameters can be learned by **batch**, **stochastic**, or **mini-batch gradient descent**, or by higher-order solvers such as **L-BFGS** and **SAGA**, which are implemented in libraries like scikit-learn ([scikit-learn.org](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html?utm_source=chatgpt.com)).

## Implementation in Scikit-Learn  
```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Example with K=3 classes (e.g., Iris dataset)
X = np.array([[5.1, 3.5], [4.9, 3.0], [6.3, 3.3], [5.8, 2.7]])
y = np.array([0, 0, 1, 2])  # class labels 0,1,2

# Create multinomial logistic regression model
clf = LogisticRegression(
    multi_class='multinomial',  # direct softmax-based optimization
    solver='lbfgs',             # efficient for multinomial loss
    C=1.0                       # inverse regularization strength
)
clf.fit(X, y)  # train model

# Predict class probabilities for new samples
probs = clf.predict_proba(np.array([[5.0, 3.0], [6.0, 2.5]]))
print(probs)
```
- `multi_class='multinomial'` uses the softmax loss over all classes ([scikit-learn.org](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html?utm_source=chatgpt.com));  
- Solvers `lbfgs`, `saga`, and `newton-cg` support multinomial optimization;  
- `C` controls L2 regularization (smaller → stronger penalty).

## Visualization  
Decision boundaries for multinomial and OvR approaches can be plotted to compare classification regions; direct multinomial logistic often yields smoother boundaries ([scikit-learn.org](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html?utm_source=chatgpt.com)).

## Applications  
- **Digit recognition (MNIST):** Classify handwritten digits (0–9) with >90% accuracy using multinomial logistic regression ([scikit-learn.org](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html?utm_source=chatgpt.com)).  
- **Species classification (Iris):** Canonical example with three flower species.  
- **Text categorization:** Assign documents to one of several topics.  
- **Image classification:** Classify images into categories (e.g., animals, vehicles, buildings).  
- **Sentiment analysis:** Classify text as positive, negative, or neutral.  
- **Spam filtering:** Classify emails as spam or not spam.