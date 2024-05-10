# src/pages/upload_file.py

import streamlit as st
from document_to_node import document_to_nodes
from load_data import load_data
from save_file import save_file
from weaviate_client import create_client
from vector_index import vector_index
import os

# from weaviate_client import create_client
# import os


def run():
    st.subheader("Upload a PDF file")
    file = st.file_uploader("Chose your PDF file:", type="pdf")

    if file is not None:
        # Save the file to a temporary file
        tmp_file_path = save_file(file)

        # Now you can pass the path to your load_data function
        if st.button("Upload file"):
            documents = load_data(tmp_file_path)

            # Process documents into nodes or other structures as needed
            nodes = document_to_nodes(documents)

            # Connect to the Weaviate Cluster
            client = create_client()

            if not client or not client.is_ready():
                st.error(
                    "Failed to connect to Weaviate. Please check the connection settings or ensure the API key is valid."
                )
                st.info(
                    "You can go to Initialize Weaviate page to check your connection to Weaviate."
                )
                os.unlink(tmp_file_path)
                return

            index_name = "MyExternalContext"

            index = vector_index(index_name, client, nodes)

            st.write(index)

            # Clean up the temporary file if no longer needed
            os.unlink(tmp_file_path)
