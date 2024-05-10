import streamlit as st
import importlib


def main():
    with st.sidebar:
        st.header("RAG Application")
        page = st.radio(
            "Go to",
            [
                "Initialize Weaviate",
                "Upload file",
                "Query",
            ],
        )

    page_to_module = {
        "Initialize Weaviate": "initialize_weaviate",
        "Upload file": "upload_file",
        "Query": "query",
    }

    if page in page_to_module:
        module_name = page_to_module[page]
        module = importlib.import_module(f"modules.{module_name}")
        module.run()


if __name__ == "__main__":
    main()
