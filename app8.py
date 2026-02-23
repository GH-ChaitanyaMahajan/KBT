import streamlit as st 
import google.generativeai as genai

st.title("Welcome to my genai app")

user = st.text_input("ask me anything")
genai.configure(api_key = "AIzaSyDn5awyp03f343tFSJQHs_accstYayzQh8")

genai.GenerativeModel("models/gemini-2.5-flash")

if user:
    response = model.generate_content(user)
    st.write("respones from genai")
    st.write(response.text)