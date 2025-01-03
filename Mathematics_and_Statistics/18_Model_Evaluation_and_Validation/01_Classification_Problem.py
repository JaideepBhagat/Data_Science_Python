import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Load the dataset
import kagglehub

# Download the dataset
path = kagglehub.dataset_download("abdallahwagih/spam-emails")

# Read the dataset
file_path = f"{path}/spam.csv"  # Adjust file name if necessary
data = pd.read_csv(file_path, encoding='latin-1')

# Check the dataset structure
print("Dataset head:\n", data.head())

# Rename columns for consistency (if required)
data = data.rename(columns={"Category": "label", "Message": "text"})

# Encode labels (ham = 0, spam = 1)
data['label'] = data['label'].map({"ham": 0, "spam": 1})

# Features and labels
X = data['text']
y = data['label']

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

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