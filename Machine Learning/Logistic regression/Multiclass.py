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