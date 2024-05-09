# src/app.py
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))

import streamlit as st
from weaviate_client import create_client


# if st.button("Home"):
#     st.switch_page("your_app.py")
# if st.button("Page 1"):
#     st.switch_page("pages/page_1.py")
# if st.button("Page 2"):
#     st.switch_page("pages/page_2.py")

# import streamlit as st


def main():
    st.title("Initialize Weaviate Clusters")

    # Sidebar for input
    with st.sidebar:
        st.header("Functions / Pages")
        st.markdown("* Initialize Vectara")
        st.markdown("* Create corpus")
        st.markdown("* Reset corpus")
        st.markdown("* Upload file")
        st.markdown("* Query")

    # Main content area
    st.subheader("Client Credentials")
    weaviate_url = st.text_input("Weaviate Cluster URL", "WCS_CLUSTER_URL")
    weaviate_api_key = st.text_input(
        "Weaviate API keys", "WCS_API_KEY", type="password"
    )
    # client_secret = st.text_input(
    #     "Client Secret", "Enter Client Secret", type="password"
    # )

    # Token information
    token_info = st.empty()  # Placeholder for token info
    if st.button("Connect to Weaviate"):
        print(weaviate_url)
        print(weaviate_api_key)
        client = create_client()
        if client.is_ready():
            msg = "Client is successfully connected to Weaviate and ready to use."
        token_info.info(msg)


if __name__ == "__main__":
    main()
