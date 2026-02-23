import streamlit as st 

st.title("simple Chatbot")

Question = st.text_input("Ask me anything")

if st.button("Send"):
    st.write(f"You asked \"{Question}\"")
    st.write("Chatbot is Gathering resources .......")
