import streamlit as st
import requests

# API URLs and headers
SUMMARY_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
TRANSLATION_API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-ar"
HEADERS = {"Authorization": "Bearer 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"}

# Function to query the summarization API
@st.cache_data(show_spinner=False, ttl=3600)
def summarize_text(text):
    response = requests.post(SUMMARY_API_URL, headers=HEADERS, json={"inputs": text})
    
    # Check if response is valid and contains the summary
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]['summary_text']
        else:
            return None  # If structure is unexpected
    else:
        return None  # If API request fails

# Function to query the translation API
@st.cache_data(show_spinner=False, ttl=3600)
def translate_to_arabic(text):
    response = requests.post(TRANSLATION_API_URL, headers=HEADERS, json={"inputs": text})
    
    # Check if response is valid and contains the translation
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "translation_text" in result[0]:
            return result[0]['translation_text']
        else:
            return None  # If structure is unexpected
    else:
        return None  # If API request fails

# Streamlit UI
st.title("Text Summarization & Translation Tool")

# Input text area
input_text = st.text_area("Enter your text to summarize:", height=200)

if st.button("Summarize Text"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text)
        
        if summary:
            st.success("Summarization successful!")
            st.write("**Summary:**", summary)
        else:
            st.error("Failed to summarize. Please try again later.")

st.header("Translate Summary to Arabic")

if st.button("Translate Summary"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize first.")
    else:
        summary = summarize_text(input_text)  # Ensure summary is created
        
        if summary:
            with st.spinner("Translating to Arabic..."):
                translation = translate_to_arabic(summary)
            
            if translation:
                st.success("Translation successful!")
                st.write("**Arabic Translation:**", translation)
            else:
                st.error("Failed to translate. Please try again later.")
        else:
            st.error("Please summarize the text first before translating.")

