# weaviate_client.py
import os
import weaviate

from dotenv import load_dotenv


def create_client():
    # Load environment variables from .env file
    load_dotenv()

    # Set the Environment
    weaviate_url = os.getenv("WCS_CLUSTER_URL")
    weaviate_api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))

    # Connect to Weaviate
    client = weaviate.Client(url=weaviate_url, auth_client_secret=weaviate_api_key)

    # Check connection to Weaviate
    if client.is_ready():
        print("Client is successfully connected to Weaviate and ready to use.")
    else:
        print(
            "Client is not ready. Please check the connection settings or environment."
        )

    return client
