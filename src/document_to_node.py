# src/documents_to_node.py

from llama_index.core.node_parser import SentenceWindowNodeParser


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
