# src/file_query.py

from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings
import logging


Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
Settings.embed_model = OpenAIEmbedding()

# Configure logging
logging.basicConfig(level=logging.ERROR)


def query(question_text, index, answer_word_number):
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
    if answer_word_number:
        question_text += f" write the answer in {answer_word_number} words."
    response = query_engine.query(question_text)
    return response
