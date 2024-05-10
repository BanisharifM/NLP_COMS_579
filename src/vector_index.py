# src/vector_index

from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.core import VectorStoreIndex, StorageContext


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
