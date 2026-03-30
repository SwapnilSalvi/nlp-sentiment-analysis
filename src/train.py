import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from preprocessing import clean_text
from features import get_vectorizer

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# 1. Load dataset
df = pd.read_csv("../data/reviews.csv")

# 2. Clean text
df['review'] = df['review'].apply(clean_text)

# 3. Convert text → numbers
vectorizer = get_vectorizer()
X = vectorizer.fit_transform(df['review'])

# 4. Labels
y = df['sentiment'].map({'positive': 1, 'negative': 0})

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

# 6. Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# 7. Save model & vectorizer
pickle.dump(model, open(model_path, "wb"))
pickle.dump(vectorizer, open(vectorizer_path, "wb"))

print("✅ Model trained and saved!")
