import streamlit as st
from transformers import pipeline

# Set up the summarization pipeline with a specified model
model_name = "sshleifer/distilbart-cnn-12-6"  # You can choose a different model if needed
summarizer = pipeline("summarization", model=model_name)

# Set the maximum length of the article input
MAX_ARTICLE_LENGTH = 1000  # Set a limit for the article length

# Title of the app
st.title("Article Summarizer")

# Text area for user input
article = st.text_area("Enter the article text here:", max_chars=MAX_ARTICLE_LENGTH)

# Summarization button
if st.button("Summarize"):
    if article:
        # Generate the summary
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)
        st.write("**Summary:**")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
