import vectara
import importlib
importlib.reload(vectara)
import os

VECTARA_CUSTOMER_ID=2899834543
VECTARA_CLIENT_ID="zut_rNf2ryIFNdu2pg6HC1VvxXOyCu3MkfxzzMKJ2Q"
VECTARA_CLIENT_SECRET="zqt_rNf2rxxf3F84QJhWa_j8HZkOE2GYzYB3dje9yg"


VECTARA_CUSTOMER_ID = str(os.environ.get("VECTARA_CUSTOMER_ID"))
VECTARA_CLIENT_ID = str(os.environ.get("VECTARA_CLIENT_ID"))
VECTARA_CLIENT_SECRET = str(os.environ.get("VECTARA_CLIENT_SECRET"))


# optional, if you are using a proxy like LlaMasterKey https://github.com/TexteaInc/LlaMasterKey/
VECTARA_BASE_URL="https://vectara-prod-2899834543.auth.us-west-2.amazoncognito.com/oauth2/token"
# VECTARA_BASE_URL="https://api.vectara.io/v1/list-corpora"
client = vectara.vectara(VECTARA_CUSTOMER_ID, VECTARA_CLIENT_ID, VECTARA_CLIENT_SECRET, VECTARA_BASE_URL)

corpus_id =  3

# client.upload(corpus_id, 'one_file.pdf', description='My precious doc')  # add one file to the corpus 
# client.upload(corpus_id, 'a_folder_of_documents') # add all files under a folder to the corpus
# client.upload(corpus_id, ['user_manual.md', 'notes.txt'], description=['user manual', 'my memory']) # add a list of files to the corpus

client.query(corpus_id, 'can i bring my velociraptor to the office', top_k=5) # query the corpus for top 5 answers

client.reset_corpus(corpus_id) # delete all documents in the corpus

