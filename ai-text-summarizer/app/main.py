import streamlit as st
from app.summarizer import summarize_text

st.title("AI Text Summarizer")

text = st.text_area("Enter text to summarize:")
if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        st.success("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text.")
