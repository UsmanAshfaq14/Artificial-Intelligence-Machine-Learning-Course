# Lecture 1: Machine Learning Introduction and Types

## 1. What is Machine Learning?
Machine Learning (ML) is a branch of artificial intelligence that enables computers to learn patterns from data and make decisions or predictions without being explicitly programmed for each task.

## 2. Types of Machine Learning
- **Supervised Learning**: Learns from labeled data (input–output pairs).
- **Unsupervised Learning**: Finds structure in unlabeled data (e.g., clustering).
- **Reinforcement Learning**: Learns by interacting with an environment and receiving rewards or penalties.

## 3. Classical Machine Learning Pipeline
A series of steps followed to build an ML system:

```
[Data Collection] → [Preprocessing] → [Feature Engineering] → [Modeling] → [Evaluation] → [Deployment]
```

1. **Data Collection**: Gather raw data from sources (databases, sensors, surveys).
2. **Preprocessing**: Clean data (handle missing values, remove outliers).
3. **Feature Engineering**: Create informative inputs (scaling, encoding categorical variables).
4. **Modeling**: Choose and train an algorithm (e.g., linear regression, decision trees).
5. **Evaluation**: Assess performance using metrics (accuracy, MSE) on test data.
6. **Deployment**: Integrate the model into an application or service.

---

## 4. Supervised Machine Learning 
Supervised learning uses labeled examples to learn a mapping from inputs to outputs.

### 4.1 Regression vs. Classification
- **Regression**: Predicts a continuous value (e.g., house price).
- **Classification**: Predicts a discrete class label (e.g., spam vs. not spam).

### 4.2 Simple Code Examples

#### 4.2.1 Linear Regression Example
```python
# Simple Linear Regression with scikit-learn
from sklearn.linear_model import LinearRegression  # Model class
import numpy as np                               # Array library

# Input data: hours studied
X = np.array([[1], [2], [3], [4], [5]])  # 2D array with one feature
# Output data: exam scores
y = np.array([50, 55, 65, 70, 75])       # 1D array of targets

# Create model instance
model = LinearRegression()
# Train model on data
model.fit(X, y)

# Predict score for a student who studies 6 hours
predicted_score = model.predict(np.array([[6]]))
print(f"Predicted score for 6 hours: {predicted_score[0]:.2f}")
```

#### 4.2.2 Logistic Regression Example
```python
# Simple Classification with Logistic Regression
from sklearn.linear_model import LogisticRegression  # Classification model
import numpy as np                                  # Array library

# Input data: hours studied
X = np.array([[1], [2], [3], [4], [5], [6]])
# Output data: pass (1) or fail (0)
y = np.array([0, 0, 0, 1, 1, 1])

# Create classifier instance
clf = LogisticRegression()
# Train classifier
clf.fit(X, y)

# Predict outcome for 3.5 study hours
prediction = clf.predict(np.array([[3.5]]))
result = "Pass" if prediction[0] == 1 else "Fail"
print(f"Predicted result for 3.5 hours: {result}")
```

### 4.3 Components of Supervised Learning
- **Labeled Data**: Examples with known outputs (features and targets).
- **Hypothesis (Model)**: A function \( h_	heta(x) \) that maps inputs to predictions.
- **Cost Function**: Measures prediction error (e.g., Mean Squared Error for regression).
- **Optimizer**: Algorithm to adjust model parameters to minimize the cost (e.g., Gradient Descent).
