import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
st.title("Text Summarization Tool")

input_text = st.text_area("Enter your text here:", height=200)

if st.button("Summarize"):
    if input_text:
        output = query({
	    "inputs": input_text,
    })
        st.write("**Summary:**")
        st.write(output[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
