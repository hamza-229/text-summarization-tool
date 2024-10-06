import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

API_URL_TR = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ar"
headers_TR = {"Authorization": "Bearer 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"}

@st.cache_data(show_spinner=False, ttl=3600)
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@st.cache_data(show_spinner=False, ttl=3600)
def query_tr(payload):
    response = requests.post(API_URL_TR, headers=headers_TR, json=payload)
    return response.json()

st.title("Text Summarization Tool")

summary = None

input_text = st.text_area("Enter your text here:", height=200)

if st.button("Summarize"):
    if input_text:
        output = query({"inputs": input_text})
        summary = output[0]['summary_text']
        st.write("**Summary:**")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")

st.header("Translate Summary to Arabic")

if st.button("Translate to Arabic"):
    translation = query_tr({"inputs": summary})
    st.subheader("Translation in Arabic:")
    st.write(translation[0]['translation_text'])
