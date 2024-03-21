import weaviate
import weaviate.classes as wvc
import os
import requests
import json
import yaml
from dotenv import load_dotenv
from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

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
weaviate_api_key = weaviate.auth.AuthApiKey(os.getenv("WCS_API_KEY"))
openai_api_key=os.environ["OPENAI_APIKEY"]

client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate_api_key,
    headers={"X-OpenAI-Api-Key": openai_api_key },
)

print(client.is_ready())

try:

    questions = client.collections.create(
        name="Question_new",
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
        generative_config=wvc.config.Configure.Generative.openai(),  # Ensure the `generative-openai` module is used for generative queries
    )

    # resp = requests.get(
    #     "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
    # )
    # data = json.loads(resp.text)  # Load data

    # question_objs = list()
    # for i, d in enumerate(data):
    #     question_objs.append(
    #         {
    #             "answer": d["Answer"],
    #             "question": d["Question"],
    #             "category": d["Category"],
    #         }
    #     )

    # questions = client.collections.get("Question")
    # questions.data.insert_many(question_objs)  # This uses batching under the hood

    # # Check if the collection exists
    # existing_collections = client.schema.get()["classes"]
    # collection_names = [col["class"] for col in existing_collections]

    # if "Question" not in collection_names:
    #     # If the collection doesn't exist, create it
    #     questions = client.schema.create_class(
    #         {
    #             "class": "Question",
    #             "vectorizer": "text2vec-openai",
    #             "properties": [
    #                 {
    #                     "name": "answer",
    #                     "dataType": ["text"],
    #                 },
    #                 {
    #                     "name": "question",
    #                     "dataType": ["text"],
    #                 },
    #                 {
    #                     "name": "category",
    #                     "dataType": ["text"],
    #                 },
    #             ],
    #         }
    #     )

    # # ===== import data =====
    # resp = requests.get(
    #     "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
    # )
    # data = json.loads(resp.text)  # Load data

    # question_objs = []
    # for i, d in enumerate(data):
    #     question_objs.append(
    #         {
    #             "class": "Question",
    #             "properties": {
    #                 "answer": d["Answer"],
    #                 "question": d["Question"],
    #                 "category": d["Category"],
    #             },
    #         }
    #     )

    # # Batch insert the data objects
    # client.batch.create_objects(question_objs)
    # print("Data insertion complete.")

finally:
    print("Client is closed!")
    client.close()
