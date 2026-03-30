# 🎬 Sentiment Analysis App

## 📌 Overview

This project is an NLP-based Sentiment Analysis system that classifies text as Positive 😊 or Negative 😡 using Machine Learning.

## 🚀 Features

* Text preprocessing (cleaning, stopword removal)
* TF-IDF feature extraction
* Logistic Regression model
* Streamlit web app for real-time predictions

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* Streamlit

## 📂 Dataset

The dataset used in this project is not included in this repository due to size limitations.

You can download it from the link below:

🔗 Dataset Link: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

### 📌 Instructions

1. Download the dataset from the above link
2. Create a folder named `data/` in the project root
3. Place the dataset file inside the `data/` folder

Example structure:

```
project/
│── data/
│   └── reviews.csv
│── src/
│── app.py
│── README.md
```

## 📂 Project Structure

```
nlp-sentiment-analysis/
│── data/
│── models/
│── src/
│── app.py
│── requirements.txt
```

## ▶️ How to Run

1. Clone repo
2. Install dependencies
3. Run:

```
streamlit run app.py
```

## 📊 Example

Input: "This movie is amazing!"
Output: Positive 😊

## 📈 Future Improvements

* Use Deep Learning (LSTM, Transformers)
* Improve accuracy with better preprocessing
* Deploy using cloud platforms

---

✨ Built as part of AI/ML learning journey
