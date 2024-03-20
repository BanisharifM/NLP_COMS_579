import requests
import json

url = "https://api.vectara.io/v1/list-corpora"

payload = json.dumps({
  "numResults": 10,
  "filter": "[Tt][Ee][Ss][Tt]"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'customer-id': '2899834543',
  'x-api-key': 'zut_rNf2ryIFNdu2pg6HC1VvxXOyCu3MkfxzzMKJ2Q'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)