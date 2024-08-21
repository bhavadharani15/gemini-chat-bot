import streamlit as st
import google.generativeai as genai

st.title("welcome to my app")
text=st.text_input("Enter your question:")



genai.configure(api_key="AIzaSyA_qHoz35cLVzuQprrNEObeBLmhVOpgzt4")


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("click me"):
    response=chat.send_message(text)
    st.write(response.text)