import streamlit as st
import sys
import os

from src.predict import predict_sentiment

# Title
st.title("🎬 Sentiment Analysis App")

# Input box
user_input = st.text_area("Enter your text here:")

# Button
if st.button("Analyze Sentiment"):
    if user_input.strip() != "":
        result = predict_sentiment(user_input)
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter some text!")