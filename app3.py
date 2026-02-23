import streamlit as st 

st.title("Basics Calcutor ")

num1 = st.number_input("Enter your first number : ")
num2 = st.number_input("Enter your second number :")




operation = st.selectbox("Choose Op",["add" , "sub" , "mul" , "div"])

if st.button("Calculate"):
    if operation == "add":
        st.write(f"Addition is {num1+num2}")

    elif operation == "sub":
        st.write(f"Subtraction is {num1-num2}")
    
    elif operation == "mul":
        st.write(f"Multiplication is{num1*num2}")
    
    elif operation == "div":
        if num2 == 0:
            st.error("Divisor cannor be zero .")
        else:
            st.write(f"Division is {num1/num2}")
