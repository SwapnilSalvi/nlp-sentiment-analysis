import pickle
from src.preprocessing import clean_text
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# Load model & vectorizer
model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

def predict_sentiment(text):
    # Clean text
    cleaned = clean_text(text)
    
    # Convert to vector
    vector = vectorizer.transform([cleaned])
    
    # predict 
    prediction = model.predict(vector)[0]
    
    # Return result
    return "Positive 😊" if prediction == 1 else "Negative 😡"