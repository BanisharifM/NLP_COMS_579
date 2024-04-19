from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {
            "role": "assistant",
            "content": "The Los Angeles Dodgers won the World Series in 2020.",
        },
        {"role": "user", "content": "Where was it played?"},
    ],
)

# print(client.is_ready())

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
#         },
#         {
#             "role": "user",
#             "content": "Compose a poem that explains the concept of recursion in programming.",
#         },
#     ],
# )

# print(completion.choices[0].message)
