import streamlit as st

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
    cluster_url = st.text_input("Weaviate Cluster URL", "WCS_CLUSTER_URL")
    weaviate_api_key = st.text_input(
        "Weaviate API keys", "WCS_API_KEY", type="password"
    )
    client_secret = st.text_input(
        "Client Secret", "Enter Client Secret", type="password"
    )

    # Token information
    token_info = st.empty()  # Placeholder for token info
    if st.button("Generate Token"):
        token = "Bearer/JWT token generated. It will expire in 30 minutes. To-regenerate, please call acquire_jwt_token()."
        token_info.info(token)

    # Options
    st.checkbox("From CLI")
    st.checkbox("Continuously Run")

    # Footer
    st.text("Powered by Funix.io, minimally building apps in Python")


if __name__ == "__main__":
    main()
