import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# Converts text into numerical vectors using the TF-IDF approach,
# which evaluates the importance of words relative to the entire dataset.
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# A machine learning algorithm that builds multiple decision trees and
# combines their outputs for classification.
from sklearn.metrics import confusion_matrix, classification_report
# Metrics to evaluate model performance.
import kagglehub

# Download the dataset
path = kagglehub.dataset_download("abdallahwagih/spam-emails")
print(path)
# Read the dataset
file_path = f"{path}/spam.csv"
data = pd.read_csv(file_path, encoding='latin-1')

# Encode Categorys (ham = 0, spam = 1)
data['Category'] = data['Category'].map({"ham": 0, "spam": 1})

# Features and Categorys
X = data['Message']
y = data['Category']

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(X)
# TfidfVectorizer: Converts text into numerical features by analyzing word importance.
# stop_words: Removes common words like "the", "is", etc., to focus on meaningful terms.
# max_features: Limits the vocabulary size to the top 5000 most important words.

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# Splits data into 70% training and 30% testing subsets.
# stratify=y: Ensures balanced distribution of labels in both sets.

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
# RandomForestClassifier: A machine learning algorithm that builds multiple decision trees and

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Make predictions on new data
new_data = ["Hello! How are you?", "Meeting at 3:00 pm","Win a $1000 cash prize or a prize worth $5000"]
new_data = vectorizer.transform(new_data)
predictions = model.predict(new_data)
print("Predictions:", predictions)
# vectorizer.transform: Converts new text data into the same format as the training data.
# model.predict: Predicts whether each message is spam or ham.

# # Plotting ROC curve
import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve, auc
# fpr, tpr, thresholds = roc_curve(y_test, y_pred)
# # roc_curve: Calculates the false positive rate (FPR) and true positive rate (TPR) for different thresholds.
# roc_auc = auc(fpr, tpr)
# # auc: Calculates the area under the ROC curve.
# plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
# plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver Operating Characteristic')
# plt.legend(loc="lower right")
# plt.show()
#
# # Diagnosing Overfitting and Underfitting
# # Using Learning Curves
# from sklearn.model_selection import learning_curve
#
# train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10))
# # learning_curve: Generates learning curves for a machine learning model.
# # X: Features
# # y: Target variable
# # cv: Number of cross-validation folds
# # train_sizes: Percentage of training data to use for each iteration
#
# plt.plot(train_sizes, train_scores.mean(axis=1), label='Training Score')
# plt.plot(train_sizes, test_scores.mean(axis=1), label='Validation Score')
# plt.xlabel('Training Size')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.title('Learning Curves')
# plt.show()

# Using Validation Curves
from sklearn.model_selection import validation_curve

param_range = np.linspace(1, 100, 10)
train_scores, test_scores = validation_curve(model, X, y, param_name='n_estimators', param_range=param_range, cv=5)
# validation_curve: Generates validation curves for a machine learning model.
# X: Features
# y: Target variable
# param_name: Name of the parameter to vary
# param_range: Range of values to use for the parameter
# cv: Number of cross-validation folds

plt.plot(param_range, train_scores.mean(axis=1), label='Training Score')
plt.plot(param_range, test_scores.mean(axis=1), label='Validation Score')
plt.xlabel('n_estimators')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Validation Curves')
plt.show()
