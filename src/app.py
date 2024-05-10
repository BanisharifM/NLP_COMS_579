# src/app.py
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))

import streamlit as st
from weaviate_client import create_client
import os


# if st.button("Home"):
#     st.switch_page("your_app.py")
# if st.button("Page 1"):
#     st.switch_page("pages/page_1.py")
# if st.button("Page 2"):
#     st.switch_page("pages/page_2.py")

# import streamlit as st


def main():
    st.title("Initialize RAG App")

    # Sidebar for input
    with st.sidebar:
        st.header("Functions / Pages")
        st.markdown("* Initialize Weaviate")
        st.markdown("* Initialize Lama")
        st.markdown("* Create corpus")
        st.markdown("* Reset corpus")
        st.markdown("* Upload file")
        st.markdown("* Query")

    # Main content area
    st.subheader("Client Credentials")
    weaviate_url = st.text_input("Weaviate Cluster URL", "")
    weaviate_api_key = st.text_input("Weaviate API keys", "", type="password")
    # client_secret = st.text_input(
    #     "Client Secret", "Enter Client Secret", type="password"
    # )
    # st.write(f"RUL:  {weaviate_url}")
    # st.write(f"API:  {weaviate_api_key}")
    # Token information
    # token_info = st.empty()  # Placeholder for token info
    if st.button("Connect to Weaviate"):
        env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
        with open(env_path, "r") as file:
            lines = file.readlines()

        with open(env_path, "w") as file:
            for line in lines:
                if line.startswith("WCS_CLUSTER_URL"):
                    file.write(f"WCS_CLUSTER_URL='{weaviate_url}'\n")
                elif line.startswith("WCS_API_KEY"):
                    file.write(f"WCS_API_KEY='{weaviate_api_key}'\n")
                else:
                    file.write(line)

        st.info("Environment variables updated successfully!")
        client = create_client()
        if client.is_ready():
            st.success("Client is successfully connected to Weaviate and ready to use.")
        else:
            st.error(
                "Client is not ready. Please check the connection settings or environment."
            )


if __name__ == "__main__":
    main()
