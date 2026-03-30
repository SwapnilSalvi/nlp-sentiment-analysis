from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectorizer():
    vectorizer = TfidfVectorizer(max_features=5000)
    return vectorizer