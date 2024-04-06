import os
import weaviate
from dotenv import load_dotenv
from pathlib import Path
import argparse

from llama_index.readers.file import PDFReader
from llama_index.core import (
    Settings,
    StorageContext,
    VectorStoreIndex,
)
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_file", type=str, required=True, help="pdf file path")
    parser.add_argument("--chunk_size", type=int, default=250, help="chunk size")
    parser.add_argument("--chunk_overlap", type=int, default=10, help="chunk overlap")
    parser.add_argument(
        "--model_name", type=str, default="BAAI/bge-small-en-v1.5", help="model name"
    )
    args = parser.parse_args()
    return args


def create_client():

    # Load environment variables from .env file
    load_dotenv()

    # Set the Environment
    weaviate_url = os.getenv("WCS_CLUSTER_URL")
    weaviate_api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))

    # Connect to the Weaviate
    client = weaviate.Client(url=weaviate_url, auth_client_secret=weaviate_api_key)

    # Check connection to Weaviate
    if client.is_ready():
        print("Client is successfully connected to Weaviate and ready to use.")
    else:
        print(
            "Client is not ready. Please check the connection settings or environment."
        )

    return client


def clear_client(client):
    client.schema.delete_all()
    print("The Weaviate Client Cluster is cleared!")


def read_pdf(path):
    loaded_pdf = PDFReader().load_data(Path(path))
    file_name = os.path.basename(path)
    print("File successfully uploaded!")
    print(f"File {file_name}, has {len(loaded_pdf)} pages.")
    return loaded_pdf


def chunk_file(loaded_file, chunk_size, chunk_overlap):
    print(
        f"Starting to chunk the file with chunk size: {chunk_size} and chunk overlap: {chunk_overlap}"
    )
    file_parser = SimpleNodeParser.from_defaults(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    file_chunks = file_parser.get_nodes_from_documents(loaded_file)
    print(f"File successfully chunked into {len(file_chunks)} chunks.")
    return file_chunks


def embed_file(chunk_file, client, model):
    print(f"Starting to embed the file using the {model} model.")

    Settings.embed_model = HuggingFaceEmbedding(model_name=model)

    vector_store = WeaviateVectorStore(weaviate_client=client, index_name="TestIndex")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    embedded_file = VectorStoreIndex(chunk_file, storage_context=storage_context)

    print("File successfully embedded and stored in Weaviate.")
    return embedded_file


def main():
    # Load Arguments
    args = load_arguments()

    # Connect to the Weaviate Cluster
    client = create_client()

    # Clear the Weaviate Cluster
    clear_client(client)

    # Read PDF File
    loaded_file = read_pdf(args.pdf_file)

    chunked_file = chunk_file(loaded_file, args.chunk_size, args.chunk_overlap)

    embed_file(chunked_file, client, args.model_name)


if __name__ == "__main__":
    main()
