import streamlit as st
import backend

st.set_page_config(page_title = "WhsiperPDF", page_icon = ":green_book:", layout = "centered")


st.title("WhisperPDF")

st.file_uploader(label = "", type = "PDF")

st.text_area(label = "", placeholder = "Enter Your Prompt")

st.button("Ask Whisper")