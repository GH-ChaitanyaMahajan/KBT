import streamlit as st 

st.title("Welcome to basic streamlit app")

age = st.slider("Select yout age ",1 , 100)
city = st.selectbox("Select your city",["Delhi","Mumbai","Nashik","Pune","Banglore"])

if st.button("Show Details"):
    st.write(f"Age : {age}")
    st.write(f"City : {city}")

st.markdown("""
<style>
            
            .stButton > button
            {
            background-color : green;
            color:white;
            border-radius:50%;
            }
</style>




""",unsafe_allow_html=True)