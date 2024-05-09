import streamlit as st

# Create a simple text input
user_input = st.text_input("Enter your name:", "Type here...")

# Display the input
st.write(f"Hello, {user_input}!")
