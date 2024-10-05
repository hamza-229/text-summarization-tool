import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.title("Text Summarization Tool")

input_text = st.text_area("Enter your text here:", height=200)

if st.button("Summarize"):
    if input_text:
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.write("**Summary:**")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
