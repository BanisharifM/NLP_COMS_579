import weaviate
import weaviate.classes as wvc
import os
import requests
import json
import yaml
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

# Load environment variables from .env file
load_dotenv()


# Function to load YAML configuration
def load_config(filepath):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)


# Load the configuration
# config = load_config("configs/weaviate_cluster.yml")

# Access the URL and API key from the configuration
# weaviate_url = config["url"]
# api_key = config["api_key"]

weaviate_url = os.getenv("WCS_CLUSTER_URL")
api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))

client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=api_key,
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_APIKEY"]},
)

print(client.is_ready())

try:
    # Check if the collection exists
    existing_collections = client.schema.get()["classes"]
    collection_names = [col["class"] for col in existing_collections]

    if "Question" not in collection_names:
        # If the collection doesn't exist, create it
        questions = client.schema.create_class(
            {
                "class": "Question",
                "vectorizer": "text2vec-openai",
                "properties": [
                    {
                        "name": "answer",
                        "dataType": ["text"],
                    },
                    {
                        "name": "question",
                        "dataType": ["text"],
                    },
                    {
                        "name": "category",
                        "dataType": ["text"],
                    },
                ],
            }
        )

    # ===== import data =====
    resp = requests.get(
        "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
    )
    data = json.loads(resp.text)  # Load data

    question_objs = []
    for i, d in enumerate(data):
        question_objs.append(
            {
                "class": "Question",
                "properties": {
                    "answer": d["Answer"],
                    "question": d["Question"],
                    "category": d["Category"],
                },
            }
        )

    # Batch insert the data objects
    client.batch.create_objects(question_objs)
    print("Data insertion complete.")

finally:
    print("Client is closed!")
    client.close()

