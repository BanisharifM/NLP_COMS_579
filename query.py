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

Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
Settings.embed_model = OpenAIEmbedding()

# Configure logging
logging.basicConfig(level=logging.ERROR)


def load_data(path):
    # Load data
    documents = SimpleDirectoryReader(input_files=[path]).load_data()
    # print(documents)
    return documents


def document_to_nodes(documents):
    # create the sentence window node parser w/ default settings
    node_parser = SentenceWindowNodeParser.from_defaults(
        window_size=3,
        window_metadata_key="window",
        original_text_metadata_key="original_text",
    )
    # Extract nodes from documents
    nodes = node_parser.get_nodes_from_documents(documents)
    return nodes


def vector_index(index_name, client, nodes):
    # Construct vector store
    vector_store = WeaviateVectorStore(weaviate_client=client, index_name=index_name)
    # Set up the storage for the embeddings
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # If an index with the same index name already exists within Weaviate, delete it
    if client.schema.exists(index_name):
        client.schema.delete_class(index_name)

    # Setup the index
    # build VectorStoreIndex that takes care of chunking documents
    # and encoding chunks to embeddings for future retrieval
    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
    )

    return index


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


def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--question", type=str, required=True, help="What is your question"
    )
    args = parser.parse_args()
    return args


def query(question_text, index):
    # The target key defaults to `window` to match the node_parser's default
    postproc = MetadataReplacementPostProcessor(target_metadata_key="window")

    # BAAI/bge-reranker-base
    # link: https://huggingface.co/BAAI/bge-reranker-base
    rerank = SentenceTransformerRerank(top_n=5, model="BAAI/bge-reranker-base")

    # The QueryEngine class is equipped with the generator
    # and facilitates the retrieval and generation steps
    query_engine = index.as_query_engine(
        similarity_top_k=6,
        vector_store_query_mode="hybrid",
        alpha=0.5,
        node_postprocessors=[postproc, rerank],
    )

    # Use your Default RAG
    response = query_engine.query(question_text)
    return response


def main():

    # Load Arguments
    args = load_arguments()

    # Read PDF File
    documents = load_data("Documents/SAM.pdf")

    # Extract nodes from documents
    nodes = document_to_nodes(documents)

    # Connect to the Weaviate Cluster
    client = create_client()

    index_name = "MyExternalContext"

    index = vector_index(index_name, client, nodes)

    # response = client.schema.get(index_name)

    # print(json.dumps(response, indent=2))
    response = query(args.question, index)

    print("------------------\n")

    print("response: ", str(response))

    # window = response.source_nodes[0].node.metadata["window"]
    # sentence = response.source_nodes[0].node.metadata["original_text"]

    # print(f"Window: {window}")
    # print("------------------")
    # print(f"Original Sentence: {sentence}")


if __name__ == "__main__":
    main()
