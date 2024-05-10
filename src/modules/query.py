# src/modules/query.py
import streamlit as st
from file_query import query


def run():
    st.subheader("Have Query Here!")

    question = st.text_input("Type your question", "")
    response = query(question, index)
