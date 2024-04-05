import os
import weaviate
from dotenv import load_dotenv


def main():

    # Load environment variables from .env file
    load_dotenv()

    # Set the Environment
    weaviate_url = os.getenv("WCS_CLUSTER_URL")
    weaviate_api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))

    # Connect to the Weaviate
    client = weaviate.Client(url=weaviate_url, auth_client_secret=weaviate_api_key)

    # Check connection to the weaviate
    print(client.is_ready())


if __name__ == "__main__":
    main()
