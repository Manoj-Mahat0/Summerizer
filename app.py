import streamlit as st
from transformers import pipeline

# Specify the model you want to use
model_name = "sshleifer/distilbart-cnn-12-6"  # or any other suitable model
summarizer = pipeline("summarization", model=model_name)

st.title("Article Summarizer")

article = st.text_area("Enter the article text here:")

if st.button("Summarize"):
    if article:
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)
        st.write("**Summary:**")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
