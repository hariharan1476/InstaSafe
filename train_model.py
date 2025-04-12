import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

print("📥 Loading datasets...")

# Load datasets
offensive_df = pd.read_csv("/Users/hari1476/Desktop/instasafe/clean_data/offensive_dataset.csv")
non_offensive_df = pd.read_csv("/Users/hari1476/Desktop/instasafe/clean_data/non_offensive_dataset.csv")

# Combine them
combined_df = pd.concat([offensive_df, non_offensive_df], ignore_index=True)

# Check class distribution
print("Label distribution:\n", combined_df['label'].value_counts())

# Preprocessing
combined_df.dropna(inplace=True)
X = combined_df['text']
y = combined_df['label']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train Model
clf = LinearSVC()
clf.fit(X_train, y_train)

# Evaluation
y_pred = clf.predict(X_test)
print("\n🔍 Model Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(clf, 'model/nlp_model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("\n✅ Model and vectorizer saved to 'model/' directory")
