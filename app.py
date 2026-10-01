from flask import Flask, render_template, request, jsonify
import pickle
import os


app = Flask(__name__)


# Load trained model
model_path = os.path.join(
    "model",
    "medicine_model.pkl"
)

with open(model_path, "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    symptoms = data.get("symptoms", "").strip()

    if not symptoms:
        return jsonify({
            "error": "Please enter your symptoms."
        }), 400

    prediction = model.predict([symptoms])[0]

    probabilities = model.predict_proba([symptoms])[0]

    confidence = max(probabilities) * 100

    return jsonify({
        "medicine": prediction,
        "confidence": round(confidence, 2)
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )