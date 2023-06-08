import streamlit as st

def calculator():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.selectbox(
        "Select an operation:",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )

    result = None

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Cannot divide by zero.")

    if result is not None:
        st.success("Result: {}".format(result))


calculator()
