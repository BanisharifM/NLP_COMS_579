# src/load_data.py

from llama_index.core import SimpleDirectoryReader


def load_data(path):
    # Load data
    documents = SimpleDirectoryReader(input_files=[path]).load_data()
    # print(documents)
    return documents
