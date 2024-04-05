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
    parser.add_argument("--chunk_size", type=int, default=500, help="chunk size")
    parser.add_argument("--chunk_overlap", type=int, default=35, help="chunk overlap")
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

    return client


def clear_client(client):
    client.schema.delete_all()
    print("Client is cleared!")


def read_pdf(path):
    loaded_pdf = PDFReader().load_data(Path(path))
    return loaded_pdf


def chunk_file(loaded_file, chunk_size, chunk_overlap):
    file_parser = SimpleNodeParser.from_defaults(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    file_chunks = file_parser.get_nodes_from_documents(loaded_file)
    return file_chunks


def embed_file(chunk_file, client):

    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    vector_store = WeaviateVectorStore(weaviate_client=client, index_name="TestIndex")

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    embedded_file = VectorStoreIndex(chunk_file, storage_context=storage_context)

    print("File Successfully indexed & Weaviate Panel client is updated!")

    return embedded_file


def main():
    # Load Arguments
    args = load_arguments()

    client = create_client()

    clear_client(client)

    # Check connection to the weaviate
    print(client.is_ready())

    # Load pdf file
    loaded_file = read_pdf(args.pdf_file)
    print(f"number of pages: {len(loaded_file)}")

    chunked_file = chunk_file(loaded_file, args.chunk_size, args.chunk_overlap)

    embed_file(chunked_file, client)


if __name__ == "__main__":
    main()
