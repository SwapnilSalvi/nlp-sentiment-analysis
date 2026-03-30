import re
import nltk 
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    
    # 3. Tokenization (split into words)
    words = text.split()
    
    # 4. Remove stopwords (like: is, the, and, etc.)
    words = [word for word in words if word not in stop_words]
    
    # 5. Join words back
    return " ".join(words)