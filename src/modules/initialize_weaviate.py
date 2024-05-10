# src/modules/initialize_weaviate.py

import streamlit as st
from weaviate_client import create_client
import os


def run():
    st.subheader("Weaviate Client Credentials")
    weaviate_url = st.text_input("Weaviate Cluster URL", "")
    weaviate_api_key = st.text_input("Weaviate API keys", "", type="password")

    # Token information
    if st.button("Connect to Weaviate"):
        env_path = "/.env"
        with open(env_path, "r") as file:
            lines = file.readlines()

        with open(env_path, "w") as file:
            for line in lines:
                if line.startswith("WCS_CLUSTER_URL"):
                    file.write(f"WCS_CLUSTER_URL='{weaviate_url}'\n")
                elif line.startswith("WCS_API_KEY"):
                    file.write(f"WCS_API_KEY='{weaviate_api_key}'\n")
                elif line.startswith("OPENAI_API_KEY"):
                    file.write(
                        f"WCS_API_KEY='sk-proj-minvC1eLAqg47COAkrCWT3BlbkFJ73QYcQnoCK8lZNiRp6th'\n"
                    )
                else:
                    file.write(line)

        st.info("Environment variables updated successfully!")
        client = create_client()
        if client and client.is_ready():
            st.success("Client is successfully connected to Weaviate and ready to use.")
        else:
            st.error(
                "Failed to connect to Weaviate. Please check the connection settings or ensure the API key is valid."
            )
