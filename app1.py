import streamlit as st 

st.title("Simple input app")
name = st.text_input("Enter your name : ")

if st.button("SUBMIT"):
    st.write(f"Hello  {name}") 