# src/modules/query.py
import streamlit as st
from file_query import query
import pickle
from llama_index.core.settings import Settings
import logging
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceWindowNodeParser
import weaviate
from dotenv import load_dotenv
import os
import argparse
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.weaviate import WeaviateVectorStore
import json
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.postprocessor import SentenceTransformerRerank
import logging
from pdf_gen import pdf_gen

Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
Settings.embed_model = OpenAIEmbedding()

# Configure logging
logging.basicConfig(level=logging.ERROR)
import globals


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

    answer_word_number = st.slider("Answer length", value=15)

    index = globals.index
    if not index:
        st.error("Index not found. Please upload and process a file first.")
        return
    if st.button("Answer it"):
        response = str(query(question, index, answer_word_number))
        pdf_gen(response)
        st.write(response)
        st.success("Mask out a PDF file from the RAG system generated successfully!")
