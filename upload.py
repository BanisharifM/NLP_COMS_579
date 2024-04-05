import os
import weaviate
from dotenv import load_dotenv
from pathlib import Path
import argparse
from llama_index.readers.file import PDFReader


def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_file", type=str, required=True, help="pdf file path")
    parser.add_argument("--chunk_size", type=int, default=500, help="chunk size")
    args = parser.parse_args()
    return args


def read_pdf(path):
    loaded_pdf = PDFReader().load_data(Path(path))
    return loaded_pdf


def main():
    # Load Arguments
    args = load_arguments()

    # Load environment variables from .env file
    load_dotenv()

    # Set the Environment
    weaviate_url = os.getenv("WCS_CLUSTER_URL")
    weaviate_api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))

    # Connect to the Weaviate
    client = weaviate.Client(url=weaviate_url, auth_client_secret=weaviate_api_key)

    # Check connection to the weaviate
    print(client.is_ready())

    # Load pdf file
    loaded_file = read_pdf(args.pdf_file)
    print(f"number of pages: {len(loaded_file)}")


if __name__ == "__main__":
    main()
