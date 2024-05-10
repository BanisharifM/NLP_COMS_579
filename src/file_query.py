# src/file_query.py

from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.postprocessor import SentenceTransformerRerank


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
