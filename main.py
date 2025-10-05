import streamlit as st
import backend as bk

st.set_page_config(page_title = "CasperAI", page_icon = ":books:", layout = "centered")


st.title("CasperAI")

pdf_file = st.file_uploader(label = "", type = ["pdf"])
user_prompt = st.chat_input(placeholder = "Ask Casper")

if pdf_file and user_prompt:
    message = st.chat_message("user")
    response = st.chat_message("assistant")
    message.write(user_prompt)
    text = bk.extractPdf(pdf_file)
    # st.session_state["pdf_text": text]
    response.write(bk.Q_and_A_Chatbot(text, user_prompt))