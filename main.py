import streamlit as st
import backend as bk
import time

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
    response.write("Casper")
    def gen_output():
        """
        Generate response from backend in a streaming manner.
        """
        response = bk.Q_and_A_Chatbot(text, user_prompt)
        for char in response.split(" "):
            yield char + " "
            time.sleep(0.05)
    
    st.write_stream(gen_output)