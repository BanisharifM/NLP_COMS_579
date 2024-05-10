import weaviate
from dotenv import load_dotenv
import os


def create_client():
    # Load environment variables from .env file
    load_dotenv(override=True)

    # Get environment variables
    weaviate_url = os.getenv("WCS_CLUSTER_URL")
    weaviate_api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))

    try:
        # Connect to Weaviate
        client = weaviate.Client(url=weaviate_url, auth_client_secret=weaviate_api_key)

        # Check connection to Weaviate
        if client.is_ready():
            return client
        else:
            return None
    except Exception as e:
        return None
