from sklearn.linear_model import LogisticRegression  # brings in our classification algorithm
import numpy as np                                  # gives us easy tools to work with arrays of numbers

# 1) Prepare our input data (features):
#    We have 6 examples, each a single number: hours studied.
X = np.array([[1], [2], [3], [4], [5], [6]])
#    Notice the shape: it’s a 2-dimensional array (6 rows × 1 column).
#    Even when there’s only one feature, most ML libraries expect a 2D “matrix” of shape (n_samples, n_features).

# 2) Prepare our output data (labels):
#    For each of those 6 students, we know if they passed (1) or failed (0).
y = np.array([0, 0, 0, 1, 1, 1])
#    This is a 1-dimensional array of length 6.

# 3) Create the model (classifier):
clf = LogisticRegression()
#    Under the hood, logistic regression will learn a function that takes hours studied
#    and outputs a probability of “pass”.  If probability ≥ 0.5 it predicts class 1 (pass),
#    otherwise class 0 (fail).

# 4) Train the model on our data:
clf.fit(X, y)
#    The .fit() method looks at every (X[i], y[i]) pair and finds the best parameters
#    (weights and bias) that minimize classification errors.

# 5) Make a prediction on new data:
prediction = clf.predict(np.array([[6.5]]))
#    We ask: if someone studies 3.5 hours, will they pass or fail?
#    predict() returns an array of class labels—in our case [1] meaning “pass”.

# 6) Interpret and print the result:
result = "Pass" if prediction[0] == 1 else "Fail"
print(f"Predicted result for 3.5 hours: {result}")
# Output: Predicted result for 3.5 hours: Pass
