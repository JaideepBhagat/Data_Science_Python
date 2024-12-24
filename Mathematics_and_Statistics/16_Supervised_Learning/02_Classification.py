import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Income": [5000, 6000, 2500, 4000, 7000, 12000, 3000, 10000, 2000, 4500],
    "LoanAmount": [200, 250, 120, 180, 300, 400, 150, 350, 100, 220],
    "CreditHistory": [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    "Approved": [1, 1, 0, 1, 1, 1, 0, 1, 0, 0]
}
df = pd.DataFrame(data)

# 1. Data Preprocessing
X = df[["Income", "LoanAmount", "CreditHistory"]]  # Features
y = df["Approved"]  # Target variable

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train the Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Model Evaluation
# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["Not Approved", "Approved"], yticklabels=["Not Approved", "Approved"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Not Approved", "Approved"]))
"""
classification_report(y_test, y_pred): Generates a report with:
Precision: Proportion of positive predictions that are correct.
Recall: Proportion of actual positives identified correctly.
F1-score: Harmonic mean of precision and recall.
target_names=["Not Approved", "Approved"]: Maps numerical labels to readable class names.
"""

# 4. Make Predictions
# Example: Predict for a new applicant
new_applicant = np.array([[5500, 230, ]])  # Income=5500, LoanAmount=230, CreditHistory=1
approval_status = model.predict(new_applicant)
print(f"Loan approval status for the new applicant: {'Approved' if approval_status[0] == 1 else 'Not Approved'}")
