import streamlit as st 

st.title("Sample Form")
st.subheader("Enter Details :")

name = st.text_input("Enter Name :")
age = st.number_input("Enter Age :")
gender = st.radio("Select Gender",("Male" , "Female"))
dob = st.date_input("Enter DOB")

if st.button("SUBMIT"):
    st.write(f"Form submited")
    st.write(f"Your details are :")
    st.write(f"Name : {name}")
    st.write(f"Age : {age}")
    st.write(f"Gender : {gender}")
    st.write(f"Date of Birth : {dob}")

st.markdown("""
<style>
            .stTitle > title
            {
            color : green 
            }
            .stButton > button
            {
            background-color : green;
            color:white;
            border-radius:50%;
            }
</style>




""",unsafe_allow_html=True)