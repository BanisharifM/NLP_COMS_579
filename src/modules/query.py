# src/modules/query.py
import streamlit as st
from file_query import query
import pickle


# Function to load index
def load_index(filename="index.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


# Example usage in your query function
def run():
    st.subheader("Let's have a query on your PDF fil!")
    question = st.text_area("Ask your question", "")

    similarity_top_k = st.number_input("Top K", step=1, format="%d", value=5)
    answer_word_number = st.slider("Alex", value=15)

    index = load_index()
    if not index:
        st.error("Index not found. Please upload and process a file first.")
        return
    if st.button("Answer it"):
        response = query(question, index, similarity_top_k, answer_word_number)
        st.write(response)