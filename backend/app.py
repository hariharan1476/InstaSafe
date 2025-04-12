from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict_text  # Make sure this function is defined properly

app = Flask(__name__)
CORS(app)

# Optional home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "🚀 InstaSafe NLP Backend is Live!"})

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # Check for empty or whitespace-only input
    if not text.strip():
        return jsonify({"error": "Input text is empty."}), 400

    try:
        prediction = predict_text(text)  # Using your imported function
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/predict")
def test_predict_page():
    return {"message": "Use POST method to send text for prediction."}

if __name__ == "__main__":
    app.run(debug=True, port=3000)
