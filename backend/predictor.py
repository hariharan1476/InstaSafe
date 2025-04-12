import joblib

# Load the saved model and vectorizer
clf = joblib.load('model/nlp_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

# Optional: label map for understanding predictions
label_map = {
    0: "Non-Offensive",
    1: "highly Offensive",
    2: "Moderate Offensive"
}

def predict_text(text):
    X_input = vectorizer.transform([text])
    pred = clf.predict(X_input)[0]
    return label_map.get(pred, f"Unknown ({pred})")

# Example usage
if __name__ == "__main__":
    input_text = input("Enter a message to classify: ")
    result = predict_text(input_text)
    print(f"\n🧠 Prediction: {result}")
