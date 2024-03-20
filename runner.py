import weaviate
import yaml
import os


# Function to load YAML configuration
def load_config(filepath):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)


# Load the configuration
config = load_config("configs/weaviate_cluster.yml")

# Access the URL and API key from the configuration
weaviate_url = config["url"]
api_key = config["api_key"]

with weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key),
) as client:
    print(client.is_ready())

# schema = {
#    "classes": [
#        {
#            "class": "BlogPost",
#            "description": "Blog post from the Weaviate website.",
#            "vectorizer": "text2vec-openai",
#            "moduleConfig": {
#                "generative-openai": {
#                     "model": "gpt-3.5-turbo"
#                 }
#            },
#            "properties": [
#                {
#                   "name": "Content",
#                   "dataType": ["text"],
#                   "description": "Content from the blog post",
#                }
#             ]
#         }
#     ]
# }

# client.schema.delete_all()

# client.schema.create(schema)

# print("Schema was created.")

print("Hello World")
