import streamlit as st

st.title("Smart Calculator")
st.write("Performs basic mathematical calculations quickly and easily.")

# User Inputs
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

operation = st.selectbox(
    "Choose an operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

if st.button("Calculate"):

    if operation == "Addition (+)":
        answer = num1 + num2
        st.success(f"Result: {answer}")

    elif operation == "Subtraction (-)":
        answer = num1 - num2
        st.success(f"Result: {answer}")

    elif operation == "Multiplication (×)":
        answer = num1 * num2
        st.success(f"Result: {answer}")

    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
        else:
            answer = num1 / num2
            st.success(f"Result: {answer}")

st.markdown("---")
st.caption("Built using Python and Streamlit.")