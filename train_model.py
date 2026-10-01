import pandas as pd
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# Load dataset
data = pd.read_csv("data/medicines.csv")

# Remove missing values
data = data.dropna()

X = data["symptoms"]
y = data["medicine"]


# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )),
    ("classifier", LogisticRegression(max_iter=1000))
])


# Train model
model.fit(X, y)


# Create model directory
os.makedirs("model", exist_ok=True)


# Save trained model
with open("model/medicine_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model trained successfully!")
print("Model saved at model/medicine_model.pkl")