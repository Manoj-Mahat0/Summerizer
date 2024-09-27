import streamlit as st
from transformers import pipeline

# Initialize the summarizer
summarizer = pipeline("summarization")

# Streamlit app
st.title("Article Summarizer")

# Input text area for article
article = st.text_area("Paste your article here:", height=300)

# Input fields for summary length
max_length = st.number_input("Maximum length of summary:", min_value=10, max_value=500, value=130)
min_length = st.number_input("Minimum length of summary:", min_value=10, max_value=500, value=30)



# Button to generate summary
if st.button("Generate Summary"):
    if article:
        with st.spinner("Generating summary..."):
            summary = summarizer(article, max_length=max_length, min_length=min_length, do_sample=False)
            st.success("Summary generated!")
            st.write("### Summary:")
            st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter an article to summarize.")

# Show the article word count
if article:
    word_count = len(article.split())
    st.write(f"The article has {word_count} words.")
